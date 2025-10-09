from datetime import datetime
hour=datetime.now().hour


def time(start,end):
    def time_decorator(func):
        def wrapper():
            if start<=hour<=end:
                func()
            else:
                print('not allow')    
        return wrapper
    return time_decorator

@time(start=5,end=19)
def do_work():
    print("working ....")

do_work()