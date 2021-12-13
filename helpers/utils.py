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

def show_content_request(type_to_showed:str, output:str) -> None:
  """
  Show the content of the request passed
  for parameter.
  Show the key 'content' of the request.

  With the parameter type_to_showd you can pass this params:
    list_type_showed = ['get', 'normal']

  The show of the content change depending of this options.

  """

  list_type_showed = ['get', 'normal']

  if type_to_showed not in list_type_showed:
    raise TypeError('The optiion of the parameter type_to_showd, not is in the list')

  if type_to_showed in list_type_showed[1]:
    try:
      # getting the content of the request and converting in a string with json formating
      # content = output['content'] # this was a test for see this information
      content = dumps(output, indent = 4)
      print('\n--------------------- Content ----------------------------')
      print(content)
    
    except KeyError: # in case some problem
      print('Some problem with the key.')

  else:
    try:
      # getting the content of the requet sand converting in a string with json formating
      content = output
      content = dumps(output, indent = 4)
      print('\n--------------------- Content ----------------------------')
      print(content)
      
    except KeyError: # in case some problem
      print('Some problem with the key.')