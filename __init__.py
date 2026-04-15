# EmotionDetection/__init__.py
# This file makes the EmotionDetection folder a Python package
# It imports the main function so we can use: from EmotionDetection.emotion_detection import emotion_detector

from .emotion_detection import emotion_detector

__all__ = ['emotion_detector']
