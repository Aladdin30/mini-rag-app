# mini-rag 

this is a minimal implementation of the rag  model for question answering.


## Requirements
- Python 3.8 or later

1)Download and install Miniconda 

2)Create a new environment

## Setup the environment variables

```bash

$ cp .env.example .env

```

Set your environment variables in the '.env' file. Like 
'OPENAI_API_KEY' value. 

## Run Fast Api 

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 5000

```
