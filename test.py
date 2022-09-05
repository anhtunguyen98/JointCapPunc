from nltk import word_tokenize
from pyvi import ViTokenizer
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained('anhtunguyen98/xlm-base-vi')

print(tokenizer.tokenize("ơibụng"))