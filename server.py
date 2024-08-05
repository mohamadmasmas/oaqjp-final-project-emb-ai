"""Module providing a web app to detect emotions."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_detector():
    """Function to implement the logic needed for the route."""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if "dominant_emotion" in response and response["dominant_emotion"] != "None":
        dominant_emotion = response.pop("dominant_emotion")
        response_text = str(response)[1:len(str(response))-1]

        formatted_text = "For the given statement, the system response is " + response_text + ". The dominant emotion is "+dominant_emotion
        return formatted_text, 200
    return "Invalid text! Please try again!", 400

@app.route("/")
def render_index_page():
    """Function to serve the home page."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
