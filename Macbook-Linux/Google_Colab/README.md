# Google Colabs

## Github

[![Google Colabs](https://img.shields.io/badge/Google-Colabs%20-green?logo=google&logoColor=white&labelColor=EA4335)](https://github.com/davidtkeane/Google_Colab.git)

![Python](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python) ![License](https://img.shields.io/badge/License-MIT-green?logo=opensourceinitiative) 
![Version](https://img.shields.io/badge/Version-2.0-orange?logo=v)

<details>
<summary>📊 Github Stats</summary>

### Github Commits

![GitHub last commit](https://img.shields.io/github/last-commit/davidtkeane/Google_Colab?logo=github&style=flat-square)
![GitHub commit activity](https://img.shields.io/github/commit-activity/w/davidtkeane/Google_Colab?logo=github&authorFilter=davidtkeane)
![GitHub issues](https://img.shields.io/github/issues-raw/davidtkeane/Google_Colab?logo=github&style=flat-square)
![GitHub Sponsors](https://img.shields.io/github/sponsors/davidtkeane?logo=github&)

### Time @ Work!

[![CodeTime Badge](https://img.shields.io/endpoint?style=social&color=222&url=https%3A%2F%2Fapi.codetime.dev%2Fshield%3Fid%3D26388%26project%3D%26in=0)](https://codetime.dev)

### My Other Cool Scripts.

[![Gmail Multi-Account CLI](https://img.shields.io/badge/Gmail-Multi--Account%20CLI-green?logo=gmail&logoColor=white&labelColor=EA4335)](https://github.com/davidtkeane/gmail-multi-cli)
[![Sleep CLI](https://img.shields.io/badge/Sleep-CLI-blue?logo=homeassistant)](https://github.com/davidtkeane/Sleep-CLI)
[![PhoneBook CLI](https://img.shields.io/badge/PhoneBook-CLI-blue?logo=whatsapp&logoColor=white)](https://github.com/davidtkeane/PhoneBook-CLI)
[![Kermit ScreenSaver](https://img.shields.io/badge/kermit-screensaver-blue?logo=gnometerminal)](https://github.com/davidtkeane/kermit)

### Socials

[![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/davidtkeane)
[![X](https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white)](https://twitter.com/davidtkeane)
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/davidtkeane)

### Badges

![Windows-Badge](https://img.shields.io/badge/Microsoft-Windows%2011-0078D6?logo=windows&logoColor=0078D6&labelColor=white)
![AppleMac-Badge](https://img.shields.io/badge/Apple-macOS-000000?logo=apple&logoColor=white&labelColor=black)
![Linux-Badge](https://img.shields.io/badge/Linux-FCC624?logo=linux&logoColor=black&labelColor=white)

[![Buy me a coffee](https://img.buymeacoffee.com/button-api/?text=Buy%20me%20a%20coffee&emoji=&slug=davidtkeane&button_colour=FFDD00&font_colour=000000&font_family=Cookie&outline_colour=000000&coffee_colour=ffffff)](https://buymeacoffee.com/davidtkeane)

</details>

## Description

This project provides a foundational setup for integrating various cloud services and APIs (Google Colab, Google Drive, GitHub, OpenAI and Gemini) into a Python environment, primarily for AI development. It includes instructions on how to obtain API keys securely and use them to access Google Drive, interact with OpenAI and Gemini models in Google Colab.

## Features

*   **Google Colab Integration:** Instructions to set up Google Colab with secure API key management.
*   **Google Drive Integration:** Mount Google Drive, manage folders and synchronize files between Colab and Drive.
*   **GitHub Integration:** Connect Colab to GitHub for version control and code sharing.
*   **OpenAI API Integration:** Instructions on how to obtain your OpenAI API key and integrate it into your project.
*   **Gemini API Integration:** Instructions on how to obtain your Google Gemini API key and integrate it into your project.
*   **Secure API Key Management:** Uses Colab secrets to avoid hardcoding API keys in code.
*   **Interactive Sync Buttons:** Provides an interactive UI to initiate file sync between Google Drive and Colab.
*   **Color-coded Output:** Enhances readability with colored console outputs for status messages.

## Prerequisites

*   A Google Account
*   A GitHub Account
*   An OpenAI Account (for OpenAI API access)
*   An OpenAI API Key
*   A browser (Chrome, Firefox, Safari)

## Detailed Setup Instructions

### Part 1: Obtaining API Keys

#### 1.  Google Gemini API Key
   1.  Go to **Google AI Studio:**  [https://aistudio.google.com/](https://aistudio.google.com/)
   2.  **Sign in:** Use your Google Account.
   3.  **Create a Project (if you don't have one):**  Click "Create New Project" if necessary and name your project.
   4.  **Get Your API key:** Go to the "API" section and click "Get API key."
   5.  **Create API key:** Click "Create API key in new project".
   6. **Copy your API key**: This string is your secret.

#### 2. Google Drive API Key

   1.  Go to **Google Cloud Console:** [https://console.cloud.google.com/](https://console.cloud.google.com/)
   2.  **Sign in:** Use the same Google Account.
   3.  **Create Project (if needed):** Click the "Select a project" button, and create a new one with a name (e.g. "Google Drive API").
   4. **Go to APIs & Services:** On the left-hand menu, go to "APIs & Services" and select "Enabled APIs & Services"
   5. **Enable Google Drive API:** Click "+ Enable APIs and Services" and search for "Google Drive API", Click on it, then click on "Enable".
   6.  **Create Credentials:** On the left-hand menu, go to "Credentials"
   7.  **Create New Credentials:** Click on "Create Credentials" and select "API key".
   8. **Copy your Google Drive API Key:** This string is your secret.

#### 3. OpenAI API Key
   1.  Go to **OpenAI Platform**: [https://platform.openai.com/](https://platform.openai.com/)
   2. **Sign in:** Use your OpenAI Account or create one.
   3.  **Create API Keys:** Click on the "API Keys" option and select "Create New Secret Key".
   4.  **Copy Your API Key:** Copy the generated API key.

### Part 2: Setting up Google Colab

1.  **Go to Google Colab:** [https://colab.research.google.com/](https://colab.research.google.com/)
2.  **Sign in:** Use the same Google Account.
3.  **Create a new Notebook:** Click "New Notebook."
4.  **Set up Colab Secrets:**
    *   Find the Secrets icon (key icon) on the left sidebar.
    *   Click "Add a secret."
    *   **For Google Drive API Key:**
        *   In "Name" field enter `GOOGLE_DRIVE_API`.
        *   In "Value" field, paste your Google Drive API Key.
        *   Click "Add secret."
    *   **For Gemini API Key:**
        *    In "Name" field enter `GEMINI_API_KEY`.
        *    In "Value" field, paste your Gemini API Key.
        *    Click "Add secret."
    *   **For OpenAI API Key:**
         *    In "Name" field, enter `OPENAI_API_KEY`.
         *   In "Value" field, paste your OpenAI API key.
         *   Click "Add secret."

5.  **Mount Google Drive:**
    *  Create a code cell and add:
         ```python
           from google.colab import drive
           drive.mount('/content/drive')
        ```
       * Run the cell, it will prompt you to select the account that your Google Drive belongs to and the required permissions.
6. **Link to Github:**
    * From the menu, select "File", then select "Save a copy in GitHub" this will allow you to link a repository to Google Colab.
    * To get a repository, you can either create a new repository in github then link to that or a already existing repository.

7. **Using your API keys:**

   *   In your Colab Notebook create a new cell and add one of the following examples depending on which API Key you are using.
    *   **Google Gemini Example**

       ```python
       import google.generativeai as genai
       from google.colab import userdata

       gemini_api_key = userdata.get('GEMINI_API_KEY')

       genai.configure(api_key=gemini_api_key)

       model = genai.GenerativeModel('gemini-pro')
       response = model.generate_content("What is the capital of France?")
       print(response.text)
       ```

    *  **OpenAI Example**

          ```python
          import os
          from openai import OpenAI
          from google.colab import userdata
          OPENAI_API_KEY = userdata.get("OPENAI_API_KEY")
          os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY
          client = OpenAI()

          chat_completion = client.chat.completions.create(
              messages=[
                  {
                      "role": "user",
                      "content": "What is the capital of France?",
                  }
              ],
              model="gpt-3.5-turbo",
          )
          print(chat_completion.choices[0].message.content)

          ```

        *  Replace `gpt-3.5-turbo` with the model you want to use.

### Part 3: Example Colab Sync Script

Copy and paste the Python script (as shown previously) into a code cell in your Colab notebook.
This script will allow you to sync files between Colab and Google Drive. Be sure to have configured your API keys and Secrets correctly before running the script.

## Acknowledgment:

Created by Ranger (Dec 2024) Version 1.0.0 <br>
Modified by David Keane (Dec 31st 2024) Version 1.0.0 <br>
Assisted by Gemini (Jan 10th 2024)<br>

Feel free to customize the content as needed.