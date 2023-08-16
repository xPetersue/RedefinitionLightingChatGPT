# RedefinitionLightingChatGPT
Internet of Everything: IoT Redefinition with ChatGPT: This is a small experiment aimed at creating a complex scene mode of lighting with ChatGPT.

Step 1: Register an account on OpenAI and log in.

Step 2: Upon logging in, there are three options, choose API, navigate to the 'Personal' section located at the top-right corner. From there, access 'View API keys' as depicted in the image below.
![image](https://github.com/xPetersue/RedefinitionLightingChatGPT/assets/15628010/9700e83f-439e-4d6b-b5a2-e1748d9c316f)

Step 3: After completing step 2, a page displaying API keys will appear. Locate the 'Create new secret key' button, click on it, and a secret key will be generated. Copy this key and store it in a Notepad or any other location, as it will be necessary for the upcoming steps.
![image](https://github.com/xPetersue/RedefinitionLightingChatGPT/assets/15628010/0b9a433b-9414-41f6-b5bf-cea01d10e65a)

Step 4: Next, launch a code editor like Visual Studio Code or Sublime. For this tutorial, we'll use Visual Studio Code. Install the OpenAI library in Python using the following command.

pip install openai

Step 5: Import the openai library and assign the generated key from Step 3 to a variable, as illustrated below.

import openai
openai.my_api_key = 'YOUR_API_KEY'

Step 6: Define a context for the ChatGPT API, conveying its intended function using a JSON file. Within this context, designate the role as "system" to establish ChatGPT's identity as a system meant for user interaction. Additionally, outline the content to be processed.
messages = [ {"role": "system", "content": 
              "I am your Smart Home Lighting Controller"} ]

Step 7: Here is the rest of the code where 

We are using an infinite while loop so that we can chat with the ChatGPT API repeatedly without executing the code again and again. 
In the second line we a taking input from the user and store it in a variable ‘message’.
If a user inputs any question then only we enter the if condition and make a JSON of file and append it to the JSON file that we have created in step 6 after that generate the chat using openai.ChatCompletion.create()
Store the answer in the variable ‘reply’ and print that reply using the print() function.

![image](https://github.com/xPetersue/RedefinitionLightingChatGPT/assets/15628010/18293634-a38c-427d-a16f-317b7444077e)

Please see the complete code in RedefinitionLightingChatGPT.py file.
******************************************************************************************************************************
Note: "openai.error.RateLimitError: You exceeded your current quota, please check your plan and billing details." 

You need to activate the free plan by associating it with your credit card at a minimum, and then you will be able to import OpenAPI.
