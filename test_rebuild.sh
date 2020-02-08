mkdir build

cd build

{
    echo '-- Compiling C++ shared library --'
    cmake ../src
    make -j4 
} && {
    echo '-- Cythonising and running python Tests --'
    python setup.py build_ext --inplace 
} && {
    echo '-- Running python tests --'
    nosetests --rednose -v ../tests  
}

cd ../
