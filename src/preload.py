from transformers import AutoModel, AutoTokenizer
import os

models = {
    'coreference':'biu-nlp/lingmess-coref'
}

for modelname, modelhubpath in models.items():
    model_dir = os.path.join(os.environ['MODELS'], modelname)
    os.makedirs(model_dir)
    model = AutoModel.from_pretrained(modelhubpath)
    tokenizer = AutoTokenizer.from_pretrained(modelhubpath)
    model.save_pretrained(model_dir)
    tokenizer.save_pretrained(model_dir)
    filelist = [os.path.join(model_dir, f) for f in os.listdir(model_dir) if os.path.isfile(f)]
    outputfile = os.path.join(
        os.environ['TS_ROOT'],
        modelname,
        'filelist'
    )
    with open(outputfile, 'w') as f:
        f.write(outputfile)