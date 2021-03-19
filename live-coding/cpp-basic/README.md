# C++ / CMake Live Coding Harness

'live' in the sense that it's a repeated build.

I use this when prototyping functions, or testing snippets when I need to avoid long build times.

This isn't really suitable for projects with dependencies, but you could drop them into CMakeLists.txt

* Should work on any bash terminal, including windows
* Requires CMake in your path
* Uses your default generator (edit go.sh if you want ninja/similar non-default)

```shell
mkdir build; cd build
../go.sh
```

