from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionAnalyzer(unittest.TestCase):
    def test_emotion_analyzer(self):
       result_1 = emotion_detector("I am happy this happened")
        # Extract the emotion name from the tuple
       dominant_emotion_name_1 = result_1['dominant_emotion'][0]
       self.assertEqual(dominant_emotion_name_1, 'joy')

       result_2 = emotion_detector("I am really mad about this")
       dominant_emotion_name_2 = result_2['dominant_emotion'][0]
       self.assertEqual(dominant_emotion_name_2, 'anger')

       result_3 = emotion_detector("I feel disgusted just hearing about this")
       dominant_emotion_name_3 = result_3['dominant_emotion'][0]
       self.assertEqual(dominant_emotion_name_3, 'disgust')
 
       result_4 = emotion_detector("I am so sad about this")
       dominant_emotion_name_4 = result_4['dominant_emotion'][0]
       self.assertEqual(dominant_emotion_name_4, 'sadness')

       result_5 = emotion_detector("I am really afraid that this will happen")
       dominant_emotion_name_5 = result_5['dominant_emotion'][0]
       self.assertEqual(dominant_emotion_name_5, 'fear')
unittest.main()     