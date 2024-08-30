name: List Teams for Repositories

on:
  workflow_dispatch:
    inputs:
      org_name:
        description: "GitHub Organization Name"
        required: true
        default: "your_org_name"
      repo_file:
        description: "File containing list of repositories"
        required: true
        type: artifact

jobs:
  list-teams:
    runs-on: ubuntu-latest

    steps:
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'

      - name: Install dependencies
        run: pip install requests

      - name: Download repository list file
        uses: actions/download-artifact@v3
        with:
          name: repo_file
          path: .

      - name: Run script to list teams for repositories
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          ORG_NAME: ${{ github.event.inputs.org_name }}
        run: |
          python list_teams.py

      - name: Upload output files
        uses: actions/upload-artifact@v3
        with:
          name: output-files
          path: output/
