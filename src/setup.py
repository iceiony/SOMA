from distutils.core import setup, Extension
from Cython.Build import cythonize


ext = Extension(
    "soma",
    ["soma.pyx"],
    language="c++",
    libraries=['soma'],
    include_dirs=['.'],
    runtime_library_dirs = ['.']
    ,extra_compile_args = ['-stdlib=libc++']
    #,extra_link_args = ['-v']
    )

setup(ext_modules=cythonize(ext, language_level = "3"))
