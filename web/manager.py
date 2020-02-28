import boto3
from flask import Flask, jsonify, request


client = boto3.client('dynamodb')

app  = Flask(__name__)

@app.route("/urls", methods=['DELETE', 'POST'])
def process_url():

    # DELETE
    if request.method == 'DELETE' and request.is_json:

        host = request.json['host']
        path = request.json['path']

        client.delete_item(
            TableName="blocklist",
            Key = {
                'domain': {
                    'S': host
                },
                'path': {
                    'S': path
                }
            }
        )
    
    # POST
    if request.method == 'POST' and request.is_json:

        host = request.json['host']
        path = request.json['path']
        client.put_item(
            TableName="blocklist",
            Item = {
                'domain': {
                    'S': host
                },
                'path': {
                    'S': path
                }
            }
        ) 

    response = jsonify(success=True)
    return response



if __name__ == "__main__":
    app.run(host='0.0.0.0')