project(dynet)
cmake_minimum_required(VERSION 3.16 FATAL_ERROR)

add_library(shapes Rectangle.cpp Rectangle.h)
target_link_libraries(shapes)
