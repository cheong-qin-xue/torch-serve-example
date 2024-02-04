from transformers import AutoModel, Autotokenizer
import os

models = {
    'coreference':'biu-nlp/lingmess-coref'
}

for modelname, modelhubpath in models.items():
    model_dir = os.path.join(os.environ['MODELS'], modelname)
    os.makedirs(model_dir)
    model = AutoModel.from_pretrained(modelhubpath)
    tokenizer = Autotokenizer.from_pretrained(modelhubpath)
    filelist = model.save_pretrained(model_dir) + tokenizer.save_pretrained(model_dir)
    outputfile = os.path.join(
        os.environ['TS_ROOT'],
        modelname,
        'filelist'
    )
    with open(outputfile, 'w') as f:
        f.write(outputfile)