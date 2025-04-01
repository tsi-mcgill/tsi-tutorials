
## What is Containerization?

Containerization is a practice in software development in which a single application, or group of applications, is collected into a bundle which includes the application executable and all the libraries and dependencies required to run that application. With this information, the application can be run on any resource that uses the underlying containerization software installed.

Containerization is made possible due to "namespaces." In Linux, a namespace defines the boundaries of a process' "awareness" of what else is running around it. This essentially means that a process can "see" and interact with everything accessible within its own namespace, but not necessarily what is in other namespaces. With this in mind, we can limit what is accessible from a namespace. For example, we might limit the resources available (RAM, CPU) to a namespace or limit the file access of a namespace. When a process runs on a system, we can "containerize" the process by restricting what the process has access to. This allows the process to be run in isolation from the rest of the system. As far as the containerized process knows, it is in an operating system by itself with no other processes running (other than child processes!).

There are many types of containerization software (e.g. [Docker](https://www.docker.com/), [Podman](https://podman.io/) and [Apptainer](https://apptainer.org/)), but at their base level, they behave similarly. For simplicity, consider a container to be made up of two things:

1. A file system snapshot. This is a snapshot of the files in a system, including required libraries, executables, input data, etc. Anything that might be required for an application to run.
2. A start command. This could be the command required to start an application (e.g. an analysis pipeline, a website, a Python interpreter). The file system snapshot contains everything needed to execute the start command.

Here we rely on the fact that Linux systems are very similar, so much so that we can use a common Linux kernel to run two different operating systems. Consider OS 1 and OS 2. OS 1 is the "host" system, that is the system on which we will be running the container. OS 2 is going to be an image of a different operating system that we are going to run as a container on OS 1. The image for OS 2 contains the specific files needed (file system snapshot) to run the applications of interest. When we want to create a container, we essentially create a new namespace for the container, copy the files from OS 2 into the file system accessible to the container, and then run commands within the container. From within the namespace of the container, it would appear that we are running OS 2 despite using the Linux kernel of OS 1 to actually execute the code.

It's worth noting that while containers share the kernel, they don't necessarily emulate an entire operating system. They typically share the kernel and some system resources but maintain separate user spaces.

We can start to see some of the benefits of using a container emerge:

1. **Dependencies only need to be solved once!** We only need to determine the dependencies once when we create the image. The image can then be used on **any host system** (e.g., OS 1) which has the appropriate containerization software (Apptainer, Docker, Podman, etc.). Furthermore, I could give this image to anyone else who needs to run the same software.

2. **Old Difficult Dependencies:** When using older software, it is often difficult to get the dependencies to work on a modern system. For example, if we have old software designed to run on Ubuntu 12.04 and we want to run it on Ubuntu 22.04, we would have to fight through 10 years of development to get the software to work on Ubuntu 22.04. However, we could also just create an image which uses Ubuntu 12.04, install the required software, and then run it as a container on Ubuntu 22.04.

3. **Reproducibility:** Containers allow us to share the exact system that code was run on. This removes any system or version-dependent behavior. Imagine we submitted a paper that ran some analysis with some dependency. In between submission and receiving comments, the dependency was updated (from version 1.1 to version 1.2). This introduces a 1% discrepancy depending on which version is used. Since our code heavily depends on this dependency, that 1% discrepancy, which might have been acceptable to the developers, propagates to a larger 10% discrepancy. This could be very difficult to debug if we updated a lot of packages, especially if I need to respond to a reviewer's comments within a tight timeframe! Luckily, I created an image of the analysis at the time of submission. Therefore, I can create a container from that older image and address the reviewer's comments using the version of the code the analysis was initially run with.

**See also:**
- [What even is a container?](https://jvns.ca/blog/2016/10/10/what-even-is-a-container/)



### Containers vs Virtual Machines

Containers and Virtual Machines (VMs) are similar concepts, but they differ in how they achieve virtualization, particularly from a software and hardware perspective.

A VM is an entire operating system, including the entire file system, system kernel, and anything else required to run the operating system. Because of this, VMs tend to have larger file sizes than container images.

On the other hand, a container uses the host system's operating system through a container engine. Therefore, a container only requires the files necessary to run the application or group of applications it is designed for, without using the host system's kernel. This is based on the advanced Linux concept known as "namespaces." Essentially, the container will have its own "namespace" with its version of libraries, separate from the host OS.

A VM requires dedicated access to real hardware resources (memory, CPU, GPU, etc.). It obtains this using a "hypervisor," a process that allocates parts of the real hardware and creates virtual hardware that the VM will use. For example, if a VM needs to use 20% of the system RAM, the hypervisor would allocate 20% of the available RAM as virtual RAM, which would be used exclusively by the VM. One downside of using VMs is that since only the VM can use the allocated resources, we could never have more than 5 VMs of this configuration active at a time (as it would exceed 100% of the available resources).

In contrast, a container is executed like a normal process on the host system. Resources can be allocated as they would for any other process on a system. This allows multiple containers to operate simultaneously, with the system scheduler handling resource allocation between them. For example, if both a VM and a container need 20% of the system RAM during operations, the VM will "own" 20% of the RAM for the entire lifetime of the VM. However, the container will only "own" as much RAM as it needs at any given time. Therefore, during periods of low resource usage, such as between expensive operations when the RAM usage drops to, say, 10%, the system can allocate the remaining 10% to other processes.

Regarding startup time, since containers use the host system, they take seconds to start up (essentially just copying files). In contrast, a VM might require the VM OS to "boot" before starting up, which can take minutes (as it needs to boot an entire operating system before executing a command).

**See also:**
- [Difference between Containers and Virtual Machines](https://dockerlabs.collabnix.com/beginners/difference-vm-containers.html)

## Apptainer/Singularity


Apptainer, formerly known as Singularity, is a [computer program that performs operating-system-level virtualization](https://en.wikipedia.org/wiki/Singularity_(software)), commonly known as containerization. It addresses security concerns associated with other containerization software, making it popular in high-performance computing (HPC) environments. Apptainer enables developers to create and develop code in their preferred environment before packaging it into a Singularity Container Image (SCI). These images can be easily shared with others while ensuring reproducibility in various computing environments.


## Pulling a Pre-exisiting Image

There are numerous sources of pre-existing images. Commonly used ones are [DockerHub](https://hub.docker.com/), [GitHub Container Registry](https://ghcr.io), and [Library](https://singularityhub.github.io/library-api/#/?id=library-api).

Apptainer can convert Docker images directly into Apptainer images. This is extremely useful, allowing us to piggyback on the work of others. For example, let's say we would like to have the latest version of Python to run a test; we could simply use the latest [Python Docker image on DockerHub](https://hub.docker.com/_/python) using something like:


```
> apptainer shell docker://python:latest
```

This would create an Apptainer image and start an interactive `shell` in a container generated from the python:latest image hosted on DockerHub.
```
> apptainer shell docker://python:latest
INFO:    Using cached SIF image
Apptainer> python --version
Python 3.12.2
```
If we wanted to access a different version, for example if we needed Python 2.7, we could use:
```
> apptainer shell docker://python:2.7   
INFO:    Converting OCI blobs to SIF format
INFO:    Starting build...
Getting image source signatures
Copying blob 6f4489a7e4cf done  
Copying blob fd4b47407fc3 done  
Copying blob dc3f0c679f0f done  
Copying blob 09b6f03ffac4 done  
Copying blob b32f6bf7d96d done  
Copying blob 7e2b2a5af8f6 done  
Copying blob af4b99ad9ef0 done  
Copying blob 39db0bc48c26 done  
Copying blob acb4a89489fc done  
Copying config 8452137826 done  
Writing manifest to image destination
Storing signatures
2024/03/25 11:06:37  info unpack layer: sha256:7e2b2a5af8f65687add6d864d5841067e23bd435eb1a051be6fe1ea2384946b4
2024/03/25 11:06:38  info unpack layer: sha256:09b6f03ffac4cb4e42f8ab0bfc480bd3a3fa20e1ddee37784db63bc886b0cbb3
2024/03/25 11:06:38  info unpack layer: sha256:dc3f0c679f0f4c39597721c1df5cdb4f9685b26bd789a44eeb406835a1800d5f
2024/03/25 11:06:38  info unpack layer: sha256:fd4b47407fc30b8206971ec60f280b107b00df8007da2fb912ebb8656b53695e
2024/03/25 11:06:40  info unpack layer: sha256:b32f6bf7d96d26a22dc62da6522f384dcdc936c30c88b233d378e06cf127346d
2024/03/25 11:06:43  info unpack layer: sha256:6f4489a7e4cfcda98c90d9fb220ab8dbf5e40a7a6d756ed414707967aa96bfbd
2024/03/25 11:06:43  info unpack layer: sha256:af4b99ad9ef03daa029d78458e669f135a3c41764bbc154e9d56a3d9b2ee7bf1
2024/03/25 11:06:43  info unpack layer: sha256:39db0bc48c262bd32f4b201a4fad3dde162e73d3d1135fdaab433477156ad816
2024/03/25 11:06:43  info unpack layer: sha256:acb4a89489fc21e4c05c6ef86dacf640cab884b3b3e207cfd5ad24da02f14661
INFO:    Creating SIF file...
Apptainer> python --version
Python 2.7.18
```

We can see that Apptainer will first pull the image in layers from DockerHub before creating a `SIF` (Singularity Image Format) file. If we leave out the `tag` when pulling from DockerHub, the `latest` tag is always chosen.
```
> apptainer shell docker://python    
INFO:    Using cached SIF image
Apptainer> python --version
Python 3.12.2
```

## Editing images using `sandbox`

When taking a base image, it is often the case that we're missing packages or we would like to install other packages into that image. For example, the Python container we've been using doesn't have `ipython`.
```
> apptainer shell docker://python
INFO:    Using cached SIF image
Apptainer> ipython
bash: ipython: command not found
```

We can create a `sandbox`, essentially unpacking the contents of the image into a directory, allowing that image to be modified.
```
> apptainer build --sandbox python_project docker://python
INFO:    Starting build...
Getting image source signatures
Copying blob 63941d09e532 skipped: already exists  
Copying blob d68cd2123173 skipped: already exists  
Copying blob 567db630df8d skipped: already exists  
Copying blob 09527fa4de8d skipped: already exists  
Copying blob 5f899db30843 skipped: already exists  
Copying blob 3cb8f9c23302 skipped: already exists  
Copying blob 71215d55680c skipped: already exists  
Copying blob 097431623722 skipped: already exists  
Copying config 35a79b0576 done  
Writing manifest to image destination
Storing signatures
2024/03/25 11:18:13  info unpack layer: sha256:71215d55680cf0ab2dcc0e1dd65ed76414e3fb0c294249b5b9319a8fa7c398e4
2024/03/25 11:18:14  info unpack layer: sha256:3cb8f9c23302e175d87a827f0a1c376bd59b1f6949bd3bc24ab8da0d669cdfa0
2024/03/25 11:18:14  info unpack layer: sha256:5f899db30843f8330d5a40d1acb26bb00e93a9f21bff253f31c20562fa264767
2024/03/25 11:18:15  info unpack layer: sha256:567db630df8d441ffe43e050ede26996c87e3b33c99f79d4fba0bf6b7ffa0213
2024/03/25 11:18:19  info unpack layer: sha256:d68cd2123173935e339e3feb56980a0aefd7364ad43ca2b9750699e60fbf74c6
2024/03/25 11:18:19  info unpack layer: sha256:63941d09e5322b88281f3a325eff9ced5bf2ee45b691aaf8ec2f829bafbd8021
2024/03/25 11:18:20  info unpack layer: sha256:097431623722383300c03bb41fd162d32346bf6a02a053263f51969eb9746e3d
2024/03/25 11:18:20  info unpack layer: sha256:09527fa4de8dd73399164c307942cc43652a01fc2bb370e38ae0f806b42b4b18
INFO:    Creating sandbox directory...
INFO:    Build complete: python_project
(base) 
```

Here we have run `apptainer build --sandbox python_project docker://python`. We specify the base image as `docker://python` (the latest version of the Python image on DockerHub), and we `build` a `--sandbox` directory with the name `python_project`. 
If we look inside this directory, it will look very similar to what is at `/` (root directory) of your own machine:
```
> ls python_project 
bin  boot  dev  environment  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  singularity  srv  sys  tmp  usr  var
```
We can then create a new container by executing the following command:
```
> apptainer shell --writable python_project
```
Within the container, we can proceed to install ipython.
```
pip install ipython
```
To exit the image, type `exit`. To confirm that `ipython` is now installed, we can recreate the container using the following command:
```
> apptainer shell python_project
Apptainer> ipython --version
8.22.2
```
Note that we aren't calling `--writable` because we no longer need the directory to be writable. We could have the container writable; however, this is bad practice as modifying a container unintentionally might break compatibility with others using the container.


## Creating a basic Image using `build`

We have now pulled an image from DockerHub, created a modified version of that image, and saved it to a directory.

Looking at the directory, we notice that it takes up a pretty substantial amount of memory:
```
> du -sh ./python_project 
1.1G	./python_project
```

If we only have a single image that we work with, 1GB might not be too bad, but as we increase the complexity of the project and use more containers, this will quickly take up a lot of space.

We can build a `SIF` (Singularity Image Format) file from that directory using:
```
> apptainer build python_project.sif python_project

INFO:    Starting build...
INFO:    Creating SIF file...
INFO:    Build complete: python_project.sif

```
Note that the format is `apptainer build <output_name> <input_name>`.

This command creates a file called `python_project.sif`, which can be thought of as a compressed version of the `python_project` directory:
```
> du -sh ./*
1.1G	./python_project
346M	./python_project.sif
```
In this case, the `sif` file takes up around 1/3 of the storage of the directory.


## `apptainer run` and `apptainer exec` commands

Containers can be given a predefined command to run. This command can be executed using `apptainer run <image_name>`. For example, with the `python_project` image:
```
> apptainer run python_project.sif 
Python 3.12.2 (main, Mar 12 2024, 11:02:14) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

We can see that this puts us into a Python interpreter as designed by the [maintainers of this image](https://github.com/docker-library/python/blob/ec3500d01443b87701962245a9f465d05007dc8a/3.13-rc/bookworm/Dockerfile#L125).

We can also specify the command to `run`. Consider the Python script `hello.py`:
```python
print ("Hello, world!")
print ("Inside of container!")
```

We can run this script using the container:
```
> apptainer exec python_project.sif python hello.py
Hello, world!
Inside of container!
```

`apptainer run` executes the default command specified by the image author, while `apptainer exec` allows you to run custom commands within a running container.

## Binding file systems

By default, the Apptainer image will `bind` directories to the container, allowing them to be accessed from within the container. This behavior may depend on your environment (for example, whether or not a read directory is automatically bound).

We can explicitly `bind` directories when executing/running commands using the following syntax:


```
apptainer exec -B </path/to/local/directory>:</path/to/container/mount/point> image.sif <command>
```

For example:
```
> apptainer exec -B $HOME/Downloads:/Downloads python_project.sif bash
```

This command mounts the `~/Downloads` folder to `/Downloads` within the container and runs `bash` to get an interactive terminal. We could then access the downloads from `/Downloads`.

We can bind multiple directories, for example:

```
> apptainer exec -B $HOME/Downloads:/Downloads -B $HOME/Desktop:/Desktop  python_project.sif bash
```

By default, Apptainer will also mount the `$HOME` directory. This can occasionally be problematic; for example, if you have Python libraries stored in `$HOME`, they may be picked up when mounting the `$HOME` directory instead of the libraries stored in the image. You can specify the `$HOME` directory using `--home <dir_name>`:

```
> apptainer exec --home `pwd` python_project.sif bash                                          
```

This command sets the `$HOME` to be the current directory when launching the container. 

## Creating an image from a definition file

Similar to Docker, we can create an image from a file with a list of instructions.

Apptainer `def` files follow this format:
```
Bootstrap: docker
From: ubuntu:{{ VERSION }}
Stage: build

%arguments
    VERSION=22.04

%setup

%files

%environment

    
%post


%runscript

%startscript
    
%test

%labels

%help

```

We'll walk through these sections one by one.

### Preamble

```
Bootstrap: docker
From: ubuntu
Stage: build
```

* `Bootstrap` specifies where we are getting the base image from. In this case, it's `docker` (DockerHub).
* `From:` specifies the base image. In this case, it will grab the latest Ubuntu image.
* `Stage:` specifies the stage of the build. Multiple stages can be used to simplify the build process and reduce the final file size.


### `%arguments`

```
Bootstrap: docker
From: ubuntu:{{ VERSION }}
Stage: build

%arguments
    VERSION=22.04
```

Arguments are variables that can be used within the definition file. Using arguments allows us to change variables only in one place rather than multiple instances, preventing bugs.

In the above example, we've specified an argument `VERSION=22.04`. This argument is then accessed in the preamble when selecting the Ubuntu image version:


```
From: ubuntu:{{ VERSION }}
```
This specifies that we will be using `ubuntu:22.04`.

### `%setup`

Setup commands are first executed outside of the container on the host system before starting to build the image.

For example, suppose we want to compress some files that will later be added to the container:

```
%setup

    tar -zcvf files.tar.gz ./*.txt
```

This command would compress all the files ending in `.txt` in the current directory into `files.tar.gz` (also in the current directory).


### `%files`

This is where we can specify files to be copied into the container.
```
%files
    files.tar.gz /opt
```
Here, we are copying the `files.tar.gz` that was created in the `%setup` into the `/opt` directory of the image (`/opt/files.tar.gz`).

### `%environment`

Here we specify environmental variables that we want set within the container.

```
%enviroment
    export PATH=$PATH:/app/bin
    export DEFAULT_PORT=8001
```

In this example, we set two environmental variables. First, we modify the `PATH` to include `/app/bin`, where the hypothetical binaries for our application reside. Second, we specify the `DEFAULT_PORT` to be `8001`.

We can access these variables anytime within the container or the build process.

### `%post`

In this section, we specify the command we want to run after the base image has downloaded. Environmental variables for the host system are not passed, so this can be considered a clean environment.

This will likely be the most detailed section of your definition script. For example:

```
%post
    apt-get update && apt-get install -y gcc
    pip install ipython
```

In the above example, we are simply updating the Ubuntu base image and installing `gcc`. We then install `ipython` using `pip`.

This is a simple example, but `%post` would be the section where dependencies would be installed and/or compiled.


### `%runscript`

This is where we define a set of commands that will be executed when running `apptainer run image.sif` or when running the image itself as a command (e.g., `./image.sif`).

Internally, these commands will form a simple script that will be executed.

```
%runscript
    ipython
```

This example will start an IPython interpreter. We could have something more complicated, such as:

```
%runscript
    echo "Recieved the following arguements $*"
    ipython $*
```

This will output the arguments passed before executing them with IPython. For example:

```
> apptainer run ./jupyter.sif --version
Recieved the following arguements --version
8.22.2
```
Here, we're passing `--version` as an argument. This gets passed and run as `ipython --version`, which gives `8.22.2`.

One could use the `%runscript` section to define a default behavior and how arguments are handled.



### `%startscript`

This is similar to the `%runscript` section where we create a script to be run when running the container. Specifically, the `%startscript` runs when the container is launched as an `instance` rather than a process launched with `run` or `exec`. Instances can be considered more of a daemon, which will have a more passive interface. For example, an instance may monitor a port to receive a command that controls its behavior. It might be better to launch a web server as an instance.

Likewise, if you have multiple steps in a data pipeline, they could be passed between instances which are persistent compared to the analysis target.




### `%test`

This defines a test script that is run at the end of the build process and can be used to ensure the validity of the built container.

For example, if we are building a data pipeline, we might want to make sure we get the expected answer.


```
%test
    python test_script.py
    if [ $? -eq 0 ]; then
        echo "Script executed successfully"
    else
        echo "Script failed"
        exit 1
    fi
```
Here we are running `test_script.py`. The output of this code will be accessible using `$?`, which returns the last return code.

```
    if [ $? -eq 0 ]; then
```
This line checks if the return code is 0, which is a typical code for a successful execution. In our Python code, we would have a line like:

```
if successful_test:
    exit(0)
else:
    exit(1)
```
If the code executes successfully, then the return will be 0; otherwise, it will be 1.


### `%labels`
```
%labels
    Author myuser@example.com
    Version v0.0.1
    MyLabel Hello World
```

Here we define a set of labels that are viewable using the `apptainer inspect` command.

Versioning can be super important when developing an application. Maintaining an up-to-date version number can prevent a lot of headaches when trying to debug issues.


### `%help`

Help specifies a help message that will be outputted:

```
%help
    This is a container with jupyter lab and notebook install
```

This can be accessed using:
```
apptainer run-help my_container.sif
```


## Example definition script
Here is an example of a `.def` file which installs `Jupyter`, `IPython`, `Matplotlib`, and `NumPy`.

```
Bootstrap: docker
From: python:latest

%post
    pip install jupyter ipykernel jupyterlab notebook
    pip install matplotlib numpy

%environment
    export DEFAULT_PORT=8001

%runscript
    ipython $*

%startscript
    jupyter lab --port=$DEFAULT_PORT
```

This can be built with:
```
> apptainer build jupyter.sif jupyter.def
```

The `runscript` will take arguments and pass them to IPython. For example:
```
> ./jupyter.sif hello.py
Hello, world!
Inside of container!
```

The `startscript` will start a Jupyter Lab on port 8001. This can be launched using:
```
> apptainer instance start jupyter.sif jupyter-server 
```

When navigating to `http://localhost:8001`, we'll notice that we need to log in. We can get a login code using:"
```
> apptainer exec instance://jupyter-server jupyter lab list
Currently running servers:
http://localhost:8001/?token=643b97dc15207ca577782ea2e03a3ec1f9337a4445bc1db8 :: /home/obriens/Documents/apptainer
```

Clicking on that link will log us in. We need to remember to `stop` the instance once we're finished.

```
> apptainer instance stop jupyter-server            
```

## Example of a multi-stage build

As mentioned earlier, using multi-stage builds can help decrease the final size of the `sif` file.

Consider the following `C++` code:

```c++ title="convert_units.cpp"
#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char *argv[]){

    // parse the command passed
    // Input is in meters
    float input = atof(argv[1]);

    // convert unit to mm
    float output = input * 1e3;

    // output to a text file
    ofstream out_file;
    out_file.open("test.txt");
    out_file << output << endl;

    // Also print
    cout << output << endl;
    return 0;
}
```

This will convert meters to mm. We can imagine this being part of a larger data analysis pipeline.

This can be compiled using:
```
g++ convert_units.cpp -o convert_units
```
This will create a binary called `convert_units`.

Let's start to build the definition file:

```title="single_stage.def" linenums="1"
Bootstrap: docker
From: ubuntu
Stage: build

%files
    convert_units.cpp /build/convert_units.cpp
    
%post
    apt-get update && apt-get upgrade -y && apt-get install -y g++
    g++ /build/convert_units.cpp -o /bin/convert_units

%runscript
    /bin/convert_units $*
```

Here we have a single stage called `build`. In this stage, we copy the source code to the `/build` directory at the `%files` stage. In the `%post` stage, we update the OS and install `g++`, a C++ compiler. We then compile the code to `/bin/convert_units`. We then specify this as the entry point of the `%runscript` stage.

We can run this as:
```
> ./single_stage.sif 1.25
1250
```

You'll notice that the `convert_units.cpp` file is no longer needed once `convert_units` is compiled. Likewise, we only need `g++` to compile `convert_units`; we don't use it later in the file. We could turn this into a multi-stage build:

```linenums="1" title="multi_stage.def" hl_lines="17"
Bootstrap: docker
From: ubuntu
Stage: build


%files
    convert_units.cpp /build/convert_units.cpp
    
%post
    apt-get update && apt-get upgrade -y && apt-get install -y g++
    g++ /build/convert_units.cpp -o /build/convert_units

Bootstrap: docker
From: ubuntu
Stage: final

%files from build
  /build/convert_units /bin/convert_units

%post
    apt-get update && apt-get upgrade -y

%runscript
    /bin/convert_units $*
```

The definition file is similar to the `single_stage.def` file; however, we have broken this up into two stages. 

The first stage, tagged as `build`, will add the source file `convert_units.cpp` to the image, update the OS, install `g++`, and compile `/build/convert_units`.

The second stage, called `final`, uses the same `Bootstrap` and base image (`ubuntu`) as the `build` stage. However, at the `%files` stage on line 17, we are only copying the `/build/convert_units` from the `build` stage to `/bin/convert_units` in the `final` stage. We still want to make sure we have an up-to-date OS (security updates are always important), so we still run `apt-get update && apt-get upgrade -y`. Finally, the `%runscript` stage is only included in the `final` stage.

We can see that we get the same behavior from both images:

```
> ./single_stage.sif 1.25 ;  ./multi_stage.sif 1.25
1250
1250
```

However, when we look at the size of the files, we see a difference:
```
> ls -lah ./*_stage.sif
-rwxr-xr-x 1 obriens obriens  63M Mar 25 14:36 ./multi_stage.sif
-rwxr-xr-x 1 obriens obriens 142M Mar 25 14:36 ./single_stage.sif
```


You'll notice that the `multi_stage.sif` build is around half the size of `single_stage.sif`. This is partly due to the `multi_stage.sif` not containing the source code (`convert_units.cpp`), but also due to it not containing `g++`.



<!-- ## Converting a Docker Image to an Apptainer Image

Here we have a similar image as above written as a Dockerfile:
```
# syntax=docker/dockerfile:1

FROM ubuntu:latest

RUN apt update && apt upgrade -y && apt install -y g++ 

RUN mkdir /app
COPY ./convert_units.cpp /app
WORKDIR /app
RUN g++ convert_units.cpp -o /bin/convert_units
ENTRYPOINT ["/bin/convert_units"]
```

Note we're specifying the entry point to be the compiled executable `/bin/convert_units`.

We can build this with:
```
> docker build . -t local/convert_units:latest
```
Where `.` specfies the current directory as the location of the Dockerfile, and we `tag` the version with `-t` with the name `local/convert_units:latest`. 

We can run this as:
```
> docker run local/convert_units:latest 10.5  
10500
``` -->


