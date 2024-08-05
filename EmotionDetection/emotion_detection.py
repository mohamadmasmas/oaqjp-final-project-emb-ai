import requests
import json

def emotion_detector(text_to_analyse):
    # URL of the emotion detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Custom header specifying the model ID for the emotion detection service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Sending a POST request to the emotion detector API
    response = requests.post(url, json=myobj, headers=header)

    # Parsing the response from the API
    formatted_response = response.text

    # Parsing the response to json from the API
    json_format = json.loads(formatted_response)
    # print(json_format)
    larger_value = 0
    emotions = {}

    # Defining the dominant emotion
    for emotion in json_format["emotionPredictions"][0]["emotion"]:
        if larger_value < json_format["emotionPredictions"][0]["emotion"][emotion]:
            larger_value = json_format["emotionPredictions"][0]["emotion"][emotion]
            dominant_emotion = emotion
        emotions[emotion] = json_format["emotionPredictions"][0]["emotion"][emotion]

    
    # print("The Dominant emotion is: "+ dominant_emotion, json_format["emotionPredictions"][0]["emotion"][dominant_emotion])
    emotions["dominant_emotion"] = dominant_emotion
    print("For the given statement, the system response is" + str(emotions)[1:len(str(emotions))-1]+ ". The dominant emotion is "+emotions["dominant_emotion"])
    return emotions

emotion_detector("I love football")