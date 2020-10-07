import requests

url = input('Enter youtube url: ')
#url = 'https://www.youtube.com/watch?v=O5kJ69bPDME'

try:
	r = requests.get(url)
#r.text
	urltext = r.text  #(convert from request type into a string)

	keywords_string = urltext.partition("\"keywords\":[")[2].partition("]")[0]
 
	if len(keywords_string) != 0:
		l=keywords_string.split(',')
		for keyword in l:
			print(bytes(keyword, "utf-8").decode("unicode_escape"))
	else:
		print('no keywords found.')
except:
	print('Invalid URL\nURL needs to include http(s)://')

		