import openai
import random
import time
from secret_key import mytestkey

# Set your OpenAI API key here
openai.api_key = mytestkey

def generate_city_data(city_name):
    # Define the categories
    categories = ["health", "education", "transportation", "public safety", "cost of living"]

    # Initialize an empty dictionary to store the results
    city_data = {}

    # Rate limit: maximum requests per minute
    max_requests_per_minute = 3

    # Calculate the delay (in seconds) between each request
    delay_between_requests = 60 / max_requests_per_minute

    # Generate data for each category
    for category in categories:
        # Define a clear and explicit prompt for each category
        prompt = f"Generate an integer value between 70 and 100 representing {category} in {city_name}."

        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=10  # Adjust as needed
        )

        # Extract the generated integer value and store it in the dictionary
        generated_value = response.choices[0].text.strip()

        # Convert the generated value to an integer
        try:
            generated_value = int(generated_value)
        except ValueError:
            generated_value = None

        # Ensure the generated value falls within the specified range
        if generated_value is not None and 70 <= generated_value <= 100:
            city_data[category] = generated_value
        else:
            # Retry generation if the value is outside the desired range
            city_data[category] = random.randint(70, 100)

        time.sleep(delay_between_requests)

    return city_data

# Provide the city name for which you want to generate data
city_name = "Thrissur"

# Call the function to generate data
generated_data = generate_city_data(city_name)

# Print the generated data
print(generated_data)

