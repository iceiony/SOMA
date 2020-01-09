from distutils.core import setup, Extension
from Cython.Build import cythonize


ext = Extension(
    "shape",
    ["shape.pyx"],
    language="c++",
    libraries=['shapes'],
    include_dirs=['.'],
    runtime_library_dirs = ['.']
    )

setup(ext_modules=cythonize(ext))
