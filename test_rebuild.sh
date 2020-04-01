rm -rfd build
mkdir build

{
    cargo build --release --target-dir build
} && {
    cp src/*.py build
} && {
    cd build
    echo '-- Running python tests --'
    nosetests --rednose -v ../tests  
    cd ../
}

