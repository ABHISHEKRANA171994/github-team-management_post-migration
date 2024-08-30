import requests
import os

# Get the GitHub organization name from the environment variable
GITHUB_ORG = os.getenv("ORG_NAME")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def list_teams_for_repo(org, repo):
    url = f"https://api.github.com/repos/{org}/{repo}/teams"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }

    response = requests.get(url, headers=headers)
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f"{repo}_teams.txt")

    with open(output_file, 'w') as file:
        if response.status_code == 200:
            teams = response.json()
            if teams:
                file.write(f"Teams associated with the repository {repo}:\n")
                for team in teams:
                    file.write(f"- {team['name']} (permission: {team['permission']})\n")
            else:
                file.write(f"No teams associated with the repository {repo}.")
        else:
            file.write(f"Failed to fetch teams for the repository {repo}. Status code: {response.status_code}")

def process_repo_list(file_path, org):
    with open(file_path, 'r') as file:
        repos = file.readlines()
        for repo in repos:
            repo = repo.strip()
            if repo:
                print(f"\nChecking repository: {repo}")
                list_teams_for_repo(org, repo)

if __name__ == "__main__":
    file_path = "repo_list.txt"  # Name of the uploaded file
    process_repo_list(file_path, GITHUB_ORG)
