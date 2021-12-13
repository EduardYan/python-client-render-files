"""
This module have somes functions
for make things utils.
"""

from os import environ
from json import dumps

def get_user_name() -> str:
  """
  Return the user of the current user.
  """

  # getting the current user for return
  current_user = environ['USER']
  return current_user

def ask_save_output() -> bool:
  """
  Return True if the value
  in the input is yes, else return no.
  """

  # getting and validating
  answer = input('You want save the output (yes, no) ? > ')
  if answer == 'yes' or answer == 'yes ':
    return True

  return False

def show_content_request(is_get:bool, output:str) -> None:
  """
  Show the content of the request passed
  for parameter.

  """

  if not is_get:
    # getting the content of the request and converting in a string with json formating
    content = output['content']
    print('\n---------------------- Content ----------------------------')
    print(content)
    print('\n---------------------- Info ------------------------------')
    print(f"Id file -> {output['id']}")
    print(f"Path File -> {output['path']}")

  else:
    content = dumps(output, indent = 4)
    print('\n---------------------- Content ----------------------------')
    print(content)