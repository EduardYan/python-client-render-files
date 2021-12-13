"""
This module have varibales with documentation
for show in the commands.
"""

# doc of each method
GET_DOC = '\nGET ---------------> With this method, your can get alls the file allows in the server files. With extra information.'

GET_FILE_DOC = '\nGET-FILE ---------------> With this method, your can get the file pass your id. When to save the file, the file save the key content. And getting the file content.'

POST_DOC = '\nPOST ---------------> With this method, your can send data at the server. Sample: /home/user/Pictures/tree.png. For save and allow that file in the server. Verifiy if the file exist in the server for not get a error.'

PUT_DOC = '\nPUT ----------------> With this method, your can upadate the path of a file in the server. Pass your id, and the new path.'

DELETE_DOC = '\nDELETE ---------------> With this method, your can delete a file of the files server. Pass your id.'

# final message
HELP_MESSAGE = f"Put the method for make the requuest. Some methods are GET, POST, PUT, DELETE, GET-FILE (for get a file of the server files) In alls the methods, your can save the output in a file (pass the path, sample: /home/user/get.txt). The output will save in the file. The path for pass and save the file, will be diferent in Windows or Unix.{GET_DOC} {GET_FILE_DOC} {POST_DOC} {PUT_DOC} {DELETE_DOC} \t\t\t Please see README file for see more and better information !!!"