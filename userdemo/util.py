import pickle

__author__ = '01210367'

class FeedbackMessage:

  def __init__(self, feedbackFlag, feedbackCode, feedbackMessage):
      self.feedbackFlag =feedbackFlag
      self.feedbackCode = feedbackCode
      self.feedbackMessage = feedbackMessage

  def dict(self):
      dictdate = {
         'feedbackFlag':self.feedbackFlag,
         'feedbackCode':self.feedbackCode,
         'feedbackMessage':self.feedbackMessage
         }
      return {
          'feedback':dictdate
      }
