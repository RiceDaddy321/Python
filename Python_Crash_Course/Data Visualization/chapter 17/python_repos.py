import requests

# Make an api call and store the responses
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("States code:",r.status_code)

# Store API response  in a variable
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# Explore information about the repositories
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

#Examine the first repository.
repo_dict = repo_dicts[0]
print("\nKeys:",len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)