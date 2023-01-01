from celery import shared_task
import time


@shared_task
def long_await(some_time):
    print(f'я буду ожидать {some_time} секунд')
    time.sleep(some_time)
    print(f'спасибочки за ожидание :>')