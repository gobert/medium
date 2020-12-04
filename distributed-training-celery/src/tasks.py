from celery import Celery

app = Celery(
    "worker",
    backend="redis://localhost:6379/0",
    broker="redis://localhost:6379/0",
)


@app.task
def fit(city):
    import random
    import time

    print("RECEIVED: TRAIN MODEL IN {}".format(city))
    print("Load data")
    print("Compute features")
    print("Split train  / test")
    print("Train the model")
    print("Evaluate on the testing set")
    accuracy = random.randint(0, 42)
    print(f"Compute metric: RMSE={accuracy}")
    print("-" * 100)

    # simulate some training time
    time.sleep(random.randint(5, 20))

    # return accuracy
    return accuracy


@app.task
def shutdown():
    print("Got task: shutdown all workers")
    app.control.shutdown()
