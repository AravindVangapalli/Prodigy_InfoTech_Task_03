import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)
num_records = 1000
date_rng = pd.date_range(start='2023-01-01', end='2023-01-31', freq='H')
dates = np.random.choice(date_rng, size=num_records)
weather_conditions = np.random.choice(['Sunny', 'Rainy', 'Foggy', 'Snowy'], size=num_records)
road_conditions = np.random.choice(['Dry', 'Wet', 'Icy'], size=num_records)
contributing_factors = np.random.choice(['Speeding', 'Distracted', 'Weather'], size=num_records)
data = pd.DataFrame({
    'Datetime': dates,
    'Weather_Condition': weather_conditions,
    'Road_Condition': road_conditions,
    'Contributing_Factor': contributing_factors
})
data['Datetime'] = pd.to_datetime(data['Datetime'])
data['Hour'] = data['Datetime'].dt.hour
data['DayOfWeek'] = data['Datetime'].dt.dayofweek
time_counts = data['Hour'].value_counts().sort_index()
plt.bar(time_counts.index, time_counts.values)
plt.xlabel('Hour of Day')
plt.ylabel('Accident Count')
plt.title('Accident Distribution by Time of Day')
plt.show()
weather_road_counts = data.groupby(['Weather_Condition', 'Road_Condition']).size().unstack()
weather_road_counts.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.xlabel('Weather Condition')
plt.ylabel('Accident Count')
plt.title('Accident Count by Weather and Road Conditions')
plt.xticks(rotation=45)
plt.legend(title='Road Condition')
plt.tight_layout()
plt.show()
contributing_factors = data['Contributing_Factor'].value_counts()
plt.bar(contributing_factors.index, contributing_factors.values)
plt.xlabel('Contributing Factor')
plt.ylabel('Accident Count')
plt.title('Distribution of Contributing Factors')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
