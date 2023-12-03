from transformers import BertTokenizer, TFBertForSequenceClassification
from transformers import pipeline

finbert = TFBertForSequenceClassification.from_pretrained('yiyanghkust/finbert-tone',num_labels=3)
tokenizer = BertTokenizer.from_pretrained('yiyanghkust/finbert-tone')

nlp = pipeline("sentiment-analysis", model=finbert, tokenizer=tokenizer)

sentences = ["What is not to like about this product."]  
#              "growth is strong and we have plenty of liquidity", 
#              "there are doubts about our finances", 
#              "profits are flat"]
results = nlp(sentences)
print(results)  #LABEL_0: neutral; LABEL_1: positive; LABEL_2: negative
