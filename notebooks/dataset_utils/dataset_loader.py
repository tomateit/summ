# Some chunks are from https://github.com/abisee/cnn-dailymail/blob/master/make_datafiles.py
from pathlib import Path
from .cnndm_preprocessor import cleaning_function

"""
    Output format
 {"text": "", "highlights":""}
"""
CNN_DIR = Path("../data/cnn/stories").resolve()
DM_DIR = Path("../data/dailymail/stories").resolve()
HIGHLIGHTS = "@highlight"

dm_single_close_quote = u'\u2019' # unicode
dm_double_close_quote = u'\u201d'
END_TOKENS = ['.', '!', '?', '...', "'", "`", '"', dm_single_close_quote, dm_double_close_quote, ")"] # acceptable ways to end a sentence

# These are the number of .story files we expect there to be in cnn_stories_dir and dm_stories_dir
num_expected_cnn_stories = 92579
num_expected_dm_stories = 219506

def fix_missing_period(line):
    """Adds a period to a line that is missing a period"""
    if "@highlight" in line: return line
    if line=="": return line
    if line[-1] in END_TOKENS: return line
    # print line[-1]
    return line + " ."

f = "ffff522cebe5ad9dcfb6dfc476b8f423f3f8dd34.story"
def get_sample():
    with open(CNN_DIR/f, "r") as inp:
        lines = inp.readlines()
        lines = map(fix_missing_period, lines)
        text = " ".join(lines)
        chunks = text.split(HIGHLIGHTS)
        text, *highlights = map(cleaning_function, chunks)
        highlights = " ".join(highlights)
        return (text, highlights)


