from crewai.flow.flow import Flow, start, listen
from litellm import completion
import os

class CityFunFactFlow(Flow):

    @start()
    def generate_city_name(self):
        llm_result = completion(
            model=os.environ['MODEL'],
            api_key= os.environ['GEMINI_API_KEY'],
            messages=[
                {
                    "content": "Return any city name from the whole world",
                    "role": "user"
                }
            ]
        );
        city_name = llm_result['choices'][0]['message']['content'];
        print(city_name);
        return city_name;

    @listen(generate_city_name)
    def generate_fun_fact(self, city_name):
        llm_result = completion(
            model=os.environ['MODEL'],
            api_key= os.environ['GEMINI_API_KEY'],
            messages=[
                {
                    "content": f"Write fun facts about the {city_name}, return all text in html format",
                    "role": "user"
                }
            ]
        );
        return llm_result['choices'][0]['message']['content']; 
    
    @listen(generate_fun_fact)
    def save_fun_fact_in_file(self, fun_fact):
        with open("fun_fact.html", "w") as file:
            file.write(fun_fact);

def kickoff():
    output = CityFunFactFlow();
    output.kickoff();
