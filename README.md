# Thailand Smart ID Card

Installing on macOS from the source distribution
-------------------------------------------------------------
0. GCC

1. automake, libtool, pcre
```
brew install automake
brew install libtool
brew install pcre
brew install pcsc-lite
```
2. swig (http://www.swig.org)
```
cd swig
./configure
make
sudo make install
```
3. ```pip install pyscard```
