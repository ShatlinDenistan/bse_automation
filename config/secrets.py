from google.cloud import secretmanager
import json


class SecretManager:
    def __init__(self):
        self.project_id = "secrets-staging-452708"
        self.secret_id = "bse-test-automation"
        self.version = "latest"

    def get_secrets(self) -> dict:
        client = secretmanager.SecretManagerServiceClient()

        secret_name = f"projects/{self.project_id}/secrets/{self.secret_id}/versions/{self.version}"
        response = client.access_secret_version(name=secret_name)
        secret_value = response.payload.data.decode("UTF-8")
        secret_value = json.loads(secret_value)
        return secret_value
