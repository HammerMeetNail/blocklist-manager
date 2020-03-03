[![Build Status](https://travis-ci.com/HammerMeetNail/blocklist-manager.svg?branch=master)](https://travis-ci.com/HammerMeetNail/blocklist-manager)
[![Coverage Status](https://coveralls.io/repos/github/HammerMeetNail/blocklist-manager/badge.svg?branch=master)](https://coveralls.io/github/HammerMeetNail/blocklist-manager?branch=master)
# blocklist-manager
A service for managing a URL blocklist in DynamoDB

# Prerequisites
1. DynamoDB table with the following attributes
```
Table name
	blocklist
Primary partition key
	domain (String)
Primary sort key
	path (String)
```
2. (Optional) Docker

# Getting Started
```
docker build --tag hammermeetnail/blocklist-manager:latest .

# Add your AWS info to docker-compose.yml
docker-compose up -d

# Create a blocked url
curl -X POST -H "Content-Type:application/json" --data '{"host":"example.com:80","path":"/test"}' localhost/urls

# Delete a blocked url
curl -X DELETE -H "Content-Type:application/json" --data '{"host":"example.com:80","path":"/test"}' localhost/urls

```

# Local Development
```
gunicorn -c gunicorn.py wsgi:app
```