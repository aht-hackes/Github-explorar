import requests
import json

def find_best_repo(topic):
    # Use the GitHub API to search for repositories based on the provided topic
    query = f"q={topic}&sort=stars&order=desc"
    response = requests.get(f"https://api.github.com/search/repositories?{query}")

    # Check if the API call was successful
    if response.status_code == 200:
        # Parse the JSON response
          result = json.loads(response.text)
        items = result["items"]

        # Print the name and number of stars of the first 10 repositories
        for i, item in enumerate(items[:10]):
            print(f"{i + 1}. {item['name']} ({item['stargazers_count']} stars)")
    else:
        # Print an error message if the API call failed
        print("Error: API call failed")

# Example usage
find_best_repo("python")
