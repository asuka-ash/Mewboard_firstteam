#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>
#include <atomic>
#include <iostream>
#include <utility>
#include <memory>

struct MyArray {int z[50]; };
struct MyStr {int a, b;};


int main(int argc, char const *argv[])
{
    // std::atomic<int> speed (0);
    // auto concurrentSpeed = speed.load();

    std::atomic<MyArray> myArray;
    std::atomic<MyStr> myStr;

    std::cout << std::boolalpha
              << "std::atomic<myArray> is lock free? "
              << std::atomic_is_lock_free(&myArray) << std::endl
              << "std::atomic<myStr> is lock free? " 
              << std::atomic_is_lock_free(&myStr) << std::endl;

}

