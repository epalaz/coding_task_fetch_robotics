# Path Finder Server - Wall-e Finds Eve

[![Build Status](https://travis-ci.com/epalaz/coding_task_fetch_robotics.svg?token=yrJg7DrmypRwQrmBPZVW&branch=master)](https://travis-ci.com/epalaz/coding_task_fetch_robotics)

### Overview
This webserver implements a path finder based on the coding challenge available [here](https://github.com/calvinfeng/walle_finds_eve).

### Installation and Running
#####1. By using Docker Image
```console
docker pull epalaz/path_finder_server
```
```console
docker run -p 3000:3000 epalaz/path_finder_server:1.0
```

Any web request library can be siued to send requests and receive returns in the form shown in the coding challenge documentation.

#####2. Cloning the Repository
```console
git clone https://github.com/epalaz/coding_task_fetch_robotics.git
cd coding_task_fetch_robotics/
pip install -r requirements.txt
``` 
Using a virtual python environemtn tool is suggested either [**pyenv**](https://github.com/pyenv/pyenv) or [**virtualenv**](https://virtualenv.pypa.io/en/latest/).
This application is developed in Python Version 3.7.2, using this version is suggested for best compatibility.
```console
python app.py
``` 
This command starts webserver on the port 3000.

### Testing

```console
cd coding_task_fetch_robotics/
python -m unittest classes.class_tests -v
``` 