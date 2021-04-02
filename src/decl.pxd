cdef extern from 'Soma.h' namespace 'soma':
    cdef cppclass HelloWorld:
        HelloWorld() except +
