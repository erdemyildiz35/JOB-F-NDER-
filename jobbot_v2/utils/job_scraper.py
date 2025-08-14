import requests
import pandas as pd

def scrape_jobs():
    """Arbeitnow API'sinden Almanya iş ilanlarını çeker."""
    url = "https://arbeitnow.com/api/job-board-api"
    jobs_data = []

    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            data = resp.json()
            for job in data.get("data", []):
                jobs_data.append({
                    "title": job.get("title"),
                    "company": job.get("company_name"),
                    "location": job.get("location"),
                    "url": job.get("url")
                })
        else:
            print("API request failed:", resp.status_code)
    except Exception as e:
        print("Error while fetching jobs:", e)

    df = pd.DataFrame(jobs_data)
    df.to_csv("data/jobs.csv", index=False)
    print(f"{len(df)} job listings saved to data/jobs.csv")

    return df
