from flask import Flask
from skimage import io
import os
from azure.common.credentials import ServicePrincipalCredentials
from azureml.core.model import Model
   

from azureml.core.authentication import ServicePrincipalAuthentication
from azure.storage.blob import BlobServiceClient

from azureml.core import Workspace,Datastore,Dataset


app = Flask(__name__)

# Retrieve the IDs and secret to use with ServicePrincipalCredentials
tenant_id = "e6311692-39bf-4a2b-95d1-2636e4e409c7"
client_id = "80b5eb4f-f73f-45ee-8e68-47de95d57340"
client_secret = "DPG~sW85RX8Loh8L4-zc-RCH8GyJq-x5t3"


svc_pr = ServicePrincipalAuthentication(
    tenant_id=tenant_id,
    service_principal_id=client_id,
    service_principal_password=client_secret)

ws = Workspace(
    subscription_id="9c6e1d8a-238d-4ae2-8b6e-7cb9dbae6faf",
    resource_group="OCR",
    workspace_name="P8_OCR",
    auth=svc_pr
    )

model = Model(ws, 'ocr_p8_voiture_v1')

model.download(target_dir=os.getcwd(), exist_ok=True)

# verify the downloaded model file
file_path = os.path.join(os.getcwd(), "fwrk.pkl")

os.stat(file_path)

@app.route("/")
def hello():
    return image


if __name__ == '__main__':
    app.run(debug=True)