FROM jupyter/minimal-notebook:latest

COPY function-concepts.ipynb /home/jovyan/work/
COPY process_sentence.py /home/jovyan/work/
RUN conda config --append channels conda-forge && \
    conda install --yes -c conda-forge spacy
RUN pip3 install scispacy && \
    pip3 install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.4.0/en_core_sci_scibert-0.4.0.tar.gz
RUN fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER
