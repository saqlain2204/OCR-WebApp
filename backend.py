import torch
from PIL import Image
from transformers import AutoModel, AutoTokenizer

class OCRUsingGOT:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained('ucaslcl/GOT-OCR2_0', trust_remote_code=True)
        self.model = AutoModel.from_pretrained('ucaslcl/GOT-OCR2_0', trust_remote_code=True,
                               device_map = 'cuda', use_safetensors=True,
                               pad_token_id = self.tokenizer.eos_token_id)
        self.model.eval().cuda()

    def extract_text(self, image):



        extracted_text = ''
        with torch.no_grad():
            extracted_text = self.model.chat(self.tokenizer, image, ocr_type = 'ocr')

        return extracted_text
