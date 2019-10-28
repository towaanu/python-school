xhost +

ip=`ifconfig en0 | grep inet | awk '$1=="inet" {print $2}'`

# docker run \
#     -e DISPLAY=$ip:0 \
#     -v /tmp/.X11-unix:/tmp/.X11-unix \
#     -v `pwd`/meiro:/meiro \
#     meiro:dev

docker run \
    --rm \
    -e DISPLAY=$ip:0 \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    --name python-school \
    -v `pwd`:/python-school \
    -it python-school:dev /bin/sh
    