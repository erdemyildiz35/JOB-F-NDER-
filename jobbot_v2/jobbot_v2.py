from utils.job_scraper import scrape_jobs
from utils.cv_generator import generate_cv

def main():
    print("🔍 Fetching job listings...")
    df = scrape_jobs()

    print("\n📄 Generating English CV for general application...")
    generate_cv(lang="en", job_title="General Application")

    print("\n📄 Generating German CV for general application...")
    generate_cv(lang="de", job_title="Allgemeine Bewerbung")

if __name__ == "__main__":
    main()
