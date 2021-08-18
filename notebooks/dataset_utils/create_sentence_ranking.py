import argparse
import torch
from transformers import AutoTokenizer, AutoModel
from sklearn.cluster import KMeans
from scipy.spatial.distance import euclidean as  euclidean_distance
from pathlib import Path
from functools import partial
import numpy as np
from typing import List, Dict
from tqdm import tqdm
import json

def read_jsonl(path) -> List[Dict[str, List[str]]]:
    buffer = []
    with open(path, "r") as fin:
        for line in fin:
            buffer.append(json.loads(line))
    return buffer

tokenizer = AutoTokenizer.from_pretrained("cointegrated/LaBSE-en-ru")
model = AutoModel.from_pretrained("cointegrated/LaBSE-en-ru")
kmns = KMeans(n_clusters=1) # May be varying/adaptive ?

def sort_vectors_by_centroid_distance(vecs: List[torch.Tensor]) -> List[int]:
    kmns.fit(vecs)
    centroid = kmns.cluster_centers_[0]
    dists_to_centroid = []
    for idx in range(len(vecs)):
        dist = euclidean_distance(vecs[idx], centroid)
        dists_to_centroid.append(dist)
    return np.argsort(dists_to_centroid).tolist()

def create_ranking(arguments):
    input_file = Path(arguments.file_path).resolve()
    if not input_file.exists():
        raise Exception("File must exist")
    if input_file.is_dir():
        raise Exception("Provide path to file, not dir")

    output_path = Path(arguments.write_path).resolve()
    output_path.mkdir(exist_ok=True)
    output_file = output_path / "sent_id.jsonl"

    tokenize = partial(tokenizer, padding=True, truncation=True, max_length=512, return_tensors='pt')
    data = read_jsonl(input_file)

    rankings = []
    for chunk in tqdm(data):
        text = chunk["text"]
        if not text:
            rankings.append([]) # we can't just skip em because it will spoil the alignment
            continue
        tokenized_sents = tokenize(text)
        with torch.no_grad():
            model_output = model(**tokenized_sents)
            embeddings = model_output.pooler_output
            embeddings = torch.nn.functional.normalize(embeddings)
            rankings.append(sort_vectors_by_centroid_distance(embeddings))

    with open(output_file, "w") as fout:
        for line in rankings:
            line = json.dumps(dict(sent_id=line)) + "\n"
            fout.write(line)
        print(f"Wrote {len(rankings)} lines to {output_file.name}")

    
    
    


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(
        description='Create sentence ranking for futher truncation'
    )
    parser.add_argument('--file_path', type=str, required=True,
        help='Path to the original dataset file in a form of {text: [str], summary: [str]}')
    parser.add_argument('--write_path', type=str, required=True,
        help='Path to dir to store the rankings {sent_id: [int]}')

    args = parser.parse_args()

    create_ranking(args)