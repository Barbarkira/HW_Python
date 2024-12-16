from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import torch

class PipeAnalyzer:
    def __init__(self):
        self.semantic_tokenizer = AutoTokenizer.from_pretrained("MonoHime/rubert-base-cased-sentiment-new")
        self.semantic_model = AutoModelForSequenceClassification.from_pretrained("MonoHime/rubert-base-cased-sentiment-new")

        self.topic_model = pipeline("zero-shot-classification", model="MoritzLaurer/mDeBERTa-v3-base-mnli-xnli")

    def semantic_pipe(self, news_text):
        labels = ["Neutral", "Positive", "Negative"]
        inputs = self.semantic_tokenizer(news_text, padding=True, return_tensors="pt")

        with torch.no_grad():
            outputs = self.semantic_model(**inputs)

        predicted_class = torch.argmax(outputs.logits).item()
        return labels[predicted_class]

    def topic_pipe(self,news_text):
        candidate_labels = ["экономика", "политика", "спорт", "технологии", "культура"]
        output = self.topic_model(news_text, candidate_labels, multi_label=False)


        return output['labels'][0]