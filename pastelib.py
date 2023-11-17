import requests

# This is needed to run almost everything
def set_api_key(api_key):
  global api_keys
  api_keys = api_key

# This creates a paste you can not edit (API Key needed)
def create_paste(text, Name=None, privacy=0, formate="text"):
  data = {
    "api_dev_key": api_keys,
    "api_option": "paste",
    "api_paste_code": text,
    "api_paste_name": Name,
    "api_paste_private": privacy,
    "api_paste_format": formate
  }
  try:
    response = requests.post("https://pastebin.com/api/api_post.php", data=data)
    if response.status_code == 200:
      global paste_url
      paste_url = response.text
      return paste_url
    else:
      return "Failed to create paste"
  except Exception as err:
    return "Failed to create paste: " + str(err)

# The gets a paste's info (API Key not needed)
def get_paste(paste_id):
  paste_info = requests.get(f"https://pastebin.com/raw/{paste_id}")
  
  global paste_text
  paste_text = paste_info.text
  return paste_text

# This lets you get the paste id from the paste url (API Key not needed)
def get_paste_id(paste_url):
  global paste_id
  paste_id = paste_url.split("/")[-1]
  return paste_id

# This lets you delete a paste (API Key needed)
def delete_paste(paste_id):
  data = {
    "api_dev_key": api_keys,
    "api_option": "delete",
    "api_paste_key": paste_id
  }
  try:
    response = requests.post("https://pastebin.com/api/api_post.php", data=data)
  except Exception as err:
    pass
    print("There was an error")
    print(err)

