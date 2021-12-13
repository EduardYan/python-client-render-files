"""
This module have the class Error
for to model of the a error.
"""

class Error:
  def __init__(self, content:str) -> None:
    if type(content) not in [str]:
      raise TypeError('The content must be a string.')

    self.content = content

  def __str__(self) -> str:
      return self.content