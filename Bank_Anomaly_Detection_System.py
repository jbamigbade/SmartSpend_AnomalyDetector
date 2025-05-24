# Bank_Anomaly_Detection_System.py

import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import matplotlib
matplotlib.use("TkAgg")  # 👈 Add this line
import matplotlib.pyplot as plt
import seaborn as sns
from tkinter import Tk, filedialog
from datetime import datetime
import os

# File picker dialog
def get_file_path():
    Tk().withdraw()
    return filedialog.askopenfilename(title="Select Transaction CSV File", filetypes=[("CSV Files", "*.csv")])

# Extract relevant features
def extract_features(df):
    df["DayOfWeek"] = df["Date"].dt.dayofweek
    df["Month"] = df["Date"].dt.month
    return df[["Amount", "DayOfWeek", "Month"]]

# Train Isolation Forest
def train_model(X, contamination=0.05):
    model = IsolationForest(contamination=contamination, random_state=42)
    model.fit(X)
    return model

# Predict and score
def detect_anomalies(model, X):
    scores = model.decision_function(X) * -1
    predictions = model.predict(X)
    flags = [1 if p == -1 else 0 for p in predictions]
    return flags, scores

# Visualize anomalies and save plot
def plot_anomalies(df, save_path=r"D:\SmartSpend Anomaly Detection in Financial Transactions Using Isolation Forests\anomaly_plot.png"):
    plt.figure(figsize=(12, 6))
    sns.lineplot(x="Date", y="Amount", data=df, label="Transaction")
    sns.scatterplot(data=df[df["Anomaly"] == 1], x="Date", y="Amount", color="red", label="Anomaly", s=100)
    plt.title("Bank Transaction Anomalies")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.legend()
    plt.tight_layout()
    plt.savefig(save_path)
    print(f"🖼️ Plot saved to: {save_path}")
    plt.show()

# Save and log anomalies
def log_results(df, output_path="bank_anomalies.csv"):
    df[df["Anomaly"] == 1].to_csv(output_path, index=False)
    print(f"📁 Anomalies saved to: {output_path}")
    print(f"✅ Total Transactions: {len(df)}")
    print(f"🚨 Anomalies Detected: {df['Anomaly'].sum()}")
    print(f"📊 Percent Anomalous: {100 * df['Anomaly'].mean():.2f}%")

    with open("run_log.txt", "a") as log:
        log.write(f"{datetime.now()}: Detected {df['Anomaly'].sum()} anomalies from {len(df)} records.\\n")

# Main execution
def run_bank_anomaly_detection():
    file_path = get_file_path()
    if not file_path or not os.path.exists(file_path):
        print("❌ File not selected or not found.")
        return

    df = pd.read_csv(file_path)
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df = df.dropna(subset=["Date", "Amount"])

    features = extract_features(df)
    scaler = StandardScaler()
    scaled = scaler.fit_transform(features)

    model = train_model(scaled)
    flags, scores = detect_anomalies(model, scaled)
    df["Anomaly"] = flags
    df["AnomalyScore"] = scores

    plot_anomalies(df)
    log_results(df)

if __name__ == "__main__":
    run_bank_anomaly_detection()