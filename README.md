# Project Name

(short, 1-3 sentenced, description of the project)

## Features

This project framework provides the following features:

* Feature 1
* Feature 2
* ...

## Getting Started

### Prerequisites

(ideally very short, if any)

- OS
- Library version
- ...


### Prerequisites
To build and compile this project, you need to have CMake installed. CMake is an open-source, cross-platform family of tools designed to build, test, and package software. You can download and install CMake from [here](https://cmake.org/download/).

- Follow the instructions on the CMake download page to install the appropriate version for your operating system.
- Ensure that CMake is added to your system's PATH to easily run it from the command line.


### Setup Your Compiler


### Clone the Repository

To get started, clone the repository:

```sh
git clone https://github.com/Azure-Samples/gbbai-quantization-llm-llamacpp.git
```

### Build the Project

To build the project, follow these steps:

1. **Set Up Your Compiler**

    Clone the repo 

    ```sh
    clone_repo()
    ```

    Use the following CMake command to set up your compiler:

    ```sh
    cmake -DCMAKE_CXX_COMPILER=/path/to/g++ -DCMAKE_C_COMPILER=/path/to/gcc /path/to/source
    ```

    Alternatively, you can set the compiler paths in the `CMakeLists.txt` file before the `project` command:

    ```cmake
    set(CMAKE_CXX_COMPILER "C:/mingw64/bin/g++.exe")
    set(CMAKE_C_COMPILER "C:/mingw64/bin/gcc.exe")
    ```

    Replace `/path/to/g++`, `/path/to/gcc`, and `/path/to/source` with the appropriate paths on your system or add them to your system environment variables.

2. **Windows Specific Instructions**

    If you are using a Windows machine, you have two options:

    - Use the `nmake` alternative `mingw` by adding this command to your script file:

      ```sh
      cmake -S . -B build -G "MinGW Makefiles"
      ```

    - set CMAKE_GENERATOR=MinGW Makefiles as virtual env

3. **Build the Project**

    After correctly configuring the variables, run the following command to build the project:

    ```sh
    build_project()
    ```

    This will compile the source code and generate the necessary binaries.



#### To set up your compiler, use the following CMake command:

Clone the repo 

```sh
clone_repo()
build_project() .
```
and then

```sh
cmake -DCMAKE_CXX_COMPILER=/path/to/g++ -DCMAKE_C_COMPILER=/path/to/gcc /path/to/source 

```

or set it in CMakeList.txt before project:

Example:
set CMAKE_GENERATOR=MinGW Makefiles
set(CMAKE_CXX_COMPILER "C:/mingw64/bin/g++.exe")
set(CMAKE_C_COMPILER "C:/mingw64/bin/gcc.exe")


#### Replace

 `/path/to/g++`, `/path/to/gcc`, and `/path/to/source` with the appropriate paths on your system or add it to system env.

You will also need `nmake`, an executable used by Windows machines to execute a Makefile.

If you have a Windows machine, there are two options:

1. Use the `nmake` alternative `mingw` by adding this command to your script file:
    ```sh
    -G "MinGW Makefiles" after "cmake -S . -B build"
    ```

2. Perform a web search for "Visual Studio Build Tools". Microsoft releases a command line build tools package as an alternative to the larger software downloads such as Visual Studio.


#### After correctly configuring the variables, run the following command to build the project:

```sh
build_project() .
```

This will compile the source code and generate the necessary binaries.


## Quickstart

```bash
git clone https://github.com/Azure-Samples/gbbai-quantization-llm-llamacpp.git
```

### Instalation 
The Makefile is designed to set up a Python development environment using pyenv, conda, and poetry. Here's a step-by-step explanation of what each part does:

To run the Makefile included in this project, follow these steps:

1. Open a terminal and navigate to the project directory:
    ```sh
    fine-tuning-open-source-text-generation
    ```

2. Run the Makefile using the `make` command:
    ```sh
    make <target>
    ```

This will execute the default target specified in the Makefile. If you want to run a specific target, use:
Replace `<target>` with the name of the target you want to run.

This uses `condaenv` instead of `poetryenv` because Azure Machine Learning is built with `conda` and it can be easier to use when running code within Azure Machine Learning notebooks. If you are using VS Code and linking to the proper compute, you can modify the Makefile to use the `poetry` environment, or keep it as is, both will work properly.

## Demo

A demo app is included to show how to use the project.

To run the demo, follow these steps:

(Add steps to start up the demo)

1.
2.
3.

## Resources

(Any additional resources or related projects)

- Link to supporting information
- Link to similar sample
- ...
