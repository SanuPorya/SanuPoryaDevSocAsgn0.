import os
import json
import google.generativeai as genai
import time


genai.configure(api_key="AIzaSyA9xG_Z9CBUR07NJkADoTyIaVbvUpR5xP8")
    # get the Key 

# Read multiple questions from a text file
questions_file = "text.txt"
with open(questions_file, "r") as f:
    questions = [line.strip() for line in f if line.strip()]

#  Initialize list for JSON answers
answers_list = []

# Ask Gemini each question
model = genai.GenerativeModel("gemini-flash-latest")  # faster, cheaper model

for question in questions:
    try:
        response = model.generate_content(question)
        answer = response.text
    except Exception as e:
        # Fallback in case of error
        answer = f"Error getting answer: {str(e)}"
    # Add to answers list
    answers_list.append({"question": question, "answer": answer})
    # Optional: small delay to avoid hitting rate limits
    time.sleep(1)

#  Convert to JSON and save
with open("answers.json", "w") as outfile:
    json.dump(answers_list, outfile, indent=4)

#  Print to console
print(json.dumps(answers_list, indent=4))
