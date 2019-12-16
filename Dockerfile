FROM python:3-alpine

WORKDIR /python-school

RUN apk update && apk add build-base
RUN pip install --upgrade pip wheel

# pillow
RUN apk update && apk add \
    libjpeg-turbo-dev \
    zlib-dev \
    tiff-dev \
    freetype-dev \
    lcms-dev \
    libwebp-dev \
    tcl-dev \
    tk-dev \
    openjpeg-dev \
    openblas \ 
    openblas-dev
    # python3-tkinter
    # libimagequant
    # libraqm

RUN pip install \
    numpy \
    pandas \
    Pillow \
    scipy \
    cython \
    scikit-learn \
    matplotlib

RUN pip install mypy

RUN apk add python3-tkinter

# Argument to python command
CMD ["python", "main.py"]