from litellm import completion;
from dotenv import load_dotenv;
import os

load_dotenv();

def litellm_strategy() -> str:
    output = completion(
        model = os.environ['MODEL'],
        messages=[{ "content": "Who is the founder of Pakistan?","role": "user"}]
    );
    return output['choices'][0]['message']['content'];
    # return "Hello";
    