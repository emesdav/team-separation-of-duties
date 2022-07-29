import re

"""
The purpose of this file is to ensure that every input is validated
as expected input and not just a random entry.

We may want to do more than just checking what instance is sent
"""

class Validate:

  def __init__(self, value):
    #TODO: lets sanitize the value here
    self.value = value

  #Validate input to be an integer
  def IfInt(self):
    if self.value is not None: #Since this is showing up in all queries, is it posible to add it to the constructor?
      return isinstance(self.value, int)

  #Validate input to be an String
  def IfString(self):
    if self.value is not None:
      return isinstance(self.value, str)

  #Validate input to be an Float
  def IfFloat(self):
    if self.value is not None:
      return isinstance(self.value, float)

  #Validate input to be an email
  def IfEmail(self):
    if self.value is not None:
      #We build a regex pattern to match the expected email format
      emailPattern = r'\b[A-Za-z0-9._-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
      #re.fullmatch would normaly return None in place of false and we want an actual bool
      #so we check if None we return false else true
      checkEmailFormat = False if re.fullmatch(emailPattern, self.value) == None else True
      return checkEmailFormat
