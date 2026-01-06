import argparse
from datetime import datetime, timedelta
import requests

base_url = "https://api.github.com/search/repositories"
dateDict = {"day" : 1, "week" : 7, "month" : 30, "year" : 365}

parser = argparse.ArgumentParser()
parser.add_argument("-l", "--limit", help="How many repos (1-50)", type=int, default=5)
parser.add_argument("-d", "--duration", help="Duration of time to look back for repo (day, week, month, year)", default="week")

args = parser.parse_args()
limit = args.limit
if limit > 50 or limit < 1:
    print(f"Invalid limit '{limit}'. Pick a limit 1-50")
    exit(1)
duration = args.duration
if duration not in dateDict:
    print(f"Invalid duration '{duration}'. Choose from: {', '.join(dateDict.keys())}")
    exit(1)

def get_date(duration: str) -> str:
    """
    Convert a duration keyword into a cutoff date string.
    
    :param duration: Duration of time (day, week, month, year) to look back for repos
    :type duration: str
    :return: cutoff date in UTD
    :rtype: str
    """
    today = datetime.today()
    cutoff_date = today - timedelta(days= dateDict[duration])
    return cutoff_date.strftime("%Y-%m-%d")

def get_repos(limit: int, cutoff_date: str):
    """
    Docstring for get_repos
    
    :param limit: # of repos to retrieve  
    :type limit: int
    :param cutoff_date: furthest date to look for repo
    :type cutoff_date: str
    """
    url = f"{base_url}?q=created:>{cutoff_date}&sort=stars&per_page={limit}&order=desc"
    response = requests.get(url)
    status_code = response.status_code

    if status_code != 200:
        print(f"Failed to retrieve. Code: {status_code}")   
        exit(1)

    data = response.json() #Entire json file 
    repos = data["items"] #items aka the repos
    return repos

def display_repos(repos):
     """
     Docstring for display_repos
     
     :param repos: dictionary of repo items
     :Returns formatted output of repos with most stars in specified time range
     """
     n=0
     for repo in repos:
        n+=1
        name = repo["full_name"]
        stars = repo["stargazers_count"]
        desc = repo["description"] or "N/A"
        lang = repo["language"] or "N/A"
        url = repo["html_url"]
        print(f"\n{n}.\n")
        print(f"Name: {name}\nDescription: {desc}\nstars: {stars}\nLanguage: {lang}\nURL: {url}\n")
        print("____________________________________________________")

date = get_date(duration)
repos = get_repos(limit, date)
display_repos(repos)
