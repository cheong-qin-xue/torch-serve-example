from ts.torch_handler.base_handler import BaseHandler
from fastcoref import LingMessCoref
import torch
from typing import List
import json

class CorefHandler(BaseHandler):

    def __init__(self):
        self._context = None
        self.initialized = False
        self.explain = False
        self.target = 0

    def initialize(self, context):
        self._context = context
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.model = LingMessCoref(model_name_or_path='.', device=self.device)
        with open('model_config.json') as f:
            self.config = json.load(f)
        self.max_tokens_in_batch = self.config.get('max_tokens_in_batch', 256)
        self.initialized = True

    def preprocess(self, data:list):
        text_batch = []
        for data_ in data:
            input_text = data_.get('data')
            if input_text is None:
                input_text = data_.get('body')
            if isinstance(input_text, (bytes, bytearray)):
                input_text = input_text.decode('utf-8')
        
            text_batch.append(input_text)

        return text_batch

    def inference(self, text_batch:List[str]):
        model_output = self.model.predict(
            text_batch,
            max_tokens_in_batch = self.max_tokens_in_batch
        )
        return [x.get_clusters(as_strings=False) for x in model_output]

    def postprocess(self, inference_output):
        """
        Return inference result.
        :param inference_output: list of inference output
        :return: list of predict results
        """
        # Take output from network and post-process to desired format
        postprocess_output = inference_output
        return postprocess_output