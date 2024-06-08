from openai import OpenAI
from webappcv.utils.role_examples import question, messages, resume, job_description
import os
import uuid
import time


def load_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        file_brute = ''
        for line in file:
            if line.strip():
                file_brute += ' ' + line.strip()
    file = file_brute.strip()            
    return file

def call_openai_api(cv, jd, client):
    folder = os.getcwd()
    print(folder)
    cv_definition = load_file(os.path.join('webappcv', 'utils', 'data', 'cv_definition.txt'))
    definition = load_file(os.path.join('webappcv', 'utils', 'data', 'definition.txt'))
    report_example = load_file(os.path.join('webappcv', 'utils', 'data', 'report_example.txt'))
    submit = [f"1. Resume:{cv}. Job Description:{jd}. Calculate a score 0-100 depending on the similarities between 'resume' and 'job description'",
            """2. Write and return a new version for the resume according to good practices and formal english. Instead of 'Objective' section, use a 'Profile' 
            section instead; In the 'Education' section you must put only Undergraduate, Graduate and Post Graduate studies. Any other
            courses and trainning must be put in another section like 'Further Education' or any other title you see as appropriate."""
            ]

    messages = [{"role": "system",
                "content": definition},
            {"role": "user",
             "content": cv_definition},
            {"role":"assistant", 
            "content":report_example}]

    for s in submit:
        messages.append({"role":"user", "content":s})
        response = client.chat.completions.create(
            model = "gpt-3.5-turbo",
            temperature = 0.2,
            messages=messages
        )
        reply = response.choices[0].message.content
        messages.append({"role":"assistant", "content":reply})

    return messages


    

