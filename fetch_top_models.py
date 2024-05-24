import requests
import csv

def fetch_top_models():
    url = "https://huggingface.co/api/models"
    params = {
        "sort": "downloads",
        "direction": -1,  # Descending order
        "limit": 10
    }
    
    response = requests.get(url, params=params)
    response.raise_for_status()  # Ensure we notice bad responses
    
    models = response.json()
    
    return models

def generate_report(models):
    report_file = "top_models_report.csv"
    with open(report_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Model ID", "Downloads"])
        
        for model in models:
            writer.writerow([model["id"], model["downloads"]])
    
    print(f"Report generated: {report_file}")

def main():
    models = fetch_top_models()
    generate_report(models)

if __name__ == "__main__":
    main()
