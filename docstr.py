"""I am: docstr.__doc"""


def func():
    """I am: docstr.func.__doc__"""
    pass


class Spam:
    """I am: spam.__doc__ or docstr.spam.__doc__"""

    def method(self):
        """I am: spam.method.__doc__ or self.method.__doc__"""
        pass
