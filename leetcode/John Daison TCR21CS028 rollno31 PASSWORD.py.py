import pandas as pd
import numpy as np

# Define the number of persons
num = 72

# Create a dictionary with data for each person
data = {
    'RollNo': ['RollNo{}'.format(i) for i in range(1, num + 1)],'GECTCR_RollNo_CSE21': ['GECTCR_RollNo_cse21'] * num,'password': np.random.randint(10000, 99999, size=num)
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Print the DataFrame
print(df)
