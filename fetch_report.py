import requests
import json
from datetime import datetime

def fetch_top_models():
    url = "https://huggingface.co/api/models"
    response = requests.get(url)
    models = response.json()

    # Sort models by download count and take the top 10
    top_models = sorted(models, key=lambda x: x['downloads'], reverse=True)[:10]
    return top_models

def generate_report(models):
    report = "Top 10 Downloaded Models from Hugging Face\n"
    report += "======================================\n"
    report += f"Generated on: {datetime.now()}\n\n"
    for i, model in enumerate(models, start=1):
        report += f"{i}. {model['modelId']} - {model['downloads']} downloads\n"
    return report

def save_report(report, filename="report.txt"):
    with open(filename, "w") as file:
        file.write(report)

if __name__ == "__main__":
    top_models = fetch_top_models()
    report = generate_report(top_models)
    save_report(report)
