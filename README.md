# <img src="./docs/img//azure_logo.png" alt="Azure Logo" style="width:30px;height:30px;"/> Master quantization with llama.cpp in Azure Machine Learning

This project showcases how to efficiently compress large language models using llama.cpp. By applying quantization, you can drastically reduce the model's memory footprint without sacrificing performance. Follow the steps below to set up dependencies, run the quantization process, and confirm that the smaller model meets your requirements.

Use llama.cpp to reduce model size while keeping performance intact:
1. Obtain your base model and place it in the correct directory.
2. Install all dependencies from the environment file.
3. Run the quantization script to produce a smaller, optimized model.
4. Test the quantized model with the provided inference commands.

Quantization will significantly lower memory usage and simplify deployment scenarios.

## Features

* Demonstrates using llama.cpp for model quantization in Azure Machine Learning  
* Reduces model memory footprint while maintaining performance  
* Integrates CMake-based build processes for streamlined compilation  
* Showcases environment setup with conda for rapid development  
* Provides example Makefile for quick project setup and deployment  


## Quickstart

### Clone the Repository

To get started, clone the repository:

```sh
git clone https://github.com/Azure-Samples/gbbai-quantization-llm-llamacpp.git
```


And then:

1. Update the package list:
    ```bash
    sudo apt update
    ```

2. Install GCC 11:
    ```bash
    sudo apt install gcc-11
    ```

3. Register GCC 11 as an alternative with a priority of 60:
    ```bash
    sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-11 60
    ```

4. Select the default GCC version:
    ```bash
    sudo update-alternatives --config gcc
    ```

This sequence ensures your system uses GCC 11 as the default compiler.


## Prerequisites
+ [azd](https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd), used to deploy all Azure resources and assets used in this sample.

+ [PowerShell Core pwsh](https://github.com/PowerShell/powershell/releases) if using Windows

+ Python 3.11

+ To build and compile this project, you need to have CMake installed. CMake is an open-source, cross-platform family of tools designed to build, test, and package software. You can download and install CMake from [here](https://cmake.org/download/).

- Follow the instructions on the CMake download page to install the appropriate version for your operating system.
- Ensure that CMake is added to your system's PATH to easily run it from the command line.

## Instalation 
The Makefile is designed to set up a Python development environment using pyenv, conda, and poetry. Here's a step-by-step explanation of what each part does:

To run the Makefile included in this project, follow these steps:

1. Open a terminal and navigate to the project directory:
    ```sh
    fgbbai-quantization-llm-llamacpp
    ```

2. Run the Makefile using the `make` command:
    ```sh
    make <target>
    ```

This will execute the default target specified in the Makefile. If you want to run a specific target, use:
Replace `<target>` with the name of the target you want to run.

This uses `condaenv` instead of `poetryenv` because Azure Machine Learning is built with `conda` and it can be easier to use when running code within Azure Machine Learning notebooks. If you are using VS Code and linking to the proper compute, you can modify the Makefile to use the `poetry` environment, or keep it as is, both will work properly.

**You can set up your environment by following the steps below:**


### Setup environment

This sample uses [`azd`](https://learn.microsoft.com/azure/developer/azure-developer-cli/) and a bicep template to deploy all Azure resources, including the Azure OpenAI models.

1. Login to your Azure account: `azd auth login`

2. Create an environment: `azd env new`

3. Run `azd up`.

   + Choose a name for your resourge group.
   + Enter a region for the resources.

   The deployment creates multiple Azure resources and runs multiple jobs. It takes several minutes to complete. The deployment is complete when you get a command line notification stating "SUCCESS: Your up workflow to provision and deploy to Azure completed."


### Build the Project

Before running build_project, install and configure GCC 11 on Ubuntu:

```bash
sudo apt update
sudo apt install gcc-11
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-11 60
sudo update-alternatives --config gcc
```

To build the project, follow these steps:

1. **Set Up Your Compiler**

    Clone the repo 

    ```sh
    clone_repo() -> example existant in quantization_llama_drom_fine_tune.ipynb notebook
    ```

    Use the following CMake command to set up your compiler:

    ```sh
    cmake -DCMAKE_CXX_COMPILER=/path/to/g++ -DCMAKE_C_COMPILER=/path/to/gcc /path/to/source
    ```

    Alternatively, you can set the compiler paths in the `CMakeLists.txt` file before the `project` command:

    ```cmake
    set CMAKE_GENERATOR=MinGW Makefiles
    set(CMAKE_CXX_COMPILER "C:/mingw64/bin/g++.exe")
    set(CMAKE_C_COMPILER "C:/mingw64/bin/gcc.exe")
    ```

    Replace `/path/to/g++`, `/path/to/gcc`, and `/path/to/source` with the appropriate paths on your system or add them to your system environment variables.

    You will also need `nmake`, an executable used by Windows machines to execute a Makefile.

    If you have a Windows machine, there are two options:

    1. Use the `nmake` alternative `mingw` by adding this command to your script file:
            ```sh
            cmake -S . -B build -G "MinGW Makefiles"
            ```

    2. Perform a web search for "Visual Studio Build Tools". Microsoft releases a command line build tools package as an alternative to the larger software downloads such as Visual Studio.


2. **Build the Project**

    After correctly configuring the variables, run the following command to build the project:

    ```sh
    build_project()
    ```

    This will compile the source code and generate the necessary binaries.


For faster build performance, refer to the official llama.cpp documentation at:
https://github.com/ggerganov/llama.cpp/blob/master/docs/build.md

## Demo

See more in quantization_llama_fine_tune jupyter notebook


