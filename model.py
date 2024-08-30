import warnings
import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.utils import shuffle
warnings.filterwarnings('ignore')

data = pd.read_csv('combineddata.csv')
data['Result'] = data['Result'].apply(lambda x: 1 if x == 'Human' else 0)
X = data.drop(columns=['Result', 'timestamp'])
y = data['Result']
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.3, random_state=42)
model = xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss')
model.fit(X_train, y_train)
def update_model(model, X_n, y_n):
    model.fit(X_n, y_n, xgb_model=model)
def evaluate_model(model, X_val, y_val):
    y_pred = model.predict(X_val)
    accuracy = accuracy_score(y_val, y_pred)
    report = classification_report(y_val, y_pred)
    print(f"Accuracy: {accuracy}")
    print("Classification Report:")
    print(report)
print("Initial Model Evaluation:")
evaluate_model(model, X_val, y_val)
for i in range(10):  
    X_n, y_n = shuffle(X, y)
    X_nb = X_n[:100]
    y_nb = y_n[:100]
    update_model(model, X_nb, y_nb)
    if (i + 1) % 2 == 0:  
        print(f"\nEvaluation after {i+1} updates:")
        evaluate_model(model, X_val, y_val)
