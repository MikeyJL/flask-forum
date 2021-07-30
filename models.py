'''
Contains data model that interfaces with firestore.
:author: Mikey Lau
Website <https://mikeylau.uk>
GitHub <https://github.com/MikeyJL>
'''
from firebase import db

class UserModel ():

  '''
  Creates a new user in firestore.
  :param first_name: The new user's first name.
  :param last_name: The new user's last name.
  :param email: The new user's email.
  :param password: The new user's password.
  :returns: A boolean of whether it was successful.
  '''
  def create (self, first_name: str, last_name: str, email: str, password: str) -> bool:
    db.collection(u'users').document(email).set({
      u'first-name': first_name,
      u'last-name': last_name,
      u'email': email,
      u'password': password
    })
    return self.login(email, password)
  
  '''
  Logs in a user by checking their password.
  :param email: The user's email.
  :param password: The user's password.
  :returns: A boolean of whether it was successful.
  '''
  def login (self, email: str, password: str) -> bool:
    doc = db.collection(u'users').document(email).get()
    if doc.exists:
      print(doc.to_dict())
      return doc.to_dict()['password'] == password
    else:
      return False

class PostModel ():

  '''
  Creates a new post in firestore.
  :param title: The title of the new post.
  :param caption: The caption of the new post.
  :returns: A boolean of whether it was successful.
  '''
  def create (self, title: str, caption: str) -> bool:
    db.collection(u'posts').add({
      u'title': title,
      u'caption': caption
    })
    return True
  
  '''
  Gets all the documents in firestore's posts collection.
  :returns: A firestore instance of all the documents.
  '''
  def get_all (self) -> list:
    return db.collection(u'posts').stream()
  
  '''
  Deletes a post using the unique id.
  :param post_id: The id of the post.
  :returns: True.
  '''
  def delete (self, post_id: str) -> bool:
    db.collection('posts').document(post_id).delete()
    return True