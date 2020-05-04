# Run example in Docker

Download the [George Washington CV 1 proto](http://patrec.cs.tu-dortmund.de/files/cnns/phocnet_gw_cv1.binaryproto) to the root. Then:

```
docker build .
docker run $DOCKER_IMAGE_ID
```

# Run prediction in Docker

To play with the model and perhaps apply it to other data, it's possible to enter the container you just created with: 

```
docker run -it --mount type=bind,source=/home/${USER}/eval_data,target=/eval --entrypoint=/bin/bash $DOCKER_IMAGE_ID -i
```

Inside the container, run a prediction with the following command.

```
PYTHONPATH=$PYTHONPATH:/opt/phocnet/caffe/python:/opt/install/phocnet/lib/python2.7/site-packages:/usr/local/lib/python2.7/dist-packages python tools/predict_phocs.py --img_dir /eval --pretrained_phocnet examples/phocnet_gw_cv1.binaryproto --deploy_proto examples/deploy_phocnet.prototxt
```
