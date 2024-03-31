"""Emotion Detector Flask application."""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/emotion_detector")
def emotion_analyzer():
    """Analyzes emotions from user-provided text and displays the results.

    Returns:
        A rendered template with the emotion analysis response or an error message.
    """

    text_to_analyze = request.args.get("text_to_analyze")

    try:
        emotion_result = emotion_detector(text_to_analyze)
    except ValueError as e:  # Catch potential value-related errors
        return f"Error: Invalid text format. {e}", 400

    anger = emotion_result.get("anger", 0.0)
    disgust = emotion_result.get("disgust", 0.0)
    fear = emotion_result.get("fear", 0.0)
    joy = emotion_result.get("joy", 0.0)
    sadness = emotion_result.get("sadness", 0.0)
    dominant_emotion = emotion_result.get("dominant_emotion")

    if dominant_emotion is None:
        return "Invalid text! Please try again", 400

    return_message = (
        f"For the given statement, the system response is: Anger: {anger:.2f}, "
        f"Disgust: {disgust:.2f}, Fear: {fear:.2f}, Joy: {joy:.2f}, Sadness: {sadness:.2f}. "
        f"Dominant Emotion: {dominant_emotion}"
    )

    return render_template("index.html", emotion_response=return_message)


@app.route("/")
def render_index_page():
    """Renders the main emotion detector webpage."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
