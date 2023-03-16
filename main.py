from flask import Flask, request
import random
import os
import openai
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
app = Flask(__name__)

@app.route('/gpt3', methods=['GET'])
def gpt3():
    input_string = request.args.get('input', '')
    response = openai.Completion.create(
            engine="text-davinci-003",
            prompt= input_string,
            max_tokens=1024,
            n=1,  
            stop=None,
            temperature=0.5,
        )    
    return response.choices[0].text

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=random.randint(2000, 9000))
	 
