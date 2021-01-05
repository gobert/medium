# Distributed training with celery

Code for the article [How to scale the training of several models?](https://gobert.medium.com/how-to-scale-the-training-of-several-models-64180480ca3d#eba2-408b17077985-reply)


# Installation
* You need pyenv and poetry installed. Then: `poetry install`
* You need docker

# Run-me
1. Start redis locally on port 6359 with `docker run -p 6379:6379 redis`
2. Start several workers with: `poetry run bin/worker.sh`. Do it at least twice in 2 tabs
3. Start the master (once) with: `poetry run python bin/master.py`
