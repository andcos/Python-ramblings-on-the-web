# check my password online - Troy Hunt - haveibeenpwned.com
# when an Email has been used in a databreach
# Passwords too -200-228
# dictionary attack used by hackers with brute force attack
# blur 1Password stickypassword

import requests

url = 'https://api.pwnedpasswords.com/range/' + 'CBFDA'
res = requests.get(url)
print(res)

def request_api_data(query_char):
	url = 'https://api.pwnedpasswords.com/range/' + 'CBFDA'
	res = requests.get(url)
	if response.status_code != 200:
		raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')

def pwned_api_check(password):
# check if password exists in API response
	pass

request_api_data(123)
	


