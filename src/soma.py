from ctypes import cdll

lib = cdll.LoadLibrary("release/libsoma.dylib")

def process():
    lib.process()

