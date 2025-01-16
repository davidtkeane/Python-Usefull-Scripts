import requests
import subprocess

def access_webpage(url):
  """Accesses a webpage and returns the HTML content.

  Args:
    url: The URL of the webpage to access.

  Returns:
    The HTML content of the webpage, or None if the request fails.
  """
  response = requests.get(url)

  if response.status_code == 200:
    return response.content
  else:
    print(f"Failed to access webpage: {response.status_code}")
    return None

def export_conversation(conversation_history):
  """Exports a conversation to a file.

  Args:
    conversation_history: A list of strings, each string representing a line of the conversation.
  """
  with open("conversation.txt", "w") as f:
    for line in conversation_history:
      f.write(line + "\n")

def main_webpage():
  """Access a webpage and print its content."""
  url = "https://icanhelp.ie"

  html_content = access_webpage(url)

  if html_content is not None:
    print(html_content)
  else:
    print(f"Failed to access webpage: {url}")

def main_conversation():
  """Exports the current conversation to a file."""
  conversation_history = subprocess.check_output("convo history", shell=True).decode("utf-8").splitlines()

  export_conversation(conversation_history)

if __name__ == "__main__":
  main_webpage()
  main_conversation()
