# Thailand Smart ID Card
Read and Get from Thailand Smart ID Card using **python**

### Installing on macOS from the source distribution
1. Make sure It has **GCC** Compiler
2. Install **automake, libtool, pcre**

    ```
    brew install automake
    brew install libtool
    brew install pcre
    brew install pcsc-lite
    ```

3. Install  [**swig**](http://www.swig.org)

    ```
    cd swig
    ./configure
    make
    sudo make install
    ```

4. Install **pyscard**

    ```
    virtual env
    source env/bin/activate
    pip3 install pyscard
    ```

5. Finish `deactivate`
