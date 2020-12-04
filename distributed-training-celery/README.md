# Distributed training with celery


# Installation
* You need pyenv and poetry installed. Then: `poetry install`
* You need docker

# Run-me
1. Start redis locally on port 6359 with `docker run -p 6379:6379 redis`
2. Start several workers with: `poetry run bin/worker.sh`. Do it at least twice in 2 tabs
3. Start the master (once) with: `poetry run python bin/master.py`
