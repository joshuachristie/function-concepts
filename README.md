# Concepts of function in biology and biomedicine

This repository contains all the data for the paper "Concepts of function in biology and biomedicine".

The manuscript can be found [here](https://github.com/joshuachristie/function-concepts/raw/master/manuscript/concepts_function.pdf).

The instruction handbook for the natural language analysis can be found [here](https://joshuachristie.github.io/function-concepts/function-concepts-handbook.html).

We have used the natural language analysis to analyes the 42 examples from [Keeling et. al. (2019)](https://elifesciences.org/articles/47014), which can be found [here](https://joshuachristie.github.io/function-concepts/examples_Keeling_et_al_2019.html).

# Running the natural language analysis software

You can also run the code used the generate the handbook and examples (or to analyse your own sentences).

The first step is to clone the repository.
You then have two options to set up the environment for running the natural language software.

## Docker

The recommended way is to run it through Docker (especially if you are running MacOS or Windows). If you don't have docker installed, you can get it [here](https://www.docker.com/get-started).

To download the image, use `docker image pull joshuarchristie/function-concepts`.

To run the juptyer notebooks, make sure your terminal working directory is in the local git respository folder `function-concepts/natural_language_analysis/`.

Run a container using the following command:

`docker run --rm -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes -v "$PWD":/home/jovyan/work <image_id>` (replace `<image_id>` with the ID of the docker image).

This will save progress on the notebooks (as you'll be working directly on the ipynb in your local git repository) and automatically remove the container after shutdown.

## Using a python environment manager ([conda](https://docs.conda.io/en/latest/), etc.)

You can also try setting up your own environments using the [requirements.txt](https://github.com/joshuachristie/function-concepts/blob/master/requirements.txt) file (`pip3 install -r requirements.txt`). This isn't recommended as it has only been tested on my local machine (using conda/pip on a derivative of ubuntu). You can also set up an environment step-by-step by installing the following packages and models:
- [spacy](https://spacy.io/usage)
- [scispacy](https://allenai.github.io/scispacy/)
- [jupyterlab](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html)
- [scibert model (scispacy)](https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.4.0/en_core_sci_scibert-0.4.0.tar.gz)
