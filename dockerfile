FROM pytorch/torchserve:0.9.0-gpu

ENV MODELS="/models"
ENV TS_ROOT="/src"

COPY src ${TS_ROOT}
RUN mkdir ${TS_ROOT}/model_store
RUN python ${TS_ROOT}/setup.sh

WORKDIR ${TS_ROOT}
CMD ["/bin/bash","run.sh"]