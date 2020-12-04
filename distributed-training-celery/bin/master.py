import tasks

remote_tasks = {}


def fit_async():
    for city in ["PARIS", "LONDON", "PRAGUE", "ISTANBUL"]:
        remote_task = tasks.fit.delay(city)
        remote_tasks[city] = remote_task


def wait_for_workers():
    import time

    while True:
        pending_tasks = {
            city: remote_task
            for city, remote_task in remote_tasks.items()
            if not remote_task.ready()
        }
        done_tasks = {
            city: remote_task
            for city, remote_task in remote_tasks.items()
            if remote_task.ready()
        }

        print(f"Tasks done: {list(done_tasks.keys())}")
        print(f"Tasks pending: {list(pending_tasks.keys())}")
        print("-" * 10)

        if len(pending_tasks) == 0:
            return
        else:
            time.sleep(5)


def get_results():
    import statistics

    rmses = []
    for r in remote_tasks.values():
        rmse = r.get()
        rmses.append(rmse)
    print("Mean RMSE accross all cities: {}".format(statistics.mean(rmses)))


def kill_workers():
    tasks.shutdown.delay()


if __name__ == "__main__":
    fit_async()
    wait_for_workers()
    get_results()
    kill_workers()
