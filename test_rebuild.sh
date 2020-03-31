rm -rfd build
mkdir build

{
    cargo build --release --target-dir build
}
# && {
#    echo '-- Running python tests --'
#    nosetests --rednose -v ../tests  
#}

