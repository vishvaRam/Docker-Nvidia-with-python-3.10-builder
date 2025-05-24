# Docker NVIDIA CUDA Development Environment

This repository contains Docker configurations for NVIDIA CUDA development environments with different CUDA versions and Ubuntu distributions. These images are designed to provide a consistent development environment for GPU-accelerated applications.

## Available Images

The following Docker images are available in the [vishva123](https://github.com/vishva123) namespace:

| Image Name | CUDA Version | Ubuntu Version | Python Version | Status |
|------------|--------------|----------------|----------------|---------|
| nvdia-cuda-12.9-cudnn-ubuntu24.04-py-3.10-uv | 12.9 | Ubuntu 24.04 | 3.10 | Active |
| nvdia-cuda-12.8-cudnn-ubuntu24.04-py-3.10-uv | 12.8 | Ubuntu 24.04 | 3.10 | Active |
| nvdia-cuda-12.6-cudnn-ubuntu24.04-py-3.10-uv | 12.6 | Ubuntu 24.04 | 3.10 | Active |
| nvdia-cuda-12.4-cudnn-ubuntu22.04-py-3.10-uv | 12.4 | Ubuntu 22.04 | 3.10 | Active |
| nvdia-cuda-12.1-cudnn-ubuntu20.04-py-3.10-uv | 12.1 | Ubuntu 20.04 | 3.10 | Active |

## Features

- NVIDIA CUDA support with different versions (12.1, 12.4, 12.6, 12.8, 12.9)
- cuDNN integration
- Python 3.10 environment
- UV package manager
- GPU acceleration support
- Ubuntu LTS versions (20.04, 22.04, 24.04)

## Prerequisites

- Docker installed on your system
- NVIDIA Container Toolkit installed
- NVIDIA GPU with compatible drivers

## Usage

1. Pull the desired image:
```bash
docker pull vishva123/nvdia-cuda-12.9-cudnn-ubuntu24.04-py-3.10-uv
```

2. Run the container:
```bash
docker run --gpus all -it vishva123/nvdia-cuda-12.9-cudnn-ubuntu24.04-py-3.10-uv
```

## Docker Compose

You can also use the provided `docker-compose.yml` file to run the container:

```bash
docker-compose up
```

The compose file includes:
- GPU device mapping
- Volume mounting
- DNS configuration
- Environment variables for NVIDIA GPU access

## Building from Source

To build the Docker image locally:

1. Clone this repository
2. Navigate to the project directory
3. Run:
```bash
docker build -t nvidia-cuda-dev ./Code
```

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

For any questions or issues, please open an issue in the GitHub repository. 