mkdir build

cd build

cmake ../src
make -j4
python setup.py build_ext --inplace

cd ../
