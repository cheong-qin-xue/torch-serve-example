model_name=coreference
cd ${TS_ROOT}/${model_name}
extrafilelist=$(<filelist)
torch-model-archiver \
--model-name ${model_name} \
--version 1.0 \
--handler handler.py \
--requirements-file requirements.txt \
--config-file ts_model_config.yaml \
--extra-files "model_config.json,${extrafilelist}" \
--export-path ${TS_ROOT}/model_store
