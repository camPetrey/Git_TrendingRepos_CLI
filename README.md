# Git_TrendingRepos_CLI

Git_TrendingRepos_CLI is a lightweight Python command-line tool that fetches and displays trending GitHub repositories. Users can filter repositories by a time range (day, week, month, or year) and control how many results are displayed.

The tool sorts repositories by star count and presents them in a clean, readable format including:

Repository name

Description

Star count

Primary programming language

URL

Leverages the GitHub REST API and includes error handling for invalid input or API issues. For developers who want a quick snapshot of what’s popular on GitHub.

## Installation

1. Clone the repository:

git clone <your-repo-url>
cd Git_TrendingRepos_CLI


2. Create and activate a Python virtual environment:

python3 -m venv .venv
source .venv/bin/activate  # Mac/Linux
# On Windows: .venv\Scripts\activate

3. Install the required dependencies:

pip install -r requirements.txt

## Usage

Run the CLI tool from your terminal:
python3 trendingRepos.py [options]

## Examples: 

1. Fetch top 10 repositories from the past week:

python3 trendingRepos.py -l 10 -d week

2. Fetch top 3 repositories from the past year:

python3 trendingRepos.py --limit 3 --duration year

https://roadmap.sh/projects/github-trending-cli - project idea