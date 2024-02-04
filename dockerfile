FROM pytorch/torchserve:0.8.2-gpu
USER root
ENV MODELS="/models"
ENV TS_ROOT="/src"

COPY src/requirements.txt .
RUN pip install -r requirements.txt

COPY src ${TS_ROOT}
RUN mkdir ${TS_ROOT}/model_store
RUN /bin/bash ${TS_ROOT}/setup.sh

WORKDIR ${TS_ROOT}

USER model-server
EXPOSE 8080
CMD ["/bin/bash","run.sh"]