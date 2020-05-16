FROM ubuntu:bionic-20200403
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update

RUN apt install -y git wget nano cmake software-properties-common libprotobuf-dev libleveldb-dev liblmdb-dev libsnappy-dev libopencv-dev libhdf5-serial-dev protobuf-compiler libatlas-base-dev libgflags-dev libgoogle-glog-dev
RUN apt install -y --no-install-recommends libboost-all-dev

RUN apt install -y python-pip
RUN pip install numpy scikit-image scipy lmdb opencv-python protobuf

ENV PHOCNET_DIR=/opt/phocnet
ENV PHOCNET_INSTALL_DIR=/opt/install/phocnet
COPY . $PHOCNET_DIR
RUN mkdir -p $PHOCNET_INSTALL_DIR
WORKDIR $PHOCNET_DIR
RUN mkdir build ; cd build
RUN python install.py --install-dir $PHOCNET_INSTALL_DIR

RUN mv $PHOCNET_DIR/phocnet_gw_cv1.binaryproto examples
WORKDIR $PHOCNET_DIR/examples
ENV LD_BINARY_PATH=$PHOCNET_INSTALL_DIR/caffe/lib
ENV PYTHONPATH=$PYTHONPATH:/opt/phocnet/caffe/python
CMD ["python", "prediction_example.py"]
