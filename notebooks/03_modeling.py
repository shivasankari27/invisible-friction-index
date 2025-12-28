import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

df = pd.read_csv("data/processed/friction_data.csv")


baseline = ["studytime", "absences", "failures"]
X_base = df[baseline]
X_friction = df[baseline + ["friction_index"]]
y = df["failure"]

Xb_train, Xb_test, y_train, y_test = train_test_split(
    X_base, y, test_size=0.2, random_state=42
)

Xf_train, Xf_test, _, _ = train_test_split(
    X_friction, y, test_size=0.2, random_state=42
)

model_base = LogisticRegression(max_iter=1000)
model_base.fit(Xb_train, y_train)
auc_base = roc_auc_score(y_test, model_base.predict_proba(Xb_test)[:,1])

model_friction = LogisticRegression(max_iter=1000)
model_friction.fit(Xf_train, y_train)
auc_friction = roc_auc_score(y_test, model_friction.predict_proba(Xf_test)[:,1])

print("Baseline AUC:", auc_base)
print("With Friction AUC:", auc_friction)
