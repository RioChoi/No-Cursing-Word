from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from transformers import TextClassificationPipeline, BertForSequenceClassification, AutoTokenizer

from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles

from typing import Optional
from pydantic import BaseModel
import json

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str

origins = [
    "http://localhost:4173",
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/assets", StaticFiles(directory="frontend/dist/assets"))

model_name = 'smilegate-ai/kor_unsmile'
model = BertForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

pipe = TextClassificationPipeline(
        model = model,
        tokenizer = tokenizer,
        device = -1,   # cpu: -1, gpu: gpu number
        return_all_scores = True,
        function_to_apply = 'sigmoid'
    )


@app.get("/")
def index():
    return FileResponse("frontend/dist/index.html")

@app.post("/getInfo")
def create_item(item: Item):
    jsonFormat = {
        "result": [],
        "word": []
        }
    final = []
    
    for result in pipe(item.description)[0]:
        jsonFormat["result"].append((result["label"], result["score"]))
        
    with open('dictionary/남성혐오.json', 'r', encoding='UTF-8-sig') as f:
        data = json.load(f)
        q = jsonFormat["result"][1][1]
    for i in data:
        tmp = str(item.description).find(i["단어"])
        if tmp != -1 and q > 0.07:
            final.append((tmp, i["태그"], i["단어"], i["설명"], i["용례"]))
    f.close()
            
    with open('dictionary/성소수자혐오.json', 'r', encoding='UTF-8-sig') as f:
        data = json.load(f)
        q = jsonFormat["result"][2][1]
    for i in data:
        tmp = str(item.description).find(i["단어"])
        if tmp != -1 and q > 0.07:
            final.append((tmp, i["태그"], i["단어"], i["설명"], i["용례"]))
    f.close()
    
    with open('dictionary/세대갈등.json', 'r', encoding='UTF-8-sig') as f:
        data = json.load(f)
        q = jsonFormat["result"][4][1]
    for i in data:
        tmp = str(item.description).find(i["단어"])
        if tmp != -1 and q > 0.07:
            final.append((tmp, i["태그"], i["단어"], i["설명"], i["용례"]))
    f.close()
    
    with open('dictionary/여성혐오.json', 'r', encoding='UTF-8-sig') as f:
        data = json.load(f)
        q = jsonFormat["result"][0][1]
    for i in data:
        tmp = str(item.description).find(i["단어"])
        if tmp != -1 and q > 0.07:
            final.append((tmp, i["태그"], i["단어"], i["설명"], i["용례"]))
    f.close()
    
    with open('dictionary/욕설.json', 'r', encoding='UTF-8-sig') as f:
        data = json.load(f)
        q = jsonFormat["result"][8][1]
    for i in data:
        tmp = str(item.description).find(i["단어"])
        if tmp != -1 and q > 0.07:
            final.append((tmp, i["태그"], i["단어"], i["설명"], i["용례"]))
    f.close()
    
    with open('dictionary/인종차별.json', 'r', encoding='UTF-8-sig') as f:
        data = json.load(f)
        q = jsonFormat["result"][3][1]
    for i in data:
        tmp = str(item.description).find(i["단어"])
        if tmp != -1 and q > 0.07:
            final.append((tmp, i["태그"], i["단어"], i["설명"], i["용례"]))
    f.close()
    
    with open('dictionary/종교갈등.json', 'r', encoding='UTF-8-sig') as f:
        data = json.load(f)
        q = jsonFormat["result"][6][1]
    for i in data:
        tmp = str(item.description).find(i["단어"])
        if tmp != -1 and q > 0.07:
            final.append((tmp, i["태그"], i["단어"], i["설명"], i["용례"]))
    f.close()
    
    with open('dictionary/지역감정.json', 'r', encoding='UTF-8-sig') as f:
        data = json.load(f)
        q = jsonFormat["result"][5][1]
    for i in data:
        tmp = str(item.description).find(i["단어"])
        if tmp != -1 and q > 0.07:
            final.append((tmp, i["태그"], i["단어"], i["설명"], i["용례"]))
    f.close()
            
    jsonFormat["word"] = final
        
    print(jsonFormat)
    return jsonFormat


