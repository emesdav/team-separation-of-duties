import os
import sys

# Unfortunately we do not have enough time to implement
# a smarter session controller
# But this seems at the very basic to solve the problem

global_user_id = 0


class Session:
    def __init__(self, internal_user_id):
        self.internal_user_id = internal_user_id

    def start(self):
        global global_user_id
        global_user_id = self.internal_user_id
        return global_user_id

    def stop(self):
        global global_user_id
        global_user_id = 0
        self.internal_user_id = 0
        os.execl(sys.executable, sys.executable, *sys.argv)
        return global_user_id
