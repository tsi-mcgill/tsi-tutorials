# Workshop Part 1: Introduction to Docker and Containerization

Topics that will be covered:

* Introduction to Containerization
    * Definition and benefits of containerization
    * Differences between virtual machines and containers

* Docker Basics
    * Overview of Docker
    * Installing Docker on various platforms
    * Basic Docker commands: `docker run`, `docker ps`, `docker stop`, `docker rm`

* Creating Docker Images
    * Writing a simple Dockerfile
    * Building and running a Docker image
    * Understanding image layers

* Managing Docker Containers
    * Container lifecycle: start, stop, remove
    * Docker networking basics


# Docker Basics

Docker has a streamlined install process for most modern operating systems. Please ensure that Docker is installed and tested on your machine before starting the workshop.

## Installing Docker on Various Platforms

### Docker Engine

The Docker Engine can be installed on Windows, macOS, and Linux. Instructions can be found [here](https://docs.docker.com/engine/install/).

### Docker Desktop

[Docker Desktop](https://docs.docker.com/desktop/) provides a high-level interface for viewing, accessing, and managing your containers and images. There are many useful extensions you can install, such as:

* [Disk Usage](https://hub.docker.com/extensions/docker/disk-usage-extension): A tool that "displays and categorizes the disk space used by Docker."
* [Resource Usage](https://hub.docker.com/extensions/docker/resource-usage-extension): A tool to monitor the resource usage of your containers.
* [Logs Explorer](https://hub.docker.com/extensions/docker/logs-explorer-extension): A tool for examining and filtering logs from your containers.

### Creating and Adding Users to the `docker` Group

If installing Docker on Linux (including WSL), you might want to add your user to the `docker` group so that you don't need elevated permissions to run a container. Instructions on how to do this can be found [here](https://docs.docker.com/engine/install/linux-postinstall/).



## Getting ready for the Workshop

The workshop will require images to be pulled from a remote server, hence requiring internet access. 
To avoid network congestion, please `pull` the following images by running the commands below:

```
docker pull hello-world
docker pull python:3.9-slim
docker pull ubuntu
```

## Overview of Docker

# Docker Basics

Docker is a powerful tool that streamlines the process of building, sharing, and running applications. 
It uses "containerization" technology to create isolated environments, or containers, for applications and their dependencies. 
These containers are lightweight, portable, and **consistent**, ensuring that software runs the same way in development, testing, and production environments. 
By encapsulating an application and its environment, Docker simplifies the management of software projects, enhances productivity, and facilitates continuous integration and delivery (CI/CD). 
This makes it an essential tool for modern software development and deployment practices.

Docker and containerization solve the "it works on my machine" problem that one often faces when developing or running an application. 
Using Docker, a developer can package the required dependencies of an application, providing a stable environment for the application to run, and then pass this environment onto the user to run as an "image."
Using this "image," a user can then recreate the same environment that the developer intended for running the application and execute the application on their own machine as a "container."
Critically, this "container" acts as a semi-independent operating system within the host operating system, meaning that potential conflicts arising on the host system can be overcome by the containerized image. 
For example, if you have a Windows machine and you want to run software developed for Linux, Docker provides a method to run this software as if the host system were Linux.
Similarly, if the host system has some dependency (for example, Python 3) and the application has some conflicting dependency (for example, Python 2), the container will run the application using the dependencies in the container rather than the host operating system.

You may have previously heard of "Virtual Machines" (VMs). 
This is a similar idea to containers, with some important differences.
VMs work by allocating virtual hardware (e.g., CPU, GPU, RAM, and storage) and installing the entire operating system. 
This can make them quite resource-intensive.
A container, on the other hand, uses the fact that Linux systems tend to be very similar, to the extent that the underlying system kernel can be used.
A container image essentially contains a filesystem snapshot (FSS) and a run command. 
The FSS can be considered all the files, folders, programs, and libraries required to run the application that the container has been developed for.
When we create a container from the image, we are essentially loading the FSS into a new local "namespace."
The host system's resources are then allocated to the container like any other process.
Within this new namespace, we have access to the versions of files, programs, and libraries that are defined in the FSS (e.g., we might have Python 3.11.1).
By design, the container cannot "see" outside of the namespace; as far as the container can see, it is the only thing operating on the system.
The run command defines the default behavior of the container. 
This could be something like starting a new bash shell, executing a program, or starting a service.

In summary, the differences between VMs and containers are:

1. Operating System Requirements:
    - A VM requires the full operating system to be installed on the host system.
    - A container shares the host system's kernel and includes only the necessary binaries, libraries, and configuration files needed to run a specific application or suite of applications.

2. Resource Allocation and Efficiency:
    - VMs require specific resources to be allocated to them, such as CPU, RAM, and storage. These resources are managed by a "hypervisor," which runs on the host system. Each VM operates in isolation with its own OS, leading to higher overhead due to the need to replicate the OS and allocate dedicated resources.
    - Containers use the host system’s kernel to run processes and do not require a separate OS. They are managed by the container runtime (e.g., Docker Engine) and leverage the host system’s resources dynamically. Containers are subject to the host's system scheduler, just like any other process, allowing them to be more efficient in terms of resource utilization.

3. Startup Time:
    - A VM will require the entire guest operating system to boot before running a process.
    - A container does not require a guest operating system, meaning that a process can be started with very little downtime.

4. Isolation:
    - VMs provide a different operating system for a process to run on. This provides strong isolation between the host system and any number of guest operating systems.
    - Containers provide **process-level isolation**. They are isolated from each other using the host operating system's features like namespaces and cgroups, but they share the same OS kernel.



## Basic Docker commands: `docker run`, `docker ps`, `docker stop`, `docker rm`

Let's start off by using pre-made Docker images to look at some of the fundamental commands.

### `docker run`

The `docker run` command can be used to run the default command for a Docker image. For example, let's use the [hello-world](https://hub.docker.com/_/hello-world) example:
```
docker run hello-world
```

If you haven't ran this before, you will see the following:
```
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
c1ec31eb5944: Pull complete
Digest: sha256:94323f3e5e09a8b9515d74337010375a456c909543e1ff1538f5116d38ab3989
Status: Downloaded newer image for hello-world:latest
```

Let's take a moment to break this down:
```
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
```
Here we can see that Docker cannot find the `hello-world:latest` image locally and instead pulls an image from `library/hello-world`. Here Docker is searching container repositories like [Docker Hub](https://hub.docker.com/) to find the `hello-world` image.

Once the image is finished downloading, a default command is run, which gives the following output:
```
Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

This provides some information on what has just happened and suggests that we try running a command like:
```
docker run -it ubuntu bash
```

So let's do that:
```
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
9c704ecd0c69: Pull complete
Digest: sha256:2e863c44b718727c860746568e1d54afd13b2fa71b160f5cd9058fc436217b30
Status: Downloaded newer image for ubuntu:latest
root@b52ba93a0cc5:/#
```
Once again, we didn't have the `ubuntu:latest` image available locally, so Docker downloaded this image. 
We notice now that we are left with a prompt:
```
root@a1fe94f95dc6:/#
```
Let's breakdown the command we just ran:
```
docker run -it ubuntu bash
```
Here we've used `run` to specify that we want to run an image in a container. `-it` specifies that we want an interactive shell (`-i` allows STDIN to remain open for sending commands, and `-t` allocates a text terminal for running commands within the shell). We specified the image as `ubuntu`; however, unlike the previous example (`hello-world:latest`), we didn't specify the "tag" or "version" to use, so by default, the "latest" tag will be used for the `ubuntu` image. Finally, we specified the command we wanted to run, `bash`, which starts a new bash shell. 

In summary, using `docker run -it ubuntu bash`, we have started a container running `ubuntu` (specifically `ubuntu:latest` by default), configured an interactive terminal (`-it`) for command interaction, and initiated a bash shell (`bash`) within the container.

Jumping back into the container we can run commands like:
```
root@a1fe94f95dc6:/# whoami
root
```
This tells us that the current user is `root`. 
```
root@a1fe94f95dc6:/# hostname
a1fe94f95dc6
```
This tells us the name of the host as viewed from within the docker container. Notice that this will be different to the name of your system. As far as the container knows, it is running on a seperate system called `a1fe94f95dc6`.
```
root@a1fe94f95dc6:/# echo "Hello"
Hello
```
Many commonly used commands are preinstalled in the Ubuntu Docker image.
When we want to exit, we simply type:
```
root@a1fe94f95dc6:/# exit
exit
```

We can run commands directly by specifying the command:
```
docker run -it ubuntu top
```

This will run the `top` command, which is useful for viewing processes running on the machine. You should see output similar to this:
```
top - 14:56:11 up 47 min,  0 user,  load average: 0.02, 0.07, 0.08
Tasks:   1 total,   1 running,   0 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.2 us,  0.3 sy,  0.0 ni, 99.3 id,  0.1 wa,  0.0 hi,  0.1 si,  0.0 st
MiB Mem :   7536.3 total,   5033.9 free,   2113.9 used,    621.6 buff/cache
MiB Swap:   2048.0 total,   2048.0 free,      0.0 used.   5422.5 avail Mem

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
    1 root      20   0    8864   5012   2908 R   0.0   0.1   0:00.02 top
```

Notice that there is only one process running. This is because the container is isolated and cannot see processes outside of its own environment. As far as the container is concerned, it operates in isolation with no other processes running. To quit `top`, simply press `q`.

### `docker ps`

Let's run a Docker container with a command, but this time let's run it in the background without using `-it`. Instead, we'll use `-d` to "detach" the container:
```
docker run -d ubuntu sh -c "while true; do echo 'Hello, Docker!'; sleep 60; done"
```
The command we ran will start with an `ubuntu` image and execute `sh -c "while true; do echo 'Hello, Docker!'; sleep 60; done"`. This will start a new `sh` shell, which loops indefinitely and prints "Hello, Docker!" every 60 seconds.

The output we should see is something like this:

```
5af71a22c48073e0feccea5d6b6100ee1d428449fbef74b95324a29b6cfc6d18
```
This is the container's ID, which we can later use to access the container. Notably, we don't immediately see the "Hello, Docker!" output. However, when we run:

```
docker ps
```
We will see:
```
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS     NAMES
5af71a22c480   ubuntu    "sh -c 'while true; …"   2 minutes ago   Up 2 minutes             nostalgic_hertz
```
Here we can see the containers currently running. The output displays the container ID, the image being used, the command that was run, the time it was created, the current status, any exposed ports (more on this later), and a container name.

We can view the output of the container using the `docker logs` command. Here, we can either pass the container ID or the container name:

```
docker logs 5af71a22c480
Hello, Docker!
Hello, Docker!
Hello, Docker!
Hello, Docker!
Hello, Docker!
```
or 
```
docker logs nostalgic_hertz
Hello, Docker!
Hello, Docker!
Hello, Docker!
Hello, Docker!
Hello, Docker!
Hello, Docker!
```

Giving a name to a container makes it easier to identify and manage. We can assign a name to a container using the `--name` flag when launching it:
```
docker run -d --name greeter ubuntu sh -c "while true; do echo 'Hello, Docker!'; sleep 60; done"
```

In this example, `--name greeter` names the container as "greeter". We can verify this by using `docker ps`:
```
docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS     NAMES
34e6f000f761   ubuntu    "sh -c 'while true; …"   44 seconds ago   Up 42 seconds             greeter
5af71a22c480   ubuntu    "sh -c 'while true; …"   7 minutes ago    Up 7 minutes              nostalgic_hertz
```


By default, `docker ps` shows only active containers. To view all containers, including those that have exited, we use `docker ps -a`, which might display something like this:
```
docker ps -a
CONTAINER ID   IMAGE         COMMAND                  CREATED             STATUS                         PORTS     NAMES
34e6f000f761   ubuntu        "sh -c 'while true; …"   13 minutes ago      Up 12 minutes                            greeter
5af71a22c480   ubuntu        "sh -c 'while true; …"   19 minutes ago      Up 19 minutes                            nostalgic_hertz
b1709a781e28   ubuntu        "pwd"                    About an hour ago   Exited (0) About an hour ago             laughing_lumiere
f02b7d8ca480   ubuntu        "ls"                     About an hour ago   Exited (0) About an hour ago             lucid_curran
120a97deeb54   ubuntu        "ls /home/obriens/"      About an hour ago   Exited (2) About an hour ago             silly_swartz
aee56c00887d   ubuntu        "ls"                     About an hour ago   Exited (0) About an hour ago             great_payne
7f344b33f26f   ubuntu        "whoami"                 About an hour ago   Exited (0) About an hour ago             flamboyant_mahavira
05317adbd6b3   ubuntu        "hostname"               About an hour ago   Exited (0) About an hour ago             laughing_tesla
```

This output shows two running containers (`greeter` and `nostalgic_hertz`) and several containers that have exited but are still present.


### `docker stop`

Let's examine our active containers:
```
docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS     NAMES
34e6f000f761   ubuntu    "sh -c 'while true; …"   15 minutes ago   Up 15 minutes             greeter
5af71a22c480   ubuntu    "sh -c 'while true; …"   22 minutes ago   Up 22 minutes             nostalgic_hertz
```


To stop a container, use `docker stop` followed by either the container name or ID:
```
docker stop 5af71a22c480
```

This command may take a few seconds to complete. When `docker stop` is invoked, it sends a `SIGTERM` signal to the process running inside the container. `SIGTERM` is a soft request for the process to finish. If the process is designed to handle this signal, it may initiate a graceful shutdown.

After sending `SIGTERM`, Docker waits for 10 seconds (by default) to allow for a graceful shutdown. If the process does not terminate gracefully within this time frame, Docker then sends a `SIGKILL` signal, which forcefully terminates the process.

In summary, `docker stop` attempts to gracefully terminate the program inside the container. If the program does not respond to `SIGTERM`, Docker resorts to forcefully terminating it with `SIGKILL`.

### `docker rm`

Similar to the `rm` command in Unix-like systems, `docker rm` removes a container. Let's first review our running containers:


```
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS     NAMES
34e6f000f761   ubuntu    "sh -c 'while true; …"   29 minutes ago   Up 29 minutes             greeter
```

Now, let's try to remove the `greeter` container:
```
 docker rm greeter
Error response from daemon: You cannot remove a running container 34e6f000f76147c340648064e1e0356d483142f8ad6cb02fcb228a536c0ac39a. Stop the container before attempting removal or force remove
```
We need to stop a container before removing it:
```
docker stop greeter && docker rm greeter
```

Checking with `docker ps` confirms that the `greeter` container has been stopped. Running `docker ps -a` shows that `greeter` is no longer listed, but `nostalgic_hertz` is still there. We can remove it using:
```
docker rm nostalgic_hertz
```


Stale containers can consume memory over time. To remove all exited containers, you can use:
```
docker container prune
```

This command prompts for confirmation before deleting the containers permanently.



## Creating Docker Images

Up until now, we've been using pre-made Docker images. However, there may come a time when we need to create our own custom image.

### Writing a Simple Dockerfile

The first step in creating a Docker image is to write a `Dockerfile`. This file contains instructions on how to build the image. Let's start by writing a short Python program that will serve as the entry point for our image. We'll call this script `app.py`:

```python
import numpy as np

def generate_random_numbers(num_points):
    return np.random.rand(num_points)

def calculate_statistics(numbers):
    mean = np.mean(numbers)
    std_dev = np.std(numbers)
    return mean, std_dev

if __name__ == "__main__":
    num_points = 1000  # Size of the random number list
    numbers = generate_random_numbers(num_points)
    mean, std_dev = calculate_statistics(numbers)
    print(f"Generated {num_points} random numbers")
    print(f"Mean: {mean}")
    print(f"Standard Deviation: {std_dev}")

```

This program generates 1000 random numbers using `NumPy` and prints their mean and standard deviation. Note that `NumPy` is a requirement for this program, so we should create a `requirements.txt`file:
```
numpy
```

Now, let's put together the `Dockerfile`:
```
# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY app.py .

# Specify the command to run the application
CMD ["python", "app.py"]
```

Let's walk through this `Dockerfile`:

- `FROM python:3.9-slim`: This line specifies that we're using the official Python image from Docker Hub, specifically Python 3.9 in its slim variant.

- `WORKDIR /app`: Sets the working directory inside the container to `/app`. If the directory doesn't exist, it will be created.

- `COPY requirements.txt .`: Copies the `requirements.txt` file from the host into the `/app` directory in the container.

- `RUN pip install --no-cache-dir -r requirements.txt`: Installs the Python dependencies listed in `requirements.txt` using `pip`. The `--no-cache-dir` flag ensures that downloaded files aren't cached, which can reduce the size of the final image.

- `COPY app.py .`: Copies app.py from the host into the /app directory in the container.

- `CMD ["python", "app.py"]`: Specifies the command to run when the container starts. In this case, it executes python app.py within the /app directory.

It's common practice to use all caps when specifying `Dockerfile` keywords (`FROM`, `COPY`, `WORKDIR`, `RUN`, `CMD`). This helps differentiate them from commands within the scripts being run inside the container.

Creating custom Docker images allows you to package your applications with all their dependencies, ensuring consistency and reproducibility across different environments.

### Building and Running a Docker Image

Now that we have everything we need, let's build the image. Replace `obriens` with your Docker Hub username if you intend to push this image to Docker Hub:

```
docker build . -t obriens/part1:latest 
```
This command searches for a file named `Dockerfile` in the current directory (specified with `.`), builds the Docker image, and tags it (`-t`) as `obriens/part1:latest`. The username (`obriens` in this case) is specified to indicate where the image will be pushed if you decide to upload it to Docker Hub. The output will resemble something like this:
```
docker build . -t obriens/part1:latest                                                                       130 ↵
[+] Building 17.2s (11/11)
...
 => => writing image sha256:016e858e57ceb90b7b12b2aa8ec0b79642ad20d0ef356c8453e7bc6f2fc78d03                       0.0s
 => => naming to docker.io/obriens/part1:latest                                             
```
The build process involves multiple stages (`[1/5]` to `[5/5]`), where each stage corresponds to a command in your Dockerfile. The final stage (`CMD ["python", "app.py"]`) specifies the command that will be executed when the container starts. Each command creates a separate "layer" of the image, with subsequent layers building upon previous ones.

To run our newly built image as a container, use the `docker run` command:
```
docker run --rm -it obriens/part1:latest
```
Here, the `--rm` flag automatically removes the container once the process inside it finishes. The output should show something like:
```
Generated 1000 random numbers
Mean: 0.4942313233338699
Standard Deviation: 0.28658542837100653 
```
When building the image, we didn't specify the filename (`Dockerfile`) explicitly because Docker defaults to looking for a file named `Dockerfile`. However, you can specify a different filename if needed.

Let's create a development version of our image by modifying `app.py` to include a message indicating it's running from the development container:

```
...
# Copy the rest of the application code into the container
COPY app.py .

RUN echo "print ('Ran from dev container')" >> app.py

# Specify the command to run the application
CMD ["python", "app.py"]
```

This modification uses `echo` to append a line to `app.py` that prints "Ran from dev container". Now, build the development version using a different `Dockerfile` (`Dockerfile.dev`) and tag it as `obriens/part1:dev`:
```
docker build . -f Dockerfile.dev -t obriens/part1:dev
```
Notice that we specified the filename with `-f Dockerfile.dev` and changed the tag to `obriens/part1:dev`. If you try to run `obriens/part1` without specifying a tag, Docker defaults to the latest tag. For example:
```
 docker run --rm -it obriens/part1
Generated 1000 random numbers
Mean: 0.5130255869429714
Standard Deviation: 0.29060466306009264
```
This will run the `latest` tagged image. However, when running the development version:
```
docker run --rm -it obriens/part1:dev
Generated 1000 random numbers
Mean: 0.5011963504428272
Standard Deviation: 0.28711061209965844
Ran from dev container
```
The output will include the additional message from `app.py` indicating it's running from the development container.

Using multiple tags (`latest`, `dev`, etc.) is useful for specifying different versions or configurations of your Docker image. It helps manage different stages of development or deployment scenarios effectively.

#### Why Use Different Tags for Images?

In the example provided, different tags serve several key purposes:

1. **Version Control and Stability**: Tags like `obriens/part1:latest` and `obriens/part1:dev` help distinguish different versions of the same application or service. This ensures that users can choose between stable releases (`latest`) and potentially less stable development versions (`dev`).

2. **Environment Specificity**: Tags can denote images optimized for specific environments or purposes. For instance, `python:3.9-slim` indicates a Python 3.9 base image that is minimal in size (`slim`), which is preferable for lightweight deployments compared to a full version (`python:3.9`).

3. **Dependency Management**: Tags also facilitate managing dependencies. The `dev` tag might include additional libraries or tools needed for testing and development, while the `latest` tag could be streamlined for production use.

By using specific tags like `python:3.9-slim`, developers communicate to users the exact environment and optimizations applied to the image. This clarity helps in maintaining consistency across deployments and ensures compatibility with specific requirements.


### Understanding Image Layers

Previously, we introduced the concept of layers and how images are built layer by layer. Let's explore why this matters with a practical example.

First, let's modify our `requirements.txt` file to include additional dependencies:

```
numpy
matplotlib
```

Now, let's rebuild the image:
```
docker build . -t obriens/part1
[+] Building 17.2s (10/10) FINISHED                                                                      docker:default
 => [internal] load .dockerignore                                                                                  0.0s
 => => transferring context: 2B                                                                                    0.0s
 => [internal] load build definition from Dockerfile                                                               0.0s
 => => transferring dockerfile: 506B                                                                               0.0s
 => [internal] load metadata for docker.io/library/python:3.9-slim                                                 0.3s
 => [1/5] FROM docker.io/library/python:3.9-slim@sha256:e9074b2ea84e00d4a73a7d0c01c52820e7b68d8901c5fa282be4f1b28  0.0s
 => [internal] load build context                                                                                  0.0s
 => => transferring context: 89B                                                                                   0.0s
 => CACHED [2/5] WORKDIR /app                                                                                      0.0s
 => [3/5] COPY requirements.txt .                                                                                  0.0s
 => [4/5] RUN pip install --no-cache-dir -r requirements.txt                                                      15.8s
 => [5/5] COPY app.py .                                                                                            0.0s
 => exporting to image                                                                                             0.8s
 => => exporting layers                                                                                            0.8s
 => => writing image sha256:449c5e51b012be670f98fb5f33a2b7cd1ddc50dddf4f42f2f040fb69f0e4c2c7                       0.0s
 => => naming to docker.io/obriens/part1                                                                           0.0s
```
Notice the output shows:
```
...
 => CACHED [2/5] WORKDIR /app                                                                                      0.0s
...
```

What's happening here is that Docker has "cached" the previous image layers. This means that we don't need to rerun those stages. Instead, Docker starts from the last cached layer and continues building from there.

Now, let's modify `app.py` to print out the median of the sample as well:
```python
import numpy as np

def generate_random_numbers(num_points):
    return np.random.rand(num_points)

def calculate_statistics(numbers):
    mean = np.mean(numbers)
    median = np.median(numbers)
    std_dev = np.std(numbers)
    return mean, median, std_dev

if __name__ == "__main__":
    num_points = 1000  # Size of the random number list
    numbers = generate_random_numbers(num_points)
    mean, median, std_dev = calculate_statistics(numbers)
    print(f"Generated {num_points} random numbers")
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Standard Deviation: {std_dev}")
```

and build this with:
```
docker build . -t obriens/part1
[+] Building 0.5s (10/10) FINISHED                                                                       docker:default
 => [internal] load .dockerignore                                                                                  0.0s
 => => transferring context: 2B                                                                                    0.0s
 => [internal] load build definition from Dockerfile                                                               0.0s
 => => transferring dockerfile: 506B                                                                               0.0s
 => [internal] load metadata for docker.io/library/python:3.9-slim                                                 0.3s
 => [1/5] FROM docker.io/library/python:3.9-slim@sha256:e9074b2ea84e00d4a73a7d0c01c52820e7b68d8901c5fa282be4f1b28  0.0s
 => [internal] load build context                                                                                  0.0s
 => => transferring context: 674B                                                                                  0.0s
 => CACHED [2/5] WORKDIR /app                                                                                      0.0s
 => CACHED [3/5] COPY requirements.txt .                                                                           0.0s
 => CACHED [4/5] RUN pip install --no-cache-dir -r requirements.txt                                                0.0s
 => [5/5] COPY app.py .                                                                                            0.0s
 => exporting to image                                                                                             0.0s
 => => exporting layers                                                                                            0.0s
 => => writing image sha256:455ae0e0323b56ada03933dc2523c7e7fcbe312b25f04536aa8f6cca14943349                       0.0s
 => => naming to docker.io/obriens/part1                                                                           0.0s

What's Next?
  View a summary of image vulnerabilities and recommendations → docker scout quickview
```
Again, notice that Docker uses cached versions of each layer, avoiding recreating previous steps. This concept is crucial when creating images—frequent development and rebuilding can be sped up by caching unchanged steps early in the Dockerfile. However, any change detected in a later step requires rerunning all subsequent steps, regardless of whether they'll result in changes.



## Managing Docker Containers



### Docker networking basics

We can enable networking between our Docker image and the host system. Let's create an image that requires networking. Suppose we've encountered difficulty installing a Python package on our local machine but know it installs correctly on another. We'll build an image containing this Python package, based on the `python:3.9-slim` base image. Given that the base image already includes most dependencies, our `Dockerfile` will be brief:
```
FROM python:3.9-slim

# Use pip to install the requirements
RUN pip install numpy matplotlib jupyterlab notebook ipykernel ipython ipywidgets


# Create a new user and change to that user
RUN useradd europa
USER europa
# Move the europa's home directory
WORKDIR /home/europa

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8000"]
```

Here, the `CMD ["jupyter", "lab"]` command will start a JupyterLab server. The `--ip=0.0.0.0` flag binds the server to all available IP addresses, making it accessible to the outside world. The `--port=8000` option specifies that we're starting the Jupyter server on port 8000.

We've also created a new user within the container called `europa`. By default, Docker runs everything as `root`. This poses several potential issues. Firstly, anyone who can run this container gains root access to everything accessible by the container. For instance, if a file system is accessible to the container (as we'll see shortly), the user would have root privileges within that folder, enabling them to delete or modify any files. This can be particularly problematic on shared systems like computer clusters and poses a significant security concern. If an unauthorized party gains access to the container, they could execute commands as root, potentially installing and running malicious code within the container.

In the example, we created a new user using `RUN useradd europa`, switched to that user using `USER europa`, and set their home directory to `/home/europa` using `WORKDIR /home/europa`. Once we invoked `USER europa`, all subsequent commands ran as that user, meaning any files created would be owned by that user. Since we haven't granted this user sudo access, they cannot execute commands requiring sudo permissions.

 

Saving the Dockerfile in a subdirectory (`jupyter_example/Dockerfile`), we can build this as:
```
docker build ./jupyter_example -t obriens/part1-jupyter
```

Note how we've specified the location of the `Dockerfile` by passing the path to `./jupyter_example` instead of `.`. Once built, this image can be run as:
```
docker run --rm -it obriens/part1-jupyter
```

Initially, the Jupyter Lab server starts, but we cannot access it by navigating to `localhost/8000`. This is because we need to map ports from the container to our host system. If we stop the container and rerun it with port mapping:
```
docker run --rm -it -p 8000:8000 obriens/part1-jupyter
```

Now, we can navigate to localhost/8000 and see the Jupyter Lab server running!

If we shut down this container and launch a new one, we'll notice that the files created previously are no longer there. This happens because the `/home/europa` filesystem within the container is deleted when the container is deleted. To maintain persistence, we can mount a local directory at runtime using:
```
docker run --rm -it -p 8000:8000 -v $(pwd):/home/europa obriens/part1-jupyter
```
Here, the `-v` or `--volume` flag mounts `$(pwd)` (the current directory) on the host to `/home/europa` within the container, ensuring that files created or modified in `/home/europa` persist beyond the container's lifecycle.

### Permission errors, build arguments and entry points

It is possible that you still cannot save files to this directory. This might be because the `europa` user that we've created has a different user ID than the user who is running the Docker container.

To resolve this issue, we can use an "ARG" or argument within our Docker image. When creating the `europa` user, we can specify the user ID at build time. We can add the following lines to our `Dockerfile`:
```
...
# Create a new user and change to that user
ARG UID=1000
RUN useradd -m europa -u $UID
USER europa
...
```
This defines a new argument called `UID` with a default value of `1000`. The value of `UID` is then used when setting the ID of the europa user. When building the image, we can set this value to the ID of the current user with:
```
docker build  --build-arg UID=$(id -u) ./jupyter_example -t obriens/part1-jupyter
```
Here, `--build-arg UID=$(id -u)` sets the `UID` argument to the current user's ID (`$(id -u)`). This ensures that the user within the container has the same ID and permissions as the user who built the image.


```
docker run --rm -it -p 8000:8000 -v $(pwd):/home/europa:rw obriens/part1-jupyter
```

Note the `:rw` after the volume mounting. Similarly, we can restrict permissions when mounting using `:ro` to specify read-only. This can be useful when handling files or directories that we don't want the user to modify.

Using `--build-arg` allows us to specify arguments at build time, which may not always be practical if we don't know the parameters the user will set at runtime. For example, building an image that assumes a specific user ID (e.g., `1000`) might not suit another user with a different ID (e.g., `1001`).

To address this, we can refactor our image to use variables passed at runtime using an `ENTRYPOINT`. `ENTRYPOINT` defines a command or script that is executed upon starting the container, before the default command specified with `CMD` or using `docker run`. Consider the following script (`entrypoint.sh`):
```
#!/bin/bash

if [ -z "$UID" ] || [ $UID -eq 0 ]; then
    USER_ID=1000
else
    USER_ID=$UID
fi

# Create a new user with the specified UID
useradd -u $USER_ID -s /bin/bash europa

# Change ownership of the home directory
chown -R $USER_ID:$USER_ID /home/europa

# Switch to the new user and execute the command
exec gosu europa "$@"

```

This script sets the `USER_ID` parameter based on the `UID` passed at runtime (defaulting to `1000` if not specified or if `UID` is `0`). It then creates a new user `europa`, changes ownership of `/home/europa`, and switches to that user to execute further commands.


We can incorporate this script into our `Dockerfile`:
```
FROM python:3.9-slim

RUN apt-get update && apt-get install -y gosu && rm -rf /var/lib/apt/lists/*

# Use pip to install the requirements
RUN pip install numpy matplotlib jupyterlab notebook ipykernel ipython ipywidgets

# Create a new user and change to that user
ADD entrypoint.sh /home/europa/entrypoint.sh
RUN chmod +x /home/europa/entrypoint.sh

# # Move the europa's home directory
WORKDIR /home/europa

# Set the entrypoint
ENTRYPOINT [ "/home/europa/entrypoint.sh" ]


CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8000"]
```

This `Dockerfile` installs gosu, a utility for running commands as another user, and adds `entrypoint.sh`, making it executable. The `ENTRYPOINT` directive specifies the entry point script for the image.

```
RUN apt-get update && apt-get install -y gosu && rm -rf /var/lib/apt/lists/*
```
This command updates the OS and installs `gosu`, before cleaning up the install meta data.
```
ADD entrypoint.sh /home/europa/entrypoint.sh
RUN chmod +x /home/europa/entrypoint.sh
```
This command adds the `entrypoint.sh` to the home directory of some user `europa`.

```
# Set the entrypoint
ENTRYPOINT [ "/home/europa/entrypoint.sh" ]
```
This line specifies the entrypoint script for the image. 

Let's build and test the image:
```
docker build ./jupyter_example -t obriens/part1-jupyter 
> docker run --rm -it   obriens/part1-jupyter id

uid=1000(europa) gid=1000(europa) groups=1000(europa)
```

By default, the `europa` user's ID is set to `1000`. We can modify this at runtime using `-e` to specify a variable:
```
> docker run --rm -it  -e UID=1001  obriens/part1-jupyter id

uid=1001(europa) gid=1001(europa) groups=1001(europa)
```

It's best practice to avoid using the `root` user by default and to avoid hard-coding values like default user IDs. Using `--build-arg` and `ENTRYPOINT` provides flexibility at build and runtime, allowing Docker images to be configured dynamically based on user requirements.


### Container lifecycle: start, stop, remove

The above Jupyter server is an excellent example of a service that can run in the background. Let's launch the container and detach from it using:
```
docker run -d -it -p 8000:8000 -v $(pwd):/home/europa:rw --name jupyter obriens/part1-jupyter
```
Here's what each flag does:
- Removed the `--rm` flag to prevent the container from automatically deleting after exiting.
- Added `-d` to detach the running container, allowing it to run in the background.
- Specified a name using `--name jupyter` for easier identification and management.
    
If we navigate to `localhost:8000`, we'll notice that we need to log in to the server using a token. This token would have been printed as output if we hadn't used the `-d` flag. To retrieve the token, we can attach a new terminal to the running container:
```
docker exec -it jupyter bash
```
This command starts a new interactive bash shell within the `jupyter` container (`-it` ensures an interactive session). From here, we can get the login token for the Jupyter server using:
```
jupyter server list
Currently running servers:
http://8de969dd1385:8000/?token=84f69c1c8c61944fd6e322526db1c236457dc9b62fe15ffb :: /home/europa
```
Copy and paste the token (`84f69c1c8c61944fd6e322526db1c236457dc9b62fe15ffb` in this example) into your web browser to log in to the Jupyter server.
Once we're finished with the Jupyter server, we can stop it using:
```
docker stop jupyter
```
To restart it later, use:
```
docker start jupyter
```

Keeping regularly used containers set up and ready to run can be very useful. Some use case examples include:

* <b>Debugging tools</b>: Such as [Valgrind](https://valgrind.org/)  which can be challenging to install on Mac or Windows directly.
* <b>Analysis Pipelines</b>: Tools like [Heasoft](https://heasarc.gsfc.nasa.gov/docs/software/heasoft/docker.html) that allow running pipelines on locally stored data.
* <b>Specific Development Environments</b>: Such as legacy Python versions (e.g., Python 2) that may be difficult to compile on modern systems.

By managing containers effectively, developers can streamline their workflows and maintain consistent environments across different platforms and projects.

# Summary

In this workshop, we've covered the basics of Docker:

* Running pre-built images.
* Building custom images and understanding image layers to optimize development.
* Configuring containers that require networking and mapping ports between the host system and the container.
* Mounting volumes within containers and managing permissions to control file access.

In the next workshop, we will explore more advanced Docker features and dive into using Docker Compose to simplify managing and orchestrating Docker containers.
