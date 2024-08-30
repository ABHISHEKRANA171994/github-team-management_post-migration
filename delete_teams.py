import requests
import os

# Get environment variables
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_ORG = os.getenv("ORG_NAME")

def delete_team_from_repo(org, repo, team_slug):
    url = f"https://api.github.com/repos/{org}/{repo}/teams/{team_slug}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }

    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        print(f"Successfully removed team {team_slug} from repository {repo}.")
    else:
        print(f"Failed to remove team {team_slug} from repository {repo}. Status code: {response.status_code}")
        print(response.json())

def process_team_list(file_path, org):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            repo, team_slug = line.strip().split(',')
            if repo and team_slug:
                print(f"\nProcessing repository: {repo}, Team: {team_slug}")
                delete_team_from_repo(org, repo, team_slug)

if __name__ == "__main__":
    file_path = "team_list.txt"  # Name of the uploaded file
    process_team_list(file_path, GITHUB_ORG)
