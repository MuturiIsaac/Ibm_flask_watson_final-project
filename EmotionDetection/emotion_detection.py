import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    status_code = response.status_code
   

    emotions = {}
    
    if status_code == 200:
        response_dict = json.loads(response.text)
        emotions = response_dict ['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotions.items(), key=lambda x: x[1])
        emotions['dominant_emotion'] = dominant_emotion[0]
        
    elif status_code == 400:
        emotions['anger'] = None
        emotions['disgust'] = None
        emotions['fear'] = None
        emotions['joy'] = None
        emotions['sadness'] = None
        emotions['dominant_emotion'] = None

    return emotions