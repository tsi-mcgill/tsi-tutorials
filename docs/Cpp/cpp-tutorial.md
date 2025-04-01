# Introduction to C++

## What is the aim of this tutorial?

The aim of this tutorial is to provide you with an introduction to the C++ programming language. I assume that you have some background in programming, so I will skip topics like boolean logic. I'll also assume that you are not coming from a computer science background. We'll skip topics such as references and pointers, which may be the subject of a future workshop. Instead, we will focus on the core components involved in writing a C++ program.

By the end of this tutorial, you will be able to do the following:

- **Understand data types:** You will understand some of the different data types in C++ and when you might want to use one over the other.
- **Understand the structure of C++ code:** You'll understand how to structure your code and learn some of the best practices.
- **Understand loops and statements:** You'll understand how `for` and `while` loops work. We'll also touch on `do while` loops. We'll also learn how to control flow using `if` - `else if` - `else` statements.
- **Use arrays and vectors:** We'll look at how to create arrays and vectors. We'll learn about some best practices for memory safety.
- **Functions:** You'll understand how to write reusable code using functions. We'll learn the difference between a value and a reference when dealing with functions.
- **Parsing files and strings:** You'll understand how to print to the command line and to files. You'll learn how to read text files, parse them, and extract useful information.

## How to run this tutorial

