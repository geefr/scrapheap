
cmake_minimum_required(VERSION 3.17)

project(geefr-vcpkg-cmake-template)

find_package(fmt REQUIRED)

add_executable( main src/main.cpp )
target_link_libraries( main PUBLIC fmt::fmt )

