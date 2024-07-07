from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

# model_name = "cardiffnlp/twitter-roberta-base-sentiment-latest"
model_name = "lxyuan/distilbert-base-multilingual-cased-sentiments-student"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

app = FastAPI()

class RequestModel(BaseModel):
    input:str

@app.post("/sentiment")
def get_response(request: RequestModel):
    prompt = request.input
    response = classifier(prompt)
    label = response[0]["label"]
    score = response[0] ["score"]
    return f"The '{prompt}' input is {label} with a score of {score}"
# print(get_response("This tutorial is great!"))

