# Use NVIDIA CUDA base image with cuDNN
FROM nvidia/cuda:12.9.0-cudnn-devel-ubuntu24.04

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
    update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1 && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl -LsSf https://astral.sh/uv/install.sh  | sh && \
    cp $HOME/.local/bin/uv /usr/local/bin/uv && \
    cp $HOME/.local/bin/uvx /usr/local/bin/uvx

ENV PATH="/usr/local/bin:${PATH}"
ENV UV_LINK_MODE=copy

RUN uv --version

# RUN uv pip install -r requirements.txt --system
