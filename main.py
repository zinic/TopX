import requests

print(requests.get('https://api.github.com/repos/zinic/pyrox/stats/contributors').json())
