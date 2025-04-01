# GPU Programming in C++
Coming soon... Not sure how much desire there is for a C++ GPU tutorial. Maybe focus on Python:

- Drop in replacement -> `cupy`
- Compiled with numba -> `numba.cuda`
- Coding cuda kernels?
- Working with tensors? -> `torch`

## Introduction
Expanding on the [OpenMP tutorial](parallel-cpp.md), one might be interested in how to write parallel code in C++ that is designed to make use of the GPU rather than the CPU.

In this tutorial, we will first discuss the "calculate $\pi$" example. We shall implement a GPU version of the code and discuss the performance and the downfalls of this code. We will then discuss in more detail when GPU programming is more suitable than CPU programming, and use some examples to illustrate the case uses for both.


## Calculating $\pi$

