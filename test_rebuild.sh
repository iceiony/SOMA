mkdir build

cd build

cmake ../src
make -j4

echo \n---Cythonising and running python Tests---\n
python setup.py build_ext --inplace
nosetests --rednose -v ../tests 

cd ../
