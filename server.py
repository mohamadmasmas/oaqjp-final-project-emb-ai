from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_detector():
  
    text_to_analyze = request.args.get('textToAnalyze')

    if text_to_analyze is None or text_to_analyze == "":
        
        return "anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None.", 400
    else:

        response = emotion_detector(text_to_analyze)
        dominant_emotion = response.pop("dominant_emotion")
        response_text = str(response)[1:len(str(response))-1]

        formatted_text = "For the given statement, the system response is " + response_text + ". The dominant emotion is "+dominant_emotion
        
        return formatted_text

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)