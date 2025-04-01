In this tutorial, I'll assume that you have some programming experience. I'll also assume that you use programming as a tool and that you don't necessarily have a background in computer science. Our focus will be more on the "hows" rather than the "whys," whenever possible.

By the end of this tutorial, you will have gained enough knowledge of Rust to begin developing high-performing code. I encourage you to work through the examples at your own pace, attempting to solve issues before reviewing the solutions. For your convenience, unanswered problems are available on [GitHub](https://github.com/steob92/rust-tutorial/tree/main), with the solutions provided in the "solutions" branch.

## What is Rust?

Rust stands out as a high-performance and memory-efficient programming language that emerged from the endeavors of Mozilla's research employees ([Rust, not Firefox, is Mozilla’s greatest industry contribution](https://www.techrepublic.com/article/Rust-not-firefox-is-mozillas-greatest-industry-contribution/)). 
Prioritizing performance and memory safety, Rust utilizes a robust type system and an innovative "ownership" model to guarantee memory safety and thread safety at compile time. 
This approach aims to address vulnerabilities arising from memory errors, with estimates from Microsoft suggesting that approximately 70% of code vulnerabilities stem from memory-related issues ([source](https://www.technologyreview.com/2023/02/14/1067869/Rust-worlds-fastest-growing-programming-language/)).

Rust's ability to produce fast, efficient, and resilient code has catapulted it to the top of the list as the [most admired language amongst developers](https://survey.stackoverflow.co/2023/). The community of Rust programmers affectionately refers to themselves as "Rustaceans," and the language's unofficial mascot, Ferris the crab:

<figure markdown>
  ![Ferris the Crab](../images/rustacean-flat-happy.png){ width="500" }
  <figcaption> Ferris the Crab (https://Rustacean.net). Ferris being a reference to ferrous, a compound that contains iron. </figcaption>
</figure>


### Rust Compared to Python

When comparing Rust to a language like Python, several key differences become apparent:

- **Performance**: Rust is renowned for its high performance, often being [comparable to languages like C or C++](https://arxiv.org/abs/2107.11912). Python, on the other hand, tends to be significantly slower than Rust, emphasizing ease of development over raw performance.

- **Type System**: Python is a dynamically typed language, meaning the interpreter infers variable types at runtime, allowing flexibility but increasing the potential for type-related errors. In contrast, Rust requires variables to have known types at compile time, enhancing safety and allowing for optimizations to be made by the compiler.

- **Compilation**: Rust is a compiled language, while Python is interpreted. Python code is executed by an interpreter, converting code to bytecode at runtime, resulting in slower performance. Rust, as a compiled language, produces machine code binaries before runtime, reducing overhead and enabling compiler optimizations for faster, more memory-efficient execution.

- **Memory Management**: Python employs a "garbage collector" to manage memory by periodically checking and freeing memory occupied by variables that go out of scope, impacting speed and memory efficiency. Rust utilizes an "ownership" memory model enforced by the "borrow checker" at compile time. Each variable in Rust has a single owner, and memory is automatically freed when the owner goes out of scope. This approach, without a costly garbage collector, contributes to Rust's fast runtime.

- **Thread Safety**: Python's Global Interpreter Lock (GIL) allows only one CPU-bound thread to execute at a time, ensuring safety across threads but causing a bottleneck for parallel code execution. In Rust, the ownership model, combined with allowing either numerous immutable references or a single mutable reference at a time, guarantees thread safety at compile time without the restrictions posed by a GIL.

- **Package Management**: Both Python and Rust use package management systems to handle external libraries or crates (in Rust). Rust utilizes the `cargo` package manager and `toml` files to manage project dependencies, while Python uses tools like `pip` and `requirements.txt` to manage packages.

Rust and Python employ different approaches to achieve their goals, with Rust focusing on performance, memory safety, and concurrency, whereas Python emphasizes ease of use and flexibility.



### Installing Rust

Comprehensive installation instructions for Rust can be accessed [here](https://www.Rust-lang.org/learn/get-started). The installation process involves utilizing `rustup`, a tool used for installing both the Rust compiler (`rustc`) and the package manager (`cargo`). These tools are compatible with Linux, macOS, and Windows (WSL).
```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

For alternative methods of installing Rust, refer to [this page](https://forge.Rust-lang.org/infra/other-installation-methods.html).

For this tutorial, we'll utilize the [official Rust Docker image](https://hub.docker.com/_/Rust) to compile and run code within a container. To pull the image, execute:


``` bash
docker pull Rust
```
Create an interactive Docker container using the following command:

```
docker run -it --rm -v $(pwd):/local_data -w /local_data Rust bash
```
Explanation:

- `run` executes the bash command in an interactive mode (`-it`) to provide an interactive Bash shell for work.
- `--rm` ensures the container is deleted after use.
- `-v $(pwd):/local_data` mounts the current directory on the local machine to `/local_data` in the container.
- `-w /local_data` sets the working directory to `/local_data` within the container.


(Free) Learning resources:

* ["The Book", the offical ](https://doc.Rust-lang.org/book/)
* ["Rustlings Course on GitHub"](https://github.com/Rust-lang/Rustlings/)
* ["Offical Website"](https://www.Rust-lang.org/)
* ["Rust Playground" a web coding enviroment for Rust](https://play.Rust-lang.org/?version=stable&mode=debug&edition=2021)
* ["Rust Standard Library Crate"](https://doc.Rust-lang.org/std/index.html)
* ["Command line apps in Rust"](https://Rust-cli.github.io/book/index.html)
* ["The Embedded Rust Book"](https://doc.Rust-lang.org/stable/embedded-book/)



## Basics of Rust

In this section we will cover the basics of Rust.

### Hello World

To create a new project in Rust, utilize the `cargo` command:
``` bash
cargo new hello
```
This will create a new directory called `hello`. 
```bash
-> ls -ah hello
.  ..  .git  .gitignore  Cargo.toml  src
```

When using `cargo new`, a new Rust project is initialized. Alongside creating the project structure, `cargo` automatically sets up a new Git repository for the package and adds a Rust-specific `.gitignore` file. 
The newly created project includes a `Cargo.toml` file, which serves as the manifest file for the project. 
This file contains details about the project, including external dependencies, package name, and versions used.
```bash
-> cat hello/Cargo.toml 
[package]
name = "hello"
version = "0.1.0"
edition = "2021"

# See more keys and their definitions at https://doc.Rust-lang.org/cargo/reference/manifest.html

[dependencies]
```
Cargo also sets up a `src` directory with a `main.rs` file containing an example program that will print "Hello, world": 
``` Rust title="hello.rs" linenums="1" 
fn main() {
    println!("Hello, world!");
}
```

In this example, the following points are illustrated:

- Functions in Rust are defined using the `fn` keyword.
- The `main` function designates the entry point of the code to the compiler.
- Code blocks are enclosed within `{}` to denote scopes.
- Rust includes macros (indicated by `!`, which will be covered later) like `println!` used to print the string `"Hello, world!"` to the screen.
- Statements in Rust are terminated with a `;` (exceptions for when to omit the `;` will be explained later).

This example can be compiled using `rustc`:
```
rustc src/main.rs -o main
```

to create the executable `main`.

Alternatively we can use `cargo build` to compile:
```
-> cargo build
   Compiling hello v0.1.0 (/local_data/hello)
    Finished dev [unoptimized + debuginfo] target(s) in 0.28s
```
Executing this command will compile an executable located at `target/debug/hello`. To run the executable, you can either call the executable directly or use the `cargo run` command. When using `cargo run`, if there are changes in the code or if the code hasn't been compiled previously, it automatically triggers the `cargo build` command before executing the program.

```
-> cargo run
    Finished dev [unoptimized + debuginfo] target(s) in 0.01s
     Running `target/debug/hello`
Hello, world!
```

The executable is typically found within a `debug` folder. By default, Rust generates debug information useful for code analysis and debugging. To create an optimized version for end-users, the `--release` flag can be utilized:
``` 
-> cargo build --release
   Compiling hello v0.1.0 (/local_data/hello)
    Finished release [optimized] target(s) in 0.25s
```

This will take longer to compile as `rustc` is optimizing the code.


### Types in Rust

In Rust, types must be known at compile time. You can explicitly specify the type of a variable using the syntax `let my_variable: type = value`, where the `type` is specified after the variable name using a `:`. The following example demonstrates explicit declaration of variable types on lines 3-6:

``` Rust title="types.rs" linenums="1" hl_lines="3-6 9-12 16-18"
fn main() {
    // Explicitly declaring the type of the variable
    let my_integer: i32 = 42;
    let my_float: f64 = 3.14;
    let my_character: char = 'A';
    let my_boolean: bool = true;

    // Rust can infer types in many cases, so explicit annotation is not always necessary
    let inferred_integer = 10;
    let inferred_float = 2.5;
    let inferred_character = 'B';
    let inferred_boolean = false;


    // Explicitly declaring the type of the variable within the passed value
    let my_integer_in_value = 17_i8;
    let my_float_in_value = 6.28_f32;
    let my_large_unsigned_32 = 1_000_000_u32;


    // Printing the values along with their types
    println!("Integer: {} (Type: i32)", my_integer);
    println!("Float: {} (Type: f64)", my_float);
    println!("Character: {} (Type: char)", my_character);
    println!("Boolean: {} (Type: bool)", my_boolean);

    println!("Inferred Integer: {} (Type: inferred)", inferred_integer);
    println!("Inferred Float: {} (Type: inferred)", inferred_float);
    println!("Inferred Character: {} (Type: inferred)", inferred_character);
    println!("Inferred Boolean: {} (Type: inferred)", inferred_boolean);


    println!("Integer: {} (Type: inferred from value)", my_integer_in_value);
    println!("Float: {} (Type: inferred from value)", my_float_in_value);
    println!("Unsigned: {} (Type: inferred from value)", my_large_unsigned_32);
}
```

The Rust compiler features type inference, enabling omission of the variable type, as it can deduce the type based on the assigned value. Internally, the compiler determines the variable's type during compilation based on the provided value. An example illustrating this behavior is demonstrated in lines 9-12 of `types.rs`.

Additionally, we can explicitly specify the variable type by adding `::<type>` after the assigned value. This method is showcased in lines 16-18 of `types.rs`.


In Rust, type conversion between different types can be achieved using keywords such as `into`, `try_into`, `from`, `try_from`, or `as`. Below are some examples:
``` Rust linenums="1"
fn main() {
    let integer_a: i32 = 40;
    let float_b:f32 = integer_a as f32;
    
    
    let integer_c: i32 = 3;
    // We're using "try into" here because we could have a negative integer
    let unsigned_d: u32 = integer_c.try_into().unwrap();

    let float_64_e: f64 = 6.5;
    // This wont work because going from f64->f32 loses percision and range
    // There are also some funky behaviour around inf
    // let float_32_f: f32 = f32::try_from(float_64_e).unwrap();
    let float_32_f: f32 = float_64_e as f32;

    let float_32_g:f32 = f32::from(3.13);
    let i8_h:i8 = i8::from(-3);
    let u32_i :u32 =  u32::try_from(8).unwrap();
}
```


### Ownership in Rust

Ownership and the borrow checker constitute the foundation of Rust's memory management. When dealing with ownership in Rust, it's essential to remember three fundamental rules:

* Every value in Rust has a designated owner.
* At any given time, there can only be a single owner for a value.
* When the owner goes out of scope, the associated value is automatically dropped.

Let's delve into an example to illustrate this concept:
```Rust title="Ownership Example" linenums="1"
fn main() {

    let mut x = String::from("Hello");
 
    let y = x;
    println!("{}", y);

    println!("{}", x);

}
```

In the provided code, a new variable `x` of type `String` is created. At line 5, a new variable `y` is assigned the value of `x`. Subsequently, attempts to print `x` and `y` on lines 6 and 8, respectively, would result in a compilation error:
```bash
error[E0382]: borrow of moved value: `x`
 --> src/main.rs:8:20
  |
3 |     let mut x = String::from("Hello");
  |         ----- move occurs because `x` has type `String`, which does not implement the `Copy` trait
4 |  
5 |     let y = x;
  |             - value moved here
...
8 |     println!("{}", x);
  |                    ^ value borrowed here after move
```

So what's happening? Well on line 5 we changed the ownership of the part of the memory that holds "Hello". The ownership of this has changed from `x` to `y`. Since we can only ever have one owner at a time, `x` cannot be printed. We could however run this example:
```Rust title="Ownership Example Corrected" linenums="1" hl_lines="7"
fn main() {

    let mut x = String::from("Hello");
 
    let y = x;
    println!("{}", y);
    x = y;
    println!("{}", x);

}
```
In the above example once we have finished using `y` we have passed ownership back to `x`. 

The fact that all value in Rust only ever has one owner guarentees that we can never acidently drop or delete a value that is still in use. This might seem very limiting and a heavy cost to pay for safety, but we can use "borrowing" to circumvent this issue. 
```Rust title="Ownership Example Corrected" linenums="1" hl_lines="5"
fn main() {

    let x = String::from("Hello");
 
    let y = &x;
    println!("{}", y);

    println!("{}", x);

}
```

In the above value we have "borrowed" the value of `x`. By borrowing the values instead of taking ownership, `x` maintains ownership over the value, allowing different parts of the code to access the value of the value.

When borrowing values Rust's "borrow checker" will keep track of all refeneces and make sure that we don't have dangling references or data races. Consider the following:
```Rust linenums="1" title="Mutable and immutable borrows" hl_lines="5 8"
fn main() {

    let mut x = String::from("Hello");
 
    let y = &x;
    println!("{}", y);

    x += ", world";
    println!("{}", x);
    println!("{}", y);
}
```
In the preceding example, an immutable reference to `x` is established in line 5. However, an attempt to modify `x` occurs in line 8, resulting in a compilation error:
``` bash
   Compiling tutorial v0.1.0 (/local_data)
error[E0502]: cannot borrow `x` as mutable because it is also borrowed as immutable
  --> src/main.rs:8:5
   |
5  |     let y = &x;
   |             -- immutable borrow occurs here
...
8  |     x += ", world";
   |     ^^^^^^^^^^^^^^ mutable borrow occurs here
9  |     println!("{}", x);
10 |     println!("{}", y);
   |                    - immutable borrow later used here

For more information about this error, try `rustc --explain E0502`.
``` 
What's happening in this code? In Rust, strings occupy a fixed memory space. 
When modifying a String, a new memory allocation is required since the memory size needed to store the string has changed. 
The `+=` operator, used to alter the value of `x`, takes a "mutable" reference to `x` and then assigns the modified value back to `x`. 
Essentially, the `+=` operator takes ownership of `x`'s value momentarily and then returns it to the variable `x`.

Rust enforces a rule allowing only one mutable reference or any number of immutable references at any given time. 
This constraint aligns with memory safety principles: preventing a scenario where one part of the code attempts to modify a value while another part tries to read it. 
Such a situation could lead to a race condition, causing the code's behavior to be undefined and reliant on the order of execution. 
While it might not appear problematic for sequential code like this, attempting read and write actions across different threads could result in significant issues.

So how can we work with mutable and immutable references? Consider the following example:
```Rust linenums="1" title="Mutable and immutable references" hl_lines="3 5 9 17-22 27-32 35-36"
fn main() {

    let mut x:i32 = 42;

    let y: &i32 = &x;
    
    println!("y = {}", y);

    let mut z: i32 = x;
    z += 1;

    println!("x = {}", x);
    println!("y = {}", y);
    println!("z = {}", z);
    

    {
        let a = y;
        let another = &x;
        println!("a = {}", a);
        println!("another = {}", another);
    }

    x += 1;
    println!("x = {}", x);

    {
        let b  = &mut x;
        *b +=  10;
        println!("b = {}", b);

    }

    println!("x = {}", x);
    let last = &mut x;
    *last -= 100;
    println!("last = {}", last);
}
```

In this code snippet, we perform several operations with mutable and immutable references to showcase Rust's ownership and borrowing principles.

- Line 3 initializes a mutable `i32` assigned to variable `x`.
- Line 5 creates an immutable reference `y` to the value of `x`.
- Line 9 assigns a new value to `x`. This operation works because we only have a single immutable reference, `y`. As `i32` can be copied, `z` receives a copy of the value of `x`, not the actual value.

In lines 17-22, a new scope is created. Here, we transfer ownership of reference `y` to `a` and establish a second immutable reference, `another`, to `x`. Remembering the three ownership rules ("When the owner goes out of scope, the value will be dropped"), when the scope ends at line 22, the values of `a` and `another` are dropped. Since `a` took ownership of `y`, there are now 0 immutable references. Any attempt to access `y` would result in an error.

In lines 27-32, a new scope introduces a mutable reference `b` to `x`. At this point, there are 0 immutable references and 1 mutable reference. Modification of the value behind `x` is possible by "dereferencing" `b`, illustrated in line 29 (`*b +=  10;`), which adds 10 to the actual value `b` is referencing. When this scope ends at line 32, `b` is dropped, leaving 0 immutable references and 0 mutable references.

Finally, lines 35 and 36 create a mutable reference to `x` and modify its value.

Throughout this example, `x` remains the sole owner of the value, never relinquishing ownership. Borrowing the value (`y`, `a`, `another`, `b`, `last`) occurs at multiple stages, but `x` retains ownership. Although `y` initially held an immutable reference to `x`, preventing `last` from taking a mutable reference, ownership of the reference shifted from `y` to `a`. Upon `a`'s scope exit, the immutable reference was dropped. Throughout this code, multiple immutable references or a single mutable reference were consistently present.

Understanding ownership and borrowing is the most challenging concept in Rust. Proficiency in these concepts is crucial for mastering Rust.


## Functional Programming

In Rust, functional programming can be achieved through two primary methods: using functions defined with the `fn` keyword or leveraging closures.

Functions, declared using the `fn` keyword, represent a fundamental approach to functional programming in Rust. They encapsulate blocks of code that can be called multiple times with different arguments.

Closures, on the other hand, are more powerful and flexible. They are similar to functions but can capture variables from their surrounding environment. Closures allow for defining anonymous functions on the fly, making them highly adaptable for tasks requiring flexibility in behavior and data encapsulation.

Both functions and closures play integral roles in enabling functional programming paradigms within Rust, offering different levels of flexibility and usability in various scenarios.

### Functions

Functions in Rust are defined using the following syntax:
```Rust linenums="1" title="Examples of functions" hl_lines="1 5 9 13"
fn add_numbers(a: i32, b: i32) -> i32{
    return a + b;
}

fn multiply_numbers(a :i32, b :i32) -> i32{
    a * b
}

fn print_numbers(a :i32, b :i32) {
    println!("{} + {} = {}", a,b, a+b);
}

fn print_numbers_multiply(a :i32, b :i32) -> () {
    println!("{} * {} = {}", a,b, a*b);
}

fn main(){
    let x = 3;
    let y = 4;

    let sum = add_numbers(x,y);
    print_numbers(x,y);
    let product = multiply_numbers(x,y);
    print_numbers_multiply(x,y);

    println!("sum = {}, product = {}", sum, product);

}
```

In the example above, three functions are defined using the `fn` keyword to indicate their creation. When defining functions, specifying the data types of passed arguments is necessary, as demonstrated here by using `i32` types in all cases. Additionally, if a function returns a value, explicit declaration of the return type is required. Lines 1 and 5 explicitly define the return type as `i32`, denoted by `-> T`, where `T` represents the data type.

Lines 9 and 13 introduce functions that do not return any value. When a function doesn't return anything, the `->` can be omitted. Alternatively, it's possible to explicitly state the absence of a return value using `-> ()`.

The functions `add_numbers` and `multiply_numbers` both return an `i32`. However, only `add_numbers` uses a `return` keyword. In Rust, if a statement isn't followed by a `;`, it's assumed to be the return value. In the case of `multiply_numbers`, the absence of `;` specifies that the function should return `a * b`.

It's important to note that in all these functions, ownership of `a` and `b` is taken within the functions. Consequently, when the function's scope ends, both `a` and `b` are dropped. While this behavior might not be problematic for `i32` due to its copy trait, allowing passing a copy of the value rather than the value itself, it's a crucial consideration for other types where ownership might cause different behavior.
Consider the following example:

```Rust linenums="1" title="Problems with borrowing" 
fn print_string( msg : String) -> (){
    println!("{}", msg);
}


fn main(){
    let my_string = String::from("Save Ferris!");
    print_string(my_string);
}
```

This will give the following error:
``` bash
error[E0382]: borrow of moved value: `my_string`
 --> src/main.rs:9:20
  |
7 |     let my_string = String::from("Save Ferris!");
  |         --------- move occurs because `my_string` has type `String`, which does not implement the `Copy` trait
8 |     print_string(my_string);
  |                  --------- value moved here
9 |     println!("{}", my_string);
  |                    ^^^^^^^^^ value borrowed here after move
  |
```
Remember that strings have variable lengths, making direct copying non-trivial. Therefore, when `print_string` receives `my_string`, it assumes ownership. To address this, we have two solutions: either use the `clone` method when passing `my_string` to `print_string`, or modify `print_string` to borrow the string by taking a reference instead. The corrected code would appear as follows:
```Rust linenums="1" title="Examples of functions with borrowing"
fn print_string( msg : String) -> (){
    println!("{}", msg);
}


fn print_string_borrow( msg : &String) -> (){
    println!("{}", msg);
}


fn main(){
    let my_string = String::from("Save Ferris!");
    print_string(my_string.clone());
    print_string_borrow(&my_string);
    println!("{}", my_string);
}
```

Functions can also return tuples. Consider the following:
```Rust linenums="1" title="Example of function returning a tuple" hl_lines="1 7 9 11"
fn get_powers( a: i32 ) -> (i32, f32){
    (a.pow(2), (a as f32).powf(0.33))
}

fn main(){
    let x :i32 = 8;
    let tup = get_powers(x);
    // Deconstruct tuple
    let (y, z) : (i32, f32) = get_powers(x);

    println!("{}, {}", tup.0, tup.1 );
    println!("{}, {}", y, z );
}
```

In the example above, a tuple of type `(i32, f32)` is returned. Line 7 stores the tuple as a variable, while on line 9, explicit deconstruction of the tuple occurs, assigning its elements to variables `y` and `z`. Accessing elements of the tuple can be achieved using `tup.n` to retrieve the nth element.


### Closures

Closures in Rust bear similarities to lambda functions found in other programming languages. They offer a concise means to create short blocks of functionality within code. Closures, like functions, can capture and manipulate variables from their enclosing scope. They are defined using the `|argument| { body }` syntax, where `argument` represents parameters and `body` signifies the functionality of the closure.

An example of a closure definition:

```Rust linenums="1" title="Examples of Closures" hl_lines="4 6-8"
fn main(){
    let pi  = 3.14_f32;

    let area = |x| pi * x*x;
    
    let print_area = |x| {
        println!("Area of circle with radius {} is {}", {x}, area(x));
    };

    println!("The area is: {}", area(2.));
    print_area(1.5);
}
```

In lines 4 and 6, two closures are defined. The `area` closure accepts a variable `x` and computes the area of a circle with radius `x`. This closure borrows the value of `pi` for the duration of its scope. On the other hand, the `print_area` closure accepts a variable `x`, prints a statement, and then passes a copy of `x` to the `area` closure.



## Flow Control

### If statements

Rust's `if` statements follow the subsequent syntax:

```Rust linenums="1" title="if statements"  hl_lines="3 5 7"
let a :i32 = 4;

if a > 3{
    println!("a is greater than 3");
} else if a < 3{
    println!("a is less than 3");
} else{
    println!("a is equal to 3");
}
```

Note that an `if` block must start with an `if` statement and may have only one `if` branch and at most one `else` branch. However, multiple `else if` branches can be included as needed.

`if` statements are also capable of assigning variables or returning values. Let's consider the following example:
```Rust linenums="1" title="returning if statements"  hl_lines="3 4 6 8 9"
let a :i32 = 4;

let my_string :String = if a > 3{
    "a is greater than 3".to_string()
} else if a < 3{
    "a is less than 3".to_string()
} else{
    "a is equal to 3".to_string()
};
```
Line 2 defines an immutable string `my_string`, assigned the value from this `if` block. In lines 4, 6, and 8, the absence of `;` at the end of these lines allows them to return the `String` type. Finally, line 9 concludes the assignment by adding a `;` at the end of the final block.


### Match

`match` statements in Rust are akin to `switch` statements found in other programming languages. They enable pattern matching on variables, allowing for concise and comprehensive conditional branching.

Matching involves specifying the pattern to match against, which can either be a variable or a condition evaluation (e.g., `x > 10`). It commences with the keyword `match` and encloses different options within a set of `{}`. For each pattern, code branches to run are assigned using the `=>` syntax. 


```Rust linenums="1" title="match statements" hl_lines="5 6 9 12 15 20-27"
fn main(){

    let a :i32 = 4;

    match a {
        0..=3 => {
            println!("a is less than 3");
        },
        4..=10 => {
            println!("a is greater than 3");
        },
        3 => {
            println!("a is 3");
        },
        _ => {
            println!("a is > 10");
        },
    }

    let b = match a {
        0 => "0",
        1 => "alpha",
        2 => "2",
        3 => "delta",
        4 => "for",
        _ => "Something else",
    };

    println!("b is {}", b);
}
```


In lines 6 and 9, the code searches for values of `x` within the ranges 0-3 and 4-10, respectively. On line 12, it checks if `a` equals 3. Finally, on line 15, the default case is defined using `_`. Each branch in this `match` statement executes a block of code enclosed within its scope.

In the example from line 20-27 we are returning a `str` based on the pattern found. 

### Loops

Loops in Rust are straightforward and flexible. The `loop` keyword initiates an infinite loop, allowing code to execute repeatedly within a defined scope until explicitly interrupted by a `break` statement.

For instance:
```Rust title="loop example" linenums="1" hl_lines="4 7 9"
fn main(){
    let mut i = 0;

    loop {
        i+=1;
        if i == 3{
            continue;
        } else if i > 10{
            break;
        } else{
            println!("i = {}", i);
        }
    }
}
```

Lines 4-12 constitute the content wrapped within the `loop` block, as indicated on line 4. At line 7, a `continue` statement is employed to skip the iteration where `i` equals 3. Moreover, line 9 utilizes a `break` statement to exit the loop when the condition `i > 10` is met.

In Rust, it is possible to assign labels to loops to facilitate `continue` or `break` operations targeting a specific loop. This is achieved using the `'name: loop {}` syntax:
```Rust linenums="1" hl_lines="4 6 9 11"
fn main(){
    let mut i = 0;

    'astra : loop {
        let mut j = 0;

        'kafka : loop{
            if i > 10{
                break 'astra;
            } else if j > 3{
                break 'kafka;
            } else{
                println!("i,j = {},{}", i,j);
            }
            j+=1;
        }
        i+=1;
    }
}
```
In the provided example, we establish a parent loop named `'astra`, encompassing the scope from line 4 to line 18. Within `'astra`, we define a nested loop named `'kafka`, spanning lines 7 to 16. 

At line 8, a `break` statement exits the `'astra` loop if `i > 10`. Furthermore, line 11 employs a `break` statement to exit the `'kafka` loop if `j > 3`. 

The output of this code will be:
```
i,j = 0,0
i,j = 0,1
i,j = 0,2
i,j = 0,3
i,j = 1,0
...
i,j = 10,2
i,j = 10,3
```

### For Loops

For loops in Rust operate on any data that conforms to an iterator. This includes constructs such as `for element in list` or `for i in a range`. The syntax used for these loops is as follows:
```Rust linenums="1" hl_lines="4"
fn main(){
    let n:i32 = 10;

    for i in 0..n{
        println!("i = {}", i);
    }
}
```
In this context, we define a range `0..n`, representing the inclusive range from 0 to 9 (Alternatively, we could use `0..=9`).

When dealing with an array or vector of items, we can iterate over them as follows:
```Rust linenums="1" hl_lines="2 3"
fn main(){
    let my_arr: [f32;5] = [1.,2.,3.,43., 3.14];
    for a in my_arr{
        println!("{}",a);
    }
    println!("{:?}", my_arr);
}
```

In the above example, `a` stores a copy of the values from `my_arr` rather than a reference to those values. Modifying a will not alter `my_arr`. However, the behavior slightly differs when working with vectors.

```Rust linenums="1" hl_lines="2 3 7"
fn main(){
    let my_arr: Vec<f32> = vec![1.,2.,3.,43., 3.14];
    for a in my_arr{
        println!("{}",a);
    }

    println!("{:?}", my_arr);
}
```

The above example will return an error on line 7.
```bash

   --> src/main.rs:7:22
    |
2   |     let my_arr: Vec<f32> = vec![1.,2.,3.,43., 3.14];
    |         ------ move occurs because `my_arr` has type `Vec<f32>`, which does not implement the `Copy` trait
3   |     for a in my_arr{
    |              ------ `my_arr` moved due to this implicit call to `.into_iter()`
...
7   |     println!("{:?}", my_arr);
    |                      ^^^^^^ value borrowed here after move
    |
```

The error indicates that `Vec<f32>` doesn't implement the `Copy` trait. Consequently, when attempting to iterate over its values, Rust borrows the values rather than making copies. As a result, the ownership of these values is temporarily transferred into the for loop's scope at line 5. However, as the loop ends, these borrowed values are automatically dropped, as their ownership wasn't transferred back outside the loop.

Looking further at the compile output we see:
```bash
help: consider iterating over a slice of the `Vec<f32>`'s content to avoid moving into the `for` loop
    |
3   |     for a in &my_arr{
    |              +

For more information about this error, try `rustc --explain E0382`.
```
Here we see some of the awesome features of the Rust compile. It is smart enough to understand what we are trying to do and suggest a fix to the code. The fixed code would look like:

```Rust title="vector for loop" linenums="1" hl_lines="3"
fn main(){
    let my_arr: Vec<f32> = vec![1.,2.,3.,43., 3.14];
    for a in &my_arr{
        println!("{}",a);
    }

    println!("{:?}", my_arr);
}
```
At line 3, we're iterating over a reference to a slice of the vector. In this instance, the vector slice represents the entire range of the vector.


We can iterate over tuples to access and combine their values:
```Rust title="Asigning Values in a Loop" linenums="1" hl_lines="6"
fn main(){
    let x: Vec<f32> = vec![1.,2.,3.,43., 3.14];
    let y: Vec<f32> = vec![2.,0.1,5.3,0.001, 3.14];
    let mut z: Vec<f32> = vec![0.0_f32; 5];

    for ((a, b), i) in x.iter().zip(&y).zip(0..x.len()){
        println!("{},{}",a, b);
        z[i] = a + b;
    }

    println!("{:?}", z);
}
```

In the provided example, there are three vectors: `x`, `y`, and `z`, where `z` is a mutable vector.

At line 6, `iter` is utilized to obtain an iterable reference to `x`. Subsequently, it is `zip`ped with a reference to `y`, invoking the `into_iter` method for `y` (similar to the vector for loop example). This action results in a `tuple` of type `(&f32, &f32)`. Additionally, another `zip` operation is performed with the range `0..x.len()`, effectively creating a loop over a `tuple` of `((&f32, &f32), usize)`.

Within this loop, values are assigned to `z`.


!!! info "Aside on `iter` vs `into_iter`"
    In the "vector for loop" example, we employed the `for a in my_arr` syntax, which implicitly calls the `into_iter` method. The `into_iter` method, being a generic method, returns either a copy, a reference, or the value itself. On the other hand, the `iter` method explicitly returns a reference.

    If distinguishing between the two seems perplexing, consider `into_iter` as moving the value "into" the scope. If ownership needs to be maintained, it's advisable to use `iter`. Conversely, if the value can be consumed by the scope, `into_iter` is preferable.

    For a more detailed explanation, refer to [this Stack Overflow question](https://stackoverflow.com/questions/34733811/what-is-the-difference-between-iter-and-into-iter).

    

### Looping the Rust way

In the "Assigning Values in a Loop" section, we explored how to derive values from two vectors to assign to a third vector. However, this approach isn't considered very idiomatic in Rust. A more idiomatic way to achieve this would be:

```Rust title="Idomatic Rust For Loop" linenums="1" hl_lines="5"
fn main(){
    let x: Vec<f32> = vec![1.,2.,3.,43., 3.14];
    let y: Vec<f32> = vec![2.,0.1,5.3,0.001, 3.14];

    let z  = x.iter().zip(&y).map(|(a,b)| a + b).collect::<Vec<f32>>();
    println!("{:?}", z);
}
```

In this example, we condense the entire loop into a single line of code. Starting with `x.iter()`, we iterate over references to the values within `x`. Using the `zip` function with a reference to `y` facilitates the iteration over a tuple of type `(&f32, &f32)`.

Each tuple undergoes processing within a closure passed to the `map` method. This closure deconstructs the tuple into two values and adds them together. The `collect()` method accumulates the values returned by the closure used in the `map` method.

The ["Turbofish"](https://techblog.tonsser.com/posts/what-is-rusts-turbofish) syntax, `collect::<type>()`, informs `collect` about the desired return type. In this instance, using `collect::<Vec<f32>>()`, we obtain a `Vec<f32>`.


Using a reduction, as shown in the 'Idiomatic Rust For Loop' example, is a powerful tool. For instance, suppose we aim to extract all even values from a vector, we could employ:
```Rust linenums="1" hl_lines="2 4-7 10-12"
fn main() {
    let values = 0..100;

    let even_squared = values.clone()
        .filter(|x| x % 2 == 0)
        .map(|x| x * x)
        .collect::<Vec<i32>>();


    let odd_sum = values.clone()
        .filter(|x| x % 2 == 1)
        .sum::<i32>();

        println!("{:?}", even_squared);
        println!("Sum of the odd values = {}", odd_sum);
}
```

In the given code, `values` is a range from 0 to 99 inclusive, represented as a collection of integers (`i32`). The operations on this range illustrate various methods provided by Rust's Iterator trait.

Starting from line 4, `even_squared` is created by cloning the `values` range. The `clone` method is used here to avoid consuming the original range, enabling separate iteration over the original range (`values`) and the cloned range. The `filter` method is then applied to this cloned range, utilizing a closure (`|x| x % 2 == 0`) to test each element for evenness by performing a modulo operation and checking if the remainder is zero. Elements satisfying this condition are retained, while those failing the test are discarded. The subsequent `map` method takes the retained even numbers, squares each value by multiplying it by itself (`x * x`), and produces a transformed iterator. Finally, the `collect` method is used to gather the squared even numbers into a `Vec<i32>`.

The `filter` method implicitly calls `into_iter` on the cloned `values` range, which temporarily takes ownership of the elements within the scope of the filter operation. After the `collect` method consumes the iterator, the clone of the `values` range is no longer needed and gets dropped, releasing its resources.

Next, between lines 10 and 12, `odd_sum` is calculated using a similar approach. Here, the `filter` method is again used on a cloned range of `values`, but this time with a closure (`|x| x % 2 == 1`) that filters for odd numbers. The `sum` method is applied to this filtered iterator to compute the sum of the odd numbers present in the range.

The code concludes by displaying the vector containing squared even numbers (`even_squared`) and printing the sum of the odd numbers (`odd_sum`).

## Object Orientated Programming

In contrast to languages like Python and C++, Rust diverges from class-based [inheritance](https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming)). 
It emphasizes struct composition and trait-based [polymorphism](https://en.wikipedia.org/wiki/Polymorphism_(computer_science)). 
Rather than relying on class inheritance, Rust promotes struct composition, allowing structs to contain instances of other structs or types. 
Traits, serving as a form of polymorphism, define sets of methods that types can implement, offering shared behaviors across different types without a single inheritance hierarchy. 
This trait-based approach fosters modularity and flexibility while ensuring safety and performance.

### Structs in Rust

Structs in Rust form the foundation of object-oriented programming (OOP). They can be seen as collections of variables that serve a related purpose or represent a specific context. 

Consider the example below:

```Rust title="Example of a Struct" linenums="1"
struct Point3D {
    x: f32,
    y: f32,
    z: f32,
    coord_system: String,
}
```

We've created a `struct` named `Point3D`, representing a point in 3D space. 
The `struct` is defined by encapsulating member data within curly brackets `{}` after naming it. 
Within this `struct`, we've defined fields such as `x`, `y`, and `z`, each having the data type `f32`, representing the coordinates in the x, y, and z axes, respectively. 
Additionally, there's a field named `coord_system` of type `String`, serving to describe the coordinate system. 
In Rust, it's common practice to separate each field with a `,` and a new line for readability. 
The presence of a trailing `,` after the last field doesn't cause a compile-time error and is often used to facilitate future struct modifications.

Methods can be implemented for a `struct` in Rust, functioning as functions that the `struct` itself can utilize. These methods can modify the `struct`, perform actions based on the field data, and more. The `impl` keyword is used to define these methods:

```Rust title="Example of implementing structs" linenums="1" hl_lines="1 4 14 20 24"
impl Point3D {
    
    // Return a new Point3D
    fn new() -> Point3D{
        Point3D{
            x: 0.0_f32,
            y: 0.0_f32,
            z: 0.0_f32,
            coord_system: "cartesian",
        }
    }

    // Get the magnitude of the Point3D
    fn get_magnitude(self :&Self) -> f32{
        (self.x.powi(2) + self.y.powi(2) + self.z.powi(2))
        .sqrt()  
    }

    // Add a constant value to the Point3D
    fn add_constant(self: &mut Self, c : &f32) -> (){
        self.x += c / 3.0_f32.sqrt();
        self.y += c / 3.0_f32.sqrt();
        self.z += c / 3.0_f32.sqrt();
    }
}
```

In the code example above, we've implemented three methods for the `Point3D` struct.

- The `new` function on line 3 creates and returns a new `Point3D` with default values at the origin (0, 0, 0). To use it: `let mut my_point = Point3D::new();`

- Line 14 contains the `get_magnitude` method, which accesses the struct's data without modifying it. It takes a non-mutable reference to itself (`&Self`) and returns a `f32`. To call it: `my_point.get_magnitude()`.

- The `add_constant` method, defined on line 20, modifies the `Point3D`'s data using a given value. It requires a mutable reference to itself (`&mut Self`) and takes a non-mutable reference to the constant (`&f32`). Usage example: `my_point.add_constant(&3.14);`. By taking a reference to the constant, it prevents ownership issues and avoids unintentional dropping of `c` after line 24.



### Traits

Traits in Rust provide a means to define common interfaces that can be implemented by different structs. They enable struct types to share behavior or functionality through shared methods.

For instance, let's consider the following struct:

```Rust title="Point2D" linenums="1"
struct Point2D{
    x: f32,
    y: f32,
    coord_system: String,
}
```

The `Point2D` struct shares similarities with `Point3D`. It would be beneficial if these structs had some common methods. To achieve this, we can define a `trait` that provides a shared interface for both structs. This approach allows for greater code flexibility and consistency. Let's explore this concept:

```Rust title="Trait Example" linenums="1"
trait PointLike{
    fn get_magnitude(self: &Self) -> f32;
    fn add(self: &mut Self, c : &f32) -> ();    
}
```

The `PointLike` trait defines a common interface for types that exhibit point-like behavior. For a type to be considered `PointLike`, it must implement two functions:

- `get_magnitude`: This method calculates the magnitude of the point and returns a `f32`.
- `add`: Accepts a mutable reference to itself, along with a reference to a `f32`, and does not return any value.

Notably, the `Point3D` struct possesses a method named `get_magnitude`, aligning with the trait's requirements. However, it lacks a function named `add`, although it has a similar method called `add_constant`. To conform `Point3D` to the `PointLike` trait, we can provide an implementation that satisfies the trait's functions:

```Rust title="Implementing Traits" linenums="1"
struct Point3D {
    x: f32,
    y: f32,
    z: f32,
    coord_system: String,
}


trait PointLike{
    fn get_magnitude(self: &Self) -> f32;
    fn add(self: &mut Self, c : &f32) -> ();    
}

impl Point3D {
    
    // Return a new Point3D
    fn new() -> Point3D{
        Point3D{
            x: 0.0_f32,
            y: 0.0_f32,
            z: 0.0_f32,
            coord_system: "cartesian",
        }
    }

    // Get the magnitude of the Point3D
    fn get_magnitude(self :&Self) -> f32{
        (self.x.powi(2) + self.y.powi(2) + self.z.powi(2))
        .sqrt()  
    }

    // Add a constant value to the Point3D
    fn add_constant(self: &mut Self, c : &f32) -> (){
        self.x += c / 3.0_f32.sqrt();
        self.y += c / 3.0_f32.sqrt();
        self.z += c / 3.0_f32.sqrt();
    }
}

impl PointLike for Point3D{
    fn get_magnitude(self: &Self) -> f32{
        self.get_magnitude()
    }

    fn add(self: &mut Self, c : &f32) -> (){
        self.add_constant(c)
    }    
}
```
Above, we've implemented the `PointLike` trait for the `Point3D` struct, utilizing the methods we had previously defined. Extending this trait implementation to `Point2D` would involve providing similar implementations for the required trait methods.

```Rust  linenums="1"
struct Point2D{
    x: f32,
    y: f32,
    coord_system: String,
}

impl Point2D{
    fn new()->Point2D{
        Point2D{
            x: 0.0_f32,
            y: 0.0_f32,
            coord_system: "cartesian",
        }
    }
}

impl PointLike for Point2D{
    fn get_magnitude(self: &Self) -> f32{
        (self.x.powi(2) + self.y.powi(2)).sqrt()
    }

    fn add(self: &mut Self, c : &f32) -> (){
        self.x += c /2.0_f32.sqrt();
        self.y += c /2.0_f32.sqrt();
    }    
}
```

In the given example, the trait implementation for `Point2D` directly utilizes existing methods. When implementing traits, we have the flexibility to use pre-existing methods or define new ones. This versatility allows us to employ these implementations within our code as demonstrated.
```Rust title="Using traits" linenums="1"
fn main(){

    let mut my_3d = Point3D::new();
    let mut my_2d = Point2D::new();

    my_3d.add(&4.5);
    my_2d.add(&5.0);
    

    println!("Magnitude of 3D {}", my_3d.get_magnitude());
    println!("Magnitude of 2D {}", my_2d.get_magnitude());
}
```


### Generics

Generic types in Rust bear resemblance to C++ templates. They enable us to write versatile code that isn't tied to specific data types. This allows for more reusable and adaptable code. Consider the following illustration:

```Rust title="Generic Types" linenums="1"
Point2D<T>{
    x:T,
    y:T,
}
```

Here we have defined a generic `Point2D` struct that represents a 2D point in space. This struct is designed to work with any data type, as it utilizes the placeholder type `T` for both the `x` and `y` coordinates. Using this placeholder type allows the struct to remain agnostic to the specific data type used for its coordinates.

The versatility of this generic struct becomes apparent when implementing methods or functionalities that can work universally across various data types.

```Rust linenums="1" 
struct Point2D<T>{
    x:T,
    y:T,
}

impl <T> Point2D<T>{
    fn get_x(self : &Self) -> &T{
        &self.x
    }

    fn get_y(self : &Self) -> &T{
        &self.y
    }
}
```

In the above we have implemented two functions assuming a type `T`. Each return references of type `T`. If we wanted to use these we could run:
``` Rust linenums="1" hl_lines="2"
fn main(){
    let my_point :Point2D<f32> = Point2D{x:0.1, y:4.3};
    println!("x = : {} ", my_point.get_x());
    println!("y = : {} ", my_point.get_y());
}
``` 
On line two, we are explicitly specifying the data type as `f32`.

We can combine traits and generics to enable custom data types that possess specific traits. Consider the example below:
```Rust linenums="1"
struct PlanetarySystem <T>{
    planet_location: Vec<T>,
    planet_name: Vec<String>,
}


impl <T: PointLike> PlanetarySystem<T> {
    fn  print_distance_from_star(self : &Self) -> (){
        for i in 0..self.planet_location.len(){
            println!(
                    "Distance from {} to it's star: {} AU",
                    self.planet_name[i], 
                    self.planet_location[i].get_magnitude()
                )
        }
    }
}
```

Here, we've defined a struct called `PlanetarySystem` that takes a generic type implementing the `PointLike` trait. As the `PointLike` trait includes the `get_magnitude` method, this code is applicable to any generic type adhering to the `PointLike` trait. This flexibility allows us to use the code as demonstrated below:


``` Rust
fn main(){

    let mut solar_system: PlanetarySystem<Point3D> = PlanetarySystem{
        planet_location: vec![
            Point3D::new(), 
            Point3D::new(), 
            Point3D::new()
        ],
        planet_name: vec![
            "Mercury".to_string(), 
            "Venus".to_string(), 
            "Earth".to_string()
        ],
    };

    solar_system.planet_location[0].add(&0.39);
    solar_system.planet_location[1].add(&0.72);
    solar_system.planet_location[2].add(&1.);
    solar_system.print_distance_from_star();


    let mut trappst_system: PlanetarySystem<Point2D> = PlanetarySystem{
        planet_location: vec![Point2D::new(), Point2D::new(), Point2D::new()],
        planet_name: vec![ "TRAPPIST-1b".to_string(), "TRAPPIST-1c".to_string(), "TRAPPIST-1e".to_string()],
        
    };

    trappst_system.planet_location[0].add(&0.01154);
    trappst_system.planet_location[1].add(&0.01580);
    trappst_system.planet_location[2].add(&0.029);
    trappst_system.print_distance_from_star();
}
```

Here, we are defining `solar_system` as a `PlanetarySystem` that utilizes a `Point3D` data type. Subsequently, we invoke the `print_distance_from_star` method, leveraging the fact that `Point3D` conforms to `PointLike` and therefore possesses the `get_magnitude` method.

In the context of our `PlanetarySystem`, the magnitude represents the distance between the planet and the origin, which we designate as the star's location. Running this code yields the following output:

```
Distance from Mercury to it's star: 0.39 AU
Distance from Venus to it's star: 0.72 AU
Distance from Earth to it's star: 0.99999994 AU
Distance from TRAPPIST-1b to it's star: 0.011540001 AU
Distance from TRAPPIST-1c to it's star: 0.0158 AU
Distance from TRAPPIST-1e to it's star: 0.029 AU
```

In this example, the `PlanetarySystem` struct doesn't differentiate between using `Point3D` or `Point2D`.

<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>