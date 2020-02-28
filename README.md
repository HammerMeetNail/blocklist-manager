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

# Getting Started
```
docker build --tag blocklist-manager:local .
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