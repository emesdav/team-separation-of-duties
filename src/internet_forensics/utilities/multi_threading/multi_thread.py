"""
The purpose of this file is to implement the required
function for handling multi-threading, i.e.,
concurrent requests or execution of operations by at
least two users at the same time in the context
of this application.
"""

from concurrent.futures import Future
from threading import Thread


def function_w_future_obj(fn, future: Future, args, kwargs) -> None:
    """
    Run a function on separate threads leveraging a
    'Future' object for multi-threading.

    Args:
        fn: function to run on separate threads
            for concurrent execution.
        future: an object of the Future class.
    """
    try:
        result = fn(*args, **kwargs)
        future.set_result(result)
    except Exception as exc:
        future.set_exception(exc)


def threaded(fn) -> Future:
    """
    Define the decorator-type of function to enable a
    function to be multi-threaded.

    Args:
        fn: function to run on separate threads for
            concurrent execution.
    """
    def wrapper(*args, **kwargs):
        future = Future()
        Thread(
            target=function_w_future_obj, args=(fn, future, args, kwargs)
        ).start()
        return future
    return wrapper
