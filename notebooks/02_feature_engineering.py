import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("data/raw/student-mat.csv", sep=",")
df["failure"] = (df["G3"] < 10).astype(int)

# ----- Friction feature engineering -----
df["schedule_density"] = df["studytime"] * 2 + df["absences"] * 0.1
df["back_to_back_score"] = (df["studytime"] >= 3).astype(int)
df["deadline_density"] = df["failures"] + (df["studytime"] > 2).astype(int)
df["temporal_rigidity"] = df["studytime"] + (df["absences"] > 5).astype(int)

friction_features = [
    "schedule_density",
    "back_to_back_score",
    "deadline_density",
    "temporal_rigidity"
]

scaler = MinMaxScaler()
df[friction_features] = scaler.fit_transform(df[friction_features])

df["friction_index"] = df[friction_features].mean(axis=1)

df.to_csv("data/processed/friction_data.csv", index=False)
print("Saved data/processed/friction_data.csv")