The code used in this tutorial is available on [GitHub](https://github.com/steob92/c-plus-plus-tutorial). I strongly recommend checking out the exercise branch and trying to work along with the notes here. Try to answer the problems before reading the solutions. If you get stuck, you can always check out the solutions branch.

To run this tutorial, you'll need `g++` or `clang++` installed. These can be installed through the `gcc` or `clang` packages. Instructions on how to install these can be found [here](https://github.com/steob92/c-plus-plus-tutorial). Alternatively, you can compile all the examples using the [GCC Docker image](https://hub.docker.com/_/gcc). You can pull the latest Docker image using:

```bash
docker pull gcc
```

## Simplifying Docker Setup

To save time and streamline your Docker setup, consider pre-downloading the necessary image. Once you have the image, you can easily create a container to compile and execute your code. Here's how to do it:

1. **Pull the Docker Image:**

    Use the following command to pull the `gcc` image:

    ```bash
    docker pull gcc
    ```
    This command downloads the image and stores it locally on your system.


2. **Create a Docker Container:**

    Now, you can create a Docker container for compiling and running your code. Use the following command:
    ```bash 
    docker run -it --rm -v $(pwd):/data -w /data gcc bash
    ```

    Let's break down this command:

    * `docker run`` initiates a new container.
    * `-it` specifies that you want an interactive shell.
    * `--rm` automatically removes the container when you exit.
    * `-v $(pwd):/data` mounts the current directory into the container at the location /data.
    * `-w /data` sets the working directory to /data within the container.

## What is C++

C++ is one of the most influential programming languages today, known for its exceptional performance. It empowers developers to create memory-efficient code that often outperforms native Python in terms of speed. Whether you are delving into the world of IoT or tackling high-performance computing, C++ remains a top choice for projects that prioritize efficient memory utilization and speedy execution.

### Key Differences from Python

Coming from a language like Python, you will immediately notice several differences when working with C++:

1. **Compiled Language:**
   Unlike Python, which can be executed through an interpreter, C++ is a "compiled" language. This means that before running C++ code, it must be compiled. Compilation takes code that is relatively readable to humans and transforms it into low-level machine code. One of the benefits of a compiled language is that the compiled program can be highly optimized at compile time, resulting in high-performing code.

2. **Statically-Typed Language:**
   Unlike Python, where variable types are determined at runtime, C++ requires knowing the type of a variable at compile time. Python is a "dynamically-typed" language, allowing you to work with variables without specifying their type in advance. In C++, specifying the type during compilation may seem limiting, but it enables the compiler to optimize the executable for better performance.

3. **Manual Memory Management:**
   In Python, the interpreter regularly pauses execution to check which variables are no longer within scope and to free up memory, thanks to the "garbage collector." While this automated memory management is convenient, it incurs a significant performance overhead. In C++, when a variable goes out of scope, its "destructor" is typically called. The destructor is a function that handles memory cleanup. However, in C++, developers need to be mindful because they can allocate memory dynamically using `new` or `alloc`. Such allocated memory must be explicitly released using `delete` or `dealloc` to avoid memory leaks.

4. **Limited Memory Safety:**
   In Python, attempting to access an element beyond the boundaries of an array, such as the 11th element in a 10-element array, results in an error. In C++, however, such boundary violations allow access to memory that should not be touched. This leads to completely undefined behavior.

5. **Thread-Friendly:**
   Python imposes the "Global Interpreter Lock" (GIL), restricting the execution of CPU-bound tasks to one at a time, regardless of the available cores. This is a memory safety feature aimed at avoiding data races. In C++, there is no such constraint. Developers can create a nearly infinite number of logical threads, and the code can utilize the available CPU cores for temporally concurrent threads. Memory safety and data race avoidance are managed using atomic types or barriers (for more details, see [Introduction to Parallel Programming in C++ with OpenMP](./parallel-cpp.md)).

These differences reflect the unique strengths and characteristics of C++, making it a powerful and versatile programming language.



### Why use C++?

C++ allows us to write fast and memory efficient code that outpaces Python on most metrics. 
Being a compiled language, we can pass pre-compiled binaries to end users, providing highly optimized executables ready for use. 
The low foot print makes C++ ideal for devices such as microcontrollers (e.g. Arduinos), FPGAs and any memory limited devices. 

C++ is very common in scientific programming. 
Complex memory intensive code (such as scientific simulations), often require huge resources.
C++ naturally fufills these requirements, with code that easily scales.


## The Anatomy of a C++ program

### Hello World

Like all good tutorials, we start with the basic "Hello World" example:

```c++ title="hello_world.cpp" linenums="1" 
#include <iostream>

int main(){
    std::cout << "Hello World" << std::endl;

    return 0;
}
```

Here we have an example code that prints "Hello World" to the terminal. Let's talk through this line-by-line.

1. `#include <iostream>` Here we are "including" an external library to our code. We're using the library "iostream", a library that allows us to use functions relating to input and output. `iostream` is part of the C++ standard library, a vast set of code that we can build upon.

2. `int main() {...}` Here we are defining our `main` function. Executables should have a `main` function. This tells the complier that this is the entry point to the program. 

3. `std::cout << "Hello World" << std::endl;` Here we are using `std::cout` to print a message to the screen. We are specifying the standard name space `std`. We pass the string "Hello World" to `std::cout` using `<<`. We then pass an additional arguement `std::endl`. `endl` passes the "end line" command to the `cout` essentially terminating the line. Finally we end the line with `;`. 

4. `return 0` Here we are ending our `main` function by return 0. A program will return an exit code when it terminates. Exit codes tell the user about how the code finishes. An exit code of 0 means the code terminated successfully. We could return any number we want, but 0 typically means a successfull termination.

We can compile this code using either `g++` or `clang++`:
```bash
g++ hello_world.cpp -o hello_world
```

or
```bash
clang++ hello_world.cpp -o hello_world
```

Here the first argument `hello_world.cpp` is the source code we want to compile. We specify the target binary with the `-o` flag. We name the output executable `hello_world`. We can run our code using:

```bash
./hello_world
```


### Data Types

In C++, understanding different data types is crucial due to its static typing nature. While the actual size of these types may vary depending on the compiler and system, here are common data types:

- `int`: Used for integer numbers (e.g., -1, 0, 23). Typically, it occupies 4 bytes or 32 bits.
- `bool`: Represents Boolean values, either `true` or `false`, allowing for Boolean arithmetic.
- `float`: Used for non-integer numbers (e.g., -0.2, 43.4, 12.0) with 32-bit precision.
- `double`: Similar to `float` but with double the precision (64 bits).
- `char`: Represents a single character or small integer value and typically occupies 8 bits (1 byte) of memory.

Additional data types include:

- `unsigned int`: Integer numbers that are unsigned, expanding the maximum possible value of the integer.
- `short int`: Signed integers with half the size (2 bytes or 16 bits).
- `long`: Allows storage of larger numbers than standard `int`, typically occupying 8 bytes or 64 bits.

Beyond these basic types, you will also encounter during this tutorial:

- `string`: A sequence of characters stored as an array of `char` elements, used to represent text or character data.
- `fstream`: Used for file input and output operations, enabling reading from and writing to files.

```c++ title="data_types.cpp" linenums="1" hl_lines="3 10-11"
#include <iostream>
// Include the <limits> header for accessing information about data type limits.
#include <limits>

int main() {

    // int - 4-byte integer (minimum/maximum values):
    int a = 42;
    std::cout << "integer a = " << a << std::endl;
    std::cout << "Minimum value for int: " << std::numeric_limits<int>::min() << std::endl;
    std::cout << "Maximum value for int: " << std::numeric_limits<int>::max() << std::endl;
    

    // Precision of float and double:
    std::cout.precision(20);
    float b = 3.14159265358979323846;
    std::cout << "float b = \t" << b << std::endl;

    double c = 3.14159265358979323846;
    std::cout << "double c = \t" << c << std::endl;
    std::cout << "Full      \t" << "3.14159265358979323846" << std::endl;

    // Display minimum and maximum values for float and double:
    std::cout << "Minimum value for float: " << std::numeric_limits<float>::min() << std::endl;
    std::cout << "Maximum value for float: " << std::numeric_limits<float>::max() << std::endl;

    std::cout << "Minimum value for double: " << std::numeric_limits<double>::min() << std::endl;
    std::cout << "Maximum value for double: " << std::numeric_limits<double>::max() << std::endl;
    
    
    return 0;
}
```

On line 3 we are including the `limits` library. We are using the `std::numeric_limits<T>::min()` and `std::numeric_limits<T>::max()` method to get the minimum and maximum value of a data type `T`. Don't worry too much about the sytax here, they indicate that we're using a template, allowing us to appy these functions to different types of data types.

When we compile this and look at the output we see:
```
integer a = 42
Minimum value for int: -2147483648
Maximum value for int: 2147483647
float b =       3.1415927410125732422
double c =      3.141592653589793116
Full            3.14159265358979323846
Minimum value for float: 1.175494350822287508e-38
Maximum value for float: 3.4028234663852885981e+38
Minimum value for double: 2.2250738585072013831e-308
Maximum value for double: 1.7976931348623157081e+308
```

We can determine the minimum and maximum values for `int`, `float`, and `double`. It's evident that when using a `float` instead of a `double`, precision is reduced. In the example above, the value of $\pi$ is accurate to the 6th decimal place for `float`, but extends to the 15th decimal place for `double`. This difference becomes significant when a high degree of precision is required.

### Namespaces

In C++, namespaces serve as a way to organize and group related code elements, including variables, functions, and classes, into distinct logical scopes. This organization helps prevent naming conflicts and enhances the modularity of your code.

In our examples, we will primarily rely on the "standard" C++ library. It's beneficial to specify which namespace we are using to save us from having to write it out every time.

Consider the `hello_world.cpp` example, where we can streamline the code by explicitly indicating the namespace we're using:

```c++ title="hello_world.cpp" linenums="1" hl_lines="3"
#include <iostream>

using namespace std;

int main(){
    cout << "Hello World" << endl;

    return 0;
}
```

By employing `using namespace std;`, we eliminate the need to specify that we are using `cout` from the `std` namespace. The compiler will automatically assume the `std` namespace.

While the examples we use here may not involve multiple namespaces, it is generally considered good practice to be explicit and specify the namespace of the elements you are using. This helps avoid issues when working with libraries that may contain classes or functions sharing the same names.

### Scopes

In C++ we can make use of multiple "Scopes". You can think of scopes as blocks of code. Within these blocks we can define variables, perform operations, enter nested scopes, etc. In general, when we exit a scope any objects created within that scope will have their `destructor` called once we exit the scope (with the execption of objects created with `new`or  `alloc`). Objects native to a scope cannot be accessed from outside that scope, but objects within a scope can be accessed from within a nested scope. We can define a scope in C++ by wrapping a body of code between curley brackets.

```c++ title="scopes.cpp" linenums="1" hl_lines="5 6 7 13 19 22 28 30 31 36 40"
#include <iostream>

using namespace std;

int main() {
    int a = 123;
    int b = 456;
    
    cout << "a is " << a << endl;
    cout << "b is " << b << endl;

    // Creating a new "nested" scope within our main function
    {
        cout << "Within the nested scope" << endl;
        
        // Here, we are "shadowing" the variable named 'a'.
        // Within the nested scope, we have a new 'a', which temporarily hides the outer 'a'.
        // This is allowed, but it can lead to confusion and is generally considered poor practice.
        int a = 43;  // Shadowing the outer 'a'
        
        // The variable 'c' is created locally within this scope.
        int c = 789;
        
        cout << "a is " << a << endl;    // Refers to the 'a' in the nested scope
        cout << "b is " << b << endl;    // Accesses the outer 'b'
        cout << "c is " << c << endl;    // Refers to the 'c' in the nested scope
        cout << "Leaving the nested scope" << endl;
    }

    cout << "a is " << a << endl;    // Refers to the outer 'a'
    cout << "b is " << b << endl;    // Accesses the outer 'b'

    // This will cause an error!
    // Introduction/scopes.cpp:27:24: error: 'c' was not declared in this scope
    // 36 |     cout << "c is " << c << endl;
    // cout << "c is " << c << endl;
    // This is because 'c' was only local to the nested scope; the outer scope cannot access it.

    return 0;
}
```

On line 3 we define a new scope associated with the `main` function, this scope ends on line 40. We define integers `a` and `b` in the `main` scope. We created a new scope on line 13 which spans until line 28. This scope is "nested" within the main scope. Within this scope we define the integer `a` on line 19. What we are doing here is known as "shadowing" we are borrowing the use of the name within this scope. When we exit the scope the varable `a` reverts back to what it was outside of the scope, this is evident on line 30. On line 22 we define an integer `c` within the scope. This variable is local to the nested scope, but inaccessible to the parent scope (the `main` scope). When we exit the nested scope the `destructor` is called and the variable is dropped. If we uncommented line 36 we would get an error.

Scopes are general blocks of code, we can modify the behaviour of the scope using loops and control access to the scope using statements. We'll learn about these in the next section.


## Flow Control
 In this sections we'll look at how to control the flow of our code using `for`, `while` and `do while` loops and control access to scopes using `if`-`else if` and `else` statements. We won't touch `goto` and neither should you. We may briefly discuss `switch`.

### For loops

`for` loops are used when we have a loop with a known number of iterations or a regular pattern we want to iterate over. In C++ they are defined as follows:

```c++
for ( initialization ; termination ; iteration){
    // block of code to be ran
}
```

The `for` loop has 3 fields each separated by a `;`. You can think of them as the following:
- initialization : What we want to initialize at the start of the loop. This could be variables that we want to modify within the loop. For example `int i = 0;`. We can also initilize multiple variables, for example `int i = 0,  j = 5;`. In this case we are defining `i` within the scope of the `for` loop, but `j` would be local to the parent loop.
- termination : The condition on which we will terminate the loop. This needs to be a boolean. For example if we want to exit the loop when i passes a certain value: `i < 10`. While `i < 10` this will be true, however when `i == 10`, this becomes false so we exit.
- iteration : This field allows us to change something at the end each iteration of the loop. So for example if we want to increase the value of `i` by 1 we could use `i++`

Putting these together we can write a for loop, to loop from 0-9 as follows:
```c++ linenums="1"
// Print out 0-9
for ( int i = 0; i < 10 ; i++ ){
    cout << i << endl;
}
```
Starting at `i = 0` we pass through the loop. When we reach the end of the loop on line 4, `i++` will run and we will restart at the beginning of the loop with `i = 1`. The loop will check if `1 < 10`, find `true` and continue running the loop. This will contiune until `i = 9`, when we finish this iteration of the loop we will apply `i++`, so now `i = 10`. When we try to reenter the loop the `10 < 10` returns `false` and we exit the loop.

You can create an infinite loop by not passing a termination condition.
```c++
// This code will run forever!
for (int i = 0; ; i++){
    // block of code    
}
``` 


!!! info "Creating a for loop using a range"
    Since C++ 11 (the 2011 update of C++), one can loop over ranges and arrays using the following format:
    ```c++ linenums="1"
    int values[] = {0,1,2,3,4,5};
    for (int i: values){
        cout << i << endl;
    }
    ```
### While loops

In C++, `while` loops iterate over a block of code as long as a specified condition is true. The basic format of a `while` loop is as follows:
```c++ linenums="1"
while (condition){
    // block of code
}
```
In boolean logic, any condition that is not `false` or `0` is considered `true`. For instance, `while (1)` and `while (1 < 10)` are equivalent to `while (true)`. Even conditions like `while ("apple")` are treated as true.

Here's an example of a `while` loop that counts from 0 to 9:
```c++ linenums="1"
int i = 0;
while (i < 10){
    cout << i << endl;
    i++;
}
```

You can also create infinite loops by providing a condition that is always `true`:
```c++ linenums="1"
int i = 0;
while (true){
    cout << i << endl;
    i++;
}
```

In the latter example, the loop will continue indefinitely until manually terminated, often by sending a kill command to the program (e.g., `Ctrl + C`).

To include a condition within the `while` loop and control when it should exit, you can use the `break` statement. Here's an example:

```c++ linenums="1" title="while_with_break.cpp" hl_lines="5 6 7"
int i = 0;
while (true){
    cout << i << endl;
    i++;
    if (i > 9 ) {
        break;
    }
}
```
In this example, the loop starts with `i = 0`, prints the value of `i`, increments `i` by one (`i++`), and checks if `i` is greater than 9. After 10 iterations (0 through 9), the `i > 9` condition becomes `true` (`10 > 9`), triggering the `break` statement, which exits the loop.

There is another type of loop known as a `do while` loop. This is very similar to a `while` loop, except the condition is check at the end of the scope, rather than at the start of the scope. 


### Controlling flow with `if`-`else if`-`else`

You can use `if`, `else if`, and `else` statements to control the flow of your program, directing it to different branches or code scopes based on conditions. Here's the format:

```c++ linenums="1" 
if (condition1) {
    // Code block for condition1
} else if (condition2) {
    // Code block for condition2
} else if (condition3) {
    // Code block for condition3
} else {
    // Default code block
}
```

In this example, the program checks conditions one by one. If `condition1` is true, it enters the scope of the first `if`. If it's `false`, it checks `condition2`, and so on. If none of the conditions are true, it enters the `else` block, which serves as the default code. Keep in mind that you always need to start with an `if` statement, but you can omit `else if` or `else` as needed. In the `while_with_break.cpp` example, only an `if` statement was used.

The order of the `else if` statements are also important. If `condition2` and `condition3` are both `true` we will only enter the first block corresponding to `condition2`.

Here's a more detailed example:

```c++ linenums="1"  hl_lines="13 15-21 6-11"
// Loop from 0-infinity 
// Loop from 0 to infinity
int i = 0;
while (true) {

    // Check if i is even using the % operator
    if (i % 2 == 0) {
        cout << i << " is even!" << endl;
    } else {
        cout << i << " is odd!" << endl;
    }

    i++;

    if (i > 10) {
        break;  // Exit the loop if i is greater than 10
    } else if (i == 3) {
        continue;  // Skip to the start of the next iteration if i is 3
    } else {
        cout << "Back to the start!" << endl;  // Print a message if neither condition is true
    }
}
```

In this code, the `%` operator is used for the modulo operation, which returns the remainder of a division operation. `i % 2` will return `0` if the number is even or `1` if the number is odd. We increment the value of `i` by one (line 13) and use a second set of `if` statements (lines 15-21). The first `if` provides a break if `i > 10`, while the `else if` allows us to skip to the start of the next iteration using a `continue` command if i is 3. The `else` block prints a message if neither of these conditions is `true`.

This code will give us the following output:
```bash
0 is even!
Back to the start!
1 is odd!
Back to the start!
2 is even!
3 is odd!
Back to the start!
4 is even!
Back to the start!
5 is odd!
Back to the start!
6 is even!
Back to the start!
7 is odd!
Back to the start!
8 is even!
Back to the start!
9 is odd!
Back to the start!
10 is even!
```

When using `if`-`else if`-`else` we can have an infinite number of `else if` conditions, but only one `if` and at most one `else`. 


### Controling Flow with a Switch

We can also use `switch` statements to control flow.

Switch statements are a useful method for controlling the flow of code. They are particularly effective for handling errors and parsing parameters when the potential outcomes are well-known. 

A `switch` statement can be implemented with the following syntax:
```c++ linenums="1"

switch (value){
    case value_1:
        // block of code
        break;
    case value_2:
        // block of code
        break;
    ...
    case value_n:
        // block of code
        break;
    default:
        // block of code
        break;
}
```

Here, the `value` is a parameter we want to test within the `switch`. When using a `switch`, we test specific cases (`case`). For example, in the `case value_1` branch, we are testing if `value == value_1`. If this is true, then the block of code within that branch will be executed. Notice here that a `break` statement is used at the end of the block of code. This prevents the other branches from being executed by `break`ing from the `switch` construct.



We can have any number of `case` statements within the `switch`. 
You'll notice that there is a special condition called `default`. 
This block will execute if reached regardless of the value.
It specifies the "default" behavior of the code.

For example, we can write a similar block to our `if` statement example:
```c++ linenums="1" hl_lines="2 5 16 17 23 28"
int i = 0;
while (true) {

    // Check if i is even using the % operator
    switch (i % 2) {
        case 0:
            cout << i << " is even!" << endl;
            break;
        case 1:
            cout << i << " is odd!" << endl;
            break;
    }

    i++;

    switch (i){
        case 0 ... 3:
            cout << i << " is between 0 and 3" << endl;
            break;
        case 4:
            cout << i << " is exactly 4" << endl;
            break;
        case 5 ... 7:
            cout << i << " is between 5 and 7" << endl;
            break;
        default:
            cout << i << " greter than 7" << endl;
            return 0;
            
    }
}
```

Here we are using two `switch` statements. 
The first, on line 5, takes `i % 2`, which will be `0` if `i` is even and `1` if `i` is odd.
The second, starting on line 16, takes the argument `i`. 
Here we're checking the actual value of `i`. 
On lines 17 and 23, we are checking if `i` lies within a range.
In C++, we can do this with the `lower ... higher` syntax.
Note this is explicitly `0 ... 3`, not `0...3`.
On line 28, we are using a `return` to exit not just the switch but also the `while` loop.
This is because running a `break` from within the `switch` would only break from the `switch` and not the outer `while` loop. This would output the following:

```
0 is even!
1 is between 0 and 3
1 is odd!
2 is between 0 and 3
2 is even!
3 is between 0 and 3
3 is odd!
4 is exactly 4
4 is even!
5 is between 5 and 7
5 is odd!
6 is between 5 and 7
6 is even!
7 is between 5 and 7
7 is odd!
8 greter than 7
```

Let's consider a more useful example. Let's say we have a device that we are controlling with C++. 
The device can have one of three states: on, off, or standby. 
We can define an `enum` to handle these three options.

```c++ linenums="1"
enum Status {On, Off, Standby};
```

An `enum` is very useful when considering a fixed number of possible options. 
The option to use a human-readable `enum` can also help with debugging by providing a human-readable status (e.g., `Status::Standby`) instead of an error code that might not make sense within the correct context (e.g., `2`).

Let's now define a function to get a random status. 
This will emulate a device that we want to interface with:

```c++ linenums="1" hl_lines="1 2 3"
Status get_status(){
    srand (time(NULL));
    int stat = rand() % 3 + 1;
    switch(stat){
        case 1:
            return Status::On;
        case 2:
            return Status::Off;
        default:
            return Status::Standby;
    }
}
```
On line 1, we are defining that this is a function (more on functions later) that returns a `Status` type (which we defined before as an `enum`).
On lines 2 and 3, we initialize a random number generator and get a random number between 1 and 3. 
We then use this random number to return a status.
When the random number is 1, we return `Status::On`.
When the random number is 2, we return `Status::Off`. 
The `default` case here is `Status::Standby`.

We can imagine that the `get_status` function is actually part of the API for some device.
Let's say it is a readout device; when the status is `On`, it is powered on. 
When the status is `Off`, either the device is off or it cannot be reached.
When the status is `Standby`, it is awaiting instructions.
Let's assume we send a power-on command with some function `activate_device`. For now, let's take:

```c++
void activate_device(){
    sleep(1);
}
```

In our workflow, it would be important to wait until the device has completely powered on and is in `Standby` mode before we send instructions. 
We could write something like:
```c++ linenums="1" hl_lines="3 5 6 8 10 17"
int main(){

    activate_device();

    Status stat;
    while (stat != Status::Standby)
    {        
        stat = get_status();

        switch (stat){
            case Status::On:
                cout << "Device is On" << endl;
                sleep(1);
                break;
            case Status::Off:
                cout << "Device is Off" << endl;
                activate_device();
                sleep(1);
                break;
            case Status::Standby:
                cout << "Device is in Standby" << endl;
                break;
        }

    }
}
```

On line 3, we send the power-on command to our device.
On line 5, we define a `Status` object called `stat`.
On line 6, we use a `while` loop to repeatedly check the status of the device.
On line 8, we retrieve the status of the device.
On line 10, we use a `switch` statement to match the `stat` to the possible values of that `enum`.
If the device is either `Status::On` or `Status::Off`, we sleep for 1 second and then restart the loop.
If the status is `Status::Off`, we also resend the power-on command with the `activate_device` function. 
Finally, if the status is `Status::Standby`, we can continue with our program.

Here is an example output from such a program:

```
Device is On
Device is Off
Device is Off
Device is On
Device is On
Device is Off
Device is On
Device is in Standby
```



## Storing Data


### Arrays

We can define arrays of a data type in C++ using the following format:
```c++ linenums="1"

    // Define an array of 6 integers
    int my_array[6] = {1, 2, 3, 4, 5, 6};

    // This will print the 3rd entry -> 3
    cout << "The 3rd entry in the array is: " << my_array[2] << endl;
```

If we do not know the size of an array at compile time, we may `dynamically` allocate memory for the array:
```c++  linenums="1"
// Where n is some integer unknown at compile time.
int *my_array = new int[n];

/* do stuff with code */

delete [] my_array;
```
On line we create a new array called `my_array` using the `new` keyword. When we do this we are dynamically allocating memory on the heap. The size of the region is going to be enough to hold `n` integers. The `int *my_array` syntax is important in C++. We have defined a "pointer" to an array of integers.  When we define a new array of values it is important to `delete` the data once we're finished with it. This is done on line 6. If we fail to do so, we will end up with a memory leak, causing our memory usage to rise over time.

!!! info "Aside on pointers"
    We may discuss pointers later, but essentially, we can think of them not as the actual array itself, but rather as signposts to where the array is stored.
    ```c++  linenums="1"
    int a = 42;
    int b = a;
    int *a_pointer = &a;

    // Access the value of the pointer
    cout << "The Value of a is: " << a << " or by pointer " << *a_pointer << endl;
    cout << "The address of a is: " << &a << " or by pointer " << a_pointer << endl;
    cout << "The Value of b is: " << b << " and its address is " << &b << endl;

    return 0;
    ```
    This will output:
    ```
    The Value of a is: 42 or by pointer 42
    The address of a is: 0x7ffee5f38334 or by pointer 0x7ffee5f38334
    The Value of b is: 42 and its address is 0x7ffee5f38330
    ```

    On line 1, we define the integer `a`. On line 2, we set `b` to be equal to `a`. On line 3, we create a pointer `a_pointer` and assign it to `&a`. Here, `&`` represents that we're passing a reference to `a` rather than the value of `a`. The reference can be thought of as the actual location in memory of `a`.

    From the output, we see that `a`, `b`, and `a_pointer` all return `42`. However, the address of `a` and `b` is different. While the values are equal, they are not the same. However, the address returned by `&a` and `a_pointer` is identical. This is because `a_pointer` is pointing to the spot in memory that `a` occupies.


When working with arrays we need to be careful when accessing elements of the array as C++ doesn't offer protection about going out of range:

```c++ linenums="1"

    // Define an array of 6 integers
    int my_array[6] = {1, 2, 3, 4, 5, 6};

    // This will print the 3rd entry -> 3
    cout << "The 3rd entry in the array is: " << my_array[2] << endl;
    cout << "The 7th entry in the array is: " << my_array[6] << endl;
```
The above example will execute, but we will be accessing whatever is in the memory at that location. This will be undefined behaviour!

### Vectors

Vectors offer a safer way to store data, and they can be defined as follows:
```c++ linenums="1"
// Create an empty vector of integers
vector<int> my_vector;
// Create a vector of length n
vector<int> my_vector_long(n);
// Create a vector of length n with a default value of 42
vector<float> my_vector_long(n, 42.0);
// Create a vector with known values
vector<double> my_known_vector{1.1, 2.3};
// Create 2D vectors (vectors of vectors)
vector<vector<float>> my_2d_vector;

```

Vectors provide safety and have a known length, which can be obtained using:
```c++ linenums="1"
unsigned int vec_size = my_vector.size();

// Get the last element of the vector
cout << "Last element: " << my_vector[vec_size - 1] << endl;
```

You can dynamically add values to the vector using `push_back`:
```c++ linenums="1"
// Define an empty vector
vector<int> my_vector;

// Add numbers 0-9 to our vector
for (int i = 0; i < 10; i++){
    my_vector.push_back(i);
}
// This will output 10
cout << "Length of vector " << my_vector.size() << endl;
```

You can also change the size of the vector with:
```C++ linenums="1"
vector<int> my_vector;

// Resize to have 10 elements
my_vector.resize(10);
// Resize to have 5 elements
my_vector.resize(5);

// Resize to have 20 elements and set the values to 0
my_vector.resize(20, 0);
```

Vectors provide a memory-efficient way to store arrays of data. When a `vector` is removed, either by deletion or leaving scope, the destructor of the vector's elements is called, freeing the memory so that you don't need to manage it.


## Functions

So far, we have used a single function, the main function. In C++, main is a special keyword that designates the entry point for our code. Let's take a closer look at the main function to understand the basics of how functions work in C++:
```c++ linenums="1"
int main(){
    return 0;
}
```
On line 1, we define a function called `main`. It's important to note that this function has a return value, which is an `int`. The code for the function is enclosed within curly brackets `{}`, defining the scope of the function. In the example above, the `main` function simply returns `0`.

We can also define functions that take arguments by specifying the argument types and providing them with local names within the function's scope:

```c++ linenums="1" hl_lines="2 7 22"
// Define a function that adds two vectors of integers together and returns the result
vector<int> add_two_vectors(vector<int> a, vector<int> b) {
    // Define a vector to hold the result, ensuring it has the same size as the input vectors
    vector<int> result(a.size());

    for (int i = 0; i < a.size(); i++) {
        result[i] = a[i] + b[i];
    }
    // Return the result
    return result;
}

...

int main() {
    vector<int> x, y;
    for (int i = 0; i < 10; i++) {
        x.push_back(i);
        y.push_back(2 * i);
    }

    vector<int> z = add_two_vectors(x, y);

    return 0;
}
```

In the example above, we define a function named `add_two_vectors` that takes two vectors of integers as arguments, adds the corresponding elements together, and returns the result as a new `vector`. This demonstrates how you can define and use functions in C++ to modularize your code and perform specific tasks.


In C++, unlike in Python, we can "overload" functions by defining multiple functions with the same name but accepting different argument types. For example, consider the following case:
```c++ linenums="1" hl_lines="2 7 19"
// Define a function that adds two vectors of integers together and returns the result
vector<int> add_two_vectors(vector<int> a, vector<int> b) {
    // Define a vector to hold the result, ensuring it has the same size as the input vectors
    vector<int> result(a.size());

    for (int i = 0; i < a.size(); i++) {
        result[i] = a[i] + b[i];
    }
    // Return the result
    return result;
}

// Define a function that adds two vectors of booleans together and returns the result
vector<bool> add_two_vectors(vector<bool> a, vector<bool> b) {
    // Define a vector to hold the result, ensuring it has the same size as the input vectors
    vector<bool> result(a.size());

    for (int i = 0; i < a.size(); i++) {
        result[i] = a[i] || b[i];
    }
    // Return the result
    return result;
}
```

In the above example, we have "overloaded" the `add_two_vectors` function to accept vectors of integers and vectors of booleans. The structure of the two functions is very similar, with the main difference occurring on line 23. In the second function, we replaced the addition operator `+` with the logical "OR" operator `||`. This demonstrates how you can create multiple functions with the same name but different behaviors based on the types of arguments they receive.

Knowing that logical '+' represents "OR" and "*" stands for "AND", we can rewrite the previous example using multiplication:

```c++ linenums="1" hl_lines="7 19"
// Define a function that multiplies two vectors of integers and returns the result
vector<int> multiply_two_vectors(vector<int> a, vector<int> b) {
    // Define a vector to hold the result, ensuring it has the same size as the input vectors
    vector<int> result(a.size());

    for (int i = 0; i < a.size(); i++) {
        result[i] = a[i] * b[i];
    }
    // Return the result
    return result;
}

// Define a function that multiplies two vectors of booleans and returns the result
vector<bool> multiply_two_vectors(vector<bool> a, vector<bool> b) {
    // Define a vector to hold the result, ensuring it has the same size as the input vectors
    vector<bool> result(a.size());

    for (int i = 0; i < a.size(); i++) {
        result[i] = a[i] && b[i];
    }
    // Return the result
    return result;
}
```
Here the `&&` operator represents the logical "and" operator. Overloading functions is super useful when you want to use common names for functions that perform similar operations on different data types.

We can also set default values in functions using the following:
```c++ linenums="1" hl_lines="1 14 16"
void print_message(bool hello = true){
    if (hello){
        cout << "Hello World" << endl;
    }
    else {
        cout << "Goodbye World" << endl;
    }
}

...

int main(){
    // Will print "Hello World"
    print_message();
    // Will print "Goodbye World"
    print_message(false);

    return 0;
}
```

On line 1, we define a function with a return type specified as `void`, indicating that the function doesn't return any value. When defining the function's parameters, we allow the bool parameter to have a default value of `true`. On line 14, when calling the function without passing any arguments, the default values are used. On line 16, we explicitly pass the value `false`, which overrides the default argument.


<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>