# function-concepts

To download the image, use `docker image pull joshuarchristie/function-concepts`.

To run, make sure your terminal working directory is in the local git respository folder `function-concepts/docker/` and type `docker run --rm -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes -v "$PWD":/home/jovyan/work <image_id>`.
This will save progress on the notebook (as you'll be working directly on the ipynb in your local git repository) and automatically remove the container after shutdown.
