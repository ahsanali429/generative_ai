from crewai.flow.flow import Flow, start, listen, router;
from litellm import completion;
import random;

class CityFunFactFlowWithRouter(Flow):

    @start()
    def generate_city_name(self):
        city_list = ["Karachi", "Islamabad", "Lahore"];
        city_name = random.choice(city_list);
        print(city_name);
        return city_name;

    @router(generate_city_name)
    def generate_fun_fact(self, city_name):
        if (city_name) == "Karachi":
            return "Karachi";
        elif (city_name) == "Islamabad":
            return "Islamabad";
        elif (city_name) == "Lahore":
            return "Lahore";
        # return city_name;
        
    @listen("Karachi")
    def run_karachi(self, city_name):
        msg = f"Write a fun fact about {city_name}"
        print(msg);
        return msg;

    @listen("Islamabad")
    def run_islamabad(self, city_name):
        msg = f"Write a fun fact about {city_name}"
        print(msg);
        return msg;
    
    @listen("Lahore")
    def run_lahore(self, city_name):
        msg = f"Write a fun fact about {city_name}"
        print(msg);
        return msg;

def kickoff():
    output = CityFunFactFlowWithRouter();
    output.kickoff();

def plot():
    output = CityFunFactFlowWithRouter();
    output.plot();
