import pandas as pd
import matplotlib.pyplot as plt

data = {"name": ["Akumu", "Joseph", "Bob"], "age" : [23, 56, 89], "city": ["Rangwe", "Oyugis", "Homa Bay"]}
df = pd.DataFrame(data)

food = pd.read_csv("onlinefoods.csv")
column_names = ['Age', 'Gender', 'Marital Status', 'Occupation', 'Monthly Income']

food_df = food.columns
new_df = food[column_names]

selected_column = 'Age'
grouped_data = food[selected_column].value_counts().sort_index()

plt.figure(figsize=(10, 6))
grouped_data.plot(kind='bar', color='skyblue')
plt.title(f'Bar Chart for {selected_column}')
plt.xlabel(selected_column)
plt.ylabel('Count')
plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
plt.grid(axis='y')  # Add gridlines on y-axis
plt.tight_layout()
plt.show()

print(len(new_df))
print(food_df)

print(df)

