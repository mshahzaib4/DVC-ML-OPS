import pandas as pd
import os

data = {
    "Name": ["Shahzaib", "Zohaib", "Abdullah"],
    "Age":  ["25", "15", "22"],
    "City":["Narowal", "Narowal", "Narowal"]
}
df = pd.DataFrame(data)

new_row = {"Name": "Ali", "Age":"31", "City":"Lahore"}
df.loc[len(df.index)] = new_row

new_row = {"Name": "Ahamed", "Age":"29", "City":"Lahore"}
df.loc[len(df.index)] = new_row
os.makedirs("data", exist_ok=True)

file_path = os.path.join("data", "sample.csv")

df.to_csv(file_path, index=False)
print(f"File are save to {file_path}")