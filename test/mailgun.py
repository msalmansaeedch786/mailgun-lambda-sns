import requests
import boto3
import json

def send_simple_message():
	return requests.post(
		"https://api.mailgun.net/v3/sandboxa86d715053564092b15a76b8b704a47c.mailgun.org",
		auth=("api", "5a60305d556a7780a0abc86ca9469688-a09d6718-6329e6c3"),
		data={"from": "Excited User <mailgun@sandboxa86d715053564092b15a76b8b704a47c.mailgun.org>",
			"to": ["msalmansaeedch786@gmail.com"],
			"subject": "Hello",
			"text": "Testing some Mailgun awesomness!"})

if __name__ == "__main__":
    print(send_simple_message())