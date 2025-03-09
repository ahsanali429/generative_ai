# CrewAI Simple Flow

This repository contains a simple CrewAI flow designed to generate a fun fact about a random city using a large language model (LLM). The fun fact is then saved to an HTML file for easy access and sharing.

## Features

- **Random City Selection**: Automatically selects a city from a predefined list.
- **Fun Fact Generation**: Uses LLM capabilities to generate an interesting fact about the city.
- **HTML File Output**: Saves the fun fact to an HTML file, making it accessible through any web browser.
- **Streamlined Workflow**: Minimal setup and easy-to-run script.

## How It Works

1. The script randomly selects a city from a predefined list.
2. An LLM generates a fun fact related to the selected city.
3. The generated fun fact is saved to an HTML file in the project directory.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ahsanali429/generative_ai.git
   cd generative_ai/crewai_simple_flow
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   <b>OR</b>
    ```bash
   uv add litellm
   ```
    ```bash
   uv add crewai
   ```

4. Configure your environment with API access to an LLM (e.g., OpenAI GPT) and set your API key as an environment variable.

## Usage

Run the script to generate a fun fact and save it as an HTML file:
```bash
uv run city_fun_fact_flow
```

- The script will select a random city.
- It will generate a fun fact about the city using the LLM.
- The output will be saved in an `output.html` file in the project directory.

## Example Output

### Selected City: Paris

**Fun Fact**: Paris is often called the "City of Light" because it was one of the first cities in the world to have street lighting.

### Generated HTML File
The generated fun fact is saved in an HTML file named `output.html`, which can be opened with any browser.

## Contributing

Contributions are welcome! Feel free to fork this repository, make improvements, and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](../LICENSE) file for more information.
