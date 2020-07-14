FROM jupyter/minimal-notebook:latest

COPY jupyter_spacy.ipynb /home/jovyan/work/
COPY process_sentence.py /home/jovyan/work/
RUN conda config --append channels conda-forge && \
    conda install --yes -c conda-forge spacy
RUN pip3 install scispacy && \
    pip3 install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.2.5/en_core_sci_lg-0.2.5.tar.gz 
RUN fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER
