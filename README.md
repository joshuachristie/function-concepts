# Concepts of function in biology and biomedicine

# Running the natural language analysis software

The first step is to clone the repository. You then have two options to set up the environment for

## Docker

The recommended way is to run it through Docker (especially if you are running MacOS or Windows). If you don't have docker installed, you can get it [here](https://www.docker.com/get-started).

To download the image, use `docker image pull joshuarchristie/function-concepts`.

To run the juptyer notebooks, make sure your terminal working directory is in the local git respository folder `function-concepts/natural_language_analysis/` and type `docker run --rm -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes -v "$PWD":/home/jovyan/work <image_id>` (replace `<image_id>` with the ID of the docker image).
This will save progress on the notebook (as you'll be working directly on the ipynb in your local git repository) and automatically remove the container after shutdown.

## conda (or other python environment manager)

You can also try setting up your own environments using the [requirements.txt](https://github.com/joshuachristie/function-concepts/blob/master/requirements.txt) file (`pip3 install -r requirements.txt`). This isn't recommended as it has only been tested on my local machine (which runs a derivative of ubuntu). If this doesn't work, you can try manually setting up an environment by installing the following:
- spacy
- scispacy
- jupyterlab
- https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.4.0/en_core_sci_scibert-0.4.0.tar.gz
