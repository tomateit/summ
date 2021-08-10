# Project that implements constrained summarization
Here I've assembled a little demo on what exactly can summarization can do.

### What does the app do:
1. Takes a text
2. Takes a goal number of sentences
3. Magically produces output :) (for details check out `notebooks/` folder)

## Launching the project locally
1. `git clone` the repository
2. `cd summ`
3. `docker-compose up` to create a docker image and launch it
4. Navigate to `127.0.0.1:8911/` in your browser for a demo page.

### REST
1. Send a `POST` request to "/" with json in a form of 
    + `{"text": "your text", "constraint": int}`
2. The result will be in a form of `{"text": "resulting text"}`
3. The REST server is based on FastAPI, so refer to `/docs` for API details.

## The sweetest part is in /notebooks folder
- I provide several approaches to the tasks with some research on the topic 
- Some baseline models 
- As well as some ideas on how to improve the quality



