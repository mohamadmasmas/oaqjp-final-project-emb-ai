from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

@app.route("/emotionDetector")
def sent_detector():
  
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)
    
    formatted_text = "For the given statement, the system response is" + str(response)[1:len(str(response))-1]+ ". The dominant emotion is "+response["dominant_emotion"]
    print("For the given statement, the system response is" + str(response)[1:len(str(response))-1]+ ". The dominant emotion is "+response["dominant_emotion"])

    # Return a formatted string with the sentiment label and score
    return formatted_text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)