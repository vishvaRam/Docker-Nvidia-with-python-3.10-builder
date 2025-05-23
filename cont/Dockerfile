# Use NVIDIA CUDA base image with cuDNN
FROM   nvidia/cuda:12.6.2-cudnn-devel-ubuntu24.04

# Set environment variables to disable interactive prompts
ENV DEBIAN_FRONTEND=noninteractive \
    TZ=Etc/UTC

# Install Python 3.10 and pip
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
    python3.10 \
    python3.10-dev \
    python3.10-venv \
    python3-pip \
    python3-setuptools \
    python3-wheel \
    curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set Python 3.10 as the default
# Set Python 3.10 as the default
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1 && \
    ln -s /usr/bin/python3 /usr/bin/python  # <-- add this line

WORKDIR /app

COPY Code .

# Set default command
CMD ["python3","main.py"]
