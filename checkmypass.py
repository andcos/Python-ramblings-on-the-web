# check my password online - Troy Hunt - haveibeenpwned.com
# when an Email has been used in a databreach
# Passwords too -200-228
# dictionary attack used by hackers with brute force attack
# blur 1Password stickypassword

import requests
import hashlib
import sys

url = 'https://api.pwnedpasswords.com/range/' + 'CBFDA'
res = requests.get(url)
print(res)

def request_api_data(query_char):
	url = 'https://api.pwnedpasswords.com/range/' + 'CBFDA'
	res = requests.get(url)
	if res.status_code != 200:
		raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')

# get the count of a password that has been leaked count number of times
def get_password_leaks_count(hashes, hash_to_check):
# tupple comprihension
# with hashes.text.splitline
	hashes = (line.split(':') for line in hashes.text.splitlines)	
	# check the generator hashes created
	for h, count in hashes:
		#print(h,count)
		# hash_to_check is only on our machine
		if h == hash_to_check:
			return count
	return 0	

def read_res(response):
	print(response.text)

def pwned_api_check(password):
# check if password exists in API response - first 5 chars - last 5 chars
	sha1password  = hashlib.sha1(password.encode('utf-8')).hexdigest().upper
	first5_char, tail = sha1password[:5], sha1password[5:]
	response = request_api_data(first5_char)
	print (first5_char, tail)
	print (response)
	return read_res(response)

request_api_data(123)
	
def main(args):
	for password in args:
		count = pwned_api_check(password)
		if count:
			print( f'{password} was found {count} times...you should probably change it!!')
		else:
			print(f'{password} was NOT found. Carry on!')
	return 'done!'

if __name__ =='__main__'
	sys.exit(main(sys.argv[1:]))


# read the passwords from a text file