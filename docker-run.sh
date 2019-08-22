#!/bin/bash
docker run --rm --name python-school -v `pwd`:/python-school -it python-school:dev /bin/sh