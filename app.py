from flask import Flask
import os
from azure.mgmt.resource import SubscriptionClient
from azure.common.credentials import ServicePrincipalCredentials


app = Flask(__name__)

# Retrieve the IDs and secret to use with ServicePrincipalCredentials
tenant_id = "e6311692-39bf-4a2b-95d1-2636e4e409c7"
client_id = "80b5eb4f-f73f-45ee-8e68-47de95d57340"
client_secret = "fdc98684-b6a8-437b-b89e-21d60a64fdc9"

credential = ServicePrincipalCredentials(tenant=tenant_id, client_id=client_id, secret=client_secret)

subscription_client = SubscriptionClient(credential)

subscription = next(subscription_client.subscriptions.list())
print(subscription.subscription_id)

@app.route("/")
def hello():
    return "Welcome to machine learning model APIs!"+subscription.subscription_id


if __name__ == '__main__':
    app.run(debug=True)