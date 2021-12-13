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

def show_content_request(type_to_show:str, output:str) -> None:
  """
  Show the content of the request passed
  for parameter.

  If the parameter type_to_show is 'get-file', show your key content
  with some formating.

  If not, show the request without formating.

  """

  if type(type_to_show) not in [str]:
    raise TypeError('The parameter type_to_show must be a string.')

  if type_to_show == 'get-file':
    # getting the content of the request and converting in a string with json formating
    content = dumps(output['content'], indent = 4)
    print('\n---------------------- Content ----------------------------')
    print(content)
    print('\n---------------------- Info ------------------------------')
    print(f"Id file -> {output['id']}")
    print(f"Path File -> {output['path']}")

  else: # in case be other
    content = dumps(output, indent = 4)
    print('\n---------------------- Content ----------------------------')
    print(content)