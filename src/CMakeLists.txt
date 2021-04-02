project(dynet)
cmake_minimum_required(VERSION 3.16 FATAL_ERROR)

add_library(soma Soma.h Soma.cpp)
target_link_libraries(soma)

configure_file(./setup.py . COPYONLY)
configure_file(decl.pxd . COPYONLY)
configure_file(decl.pyx . COPYONLY)

file(GLOB SOMA_HEADERS *.h)
file(COPY ${SOMA_HEADERS} DESTINATION .)
