import json
import requests
base_url = "https://api2.prismacloud.io"
customerName = None  # optional. customerName which is tenant Name
username = "46646263667366363663" #Prisma Access Keys
password = "sjsdhhdhdhsjjsjjs" # Prisma Access Keys

# Map of cloud type to accountIds for which autoConsent feature needs to be enabled/disabled
# Cloud Types supported: ["aws", "azure", "gcp", "oci"]
# Eg: account_ids = {"azure": ["c9addbd7-4f7d-4932-859f-990a8e9fcbd7"], "aws": ["488387218036", "963840066676"]}
account_ids = {"aws": ["663070621813"]}

# autoConsent = "enabled" - to opt in accountIds for autoConsent
# autoConsent = "disabled" - to opt out accountIds for autoConsent
auto_consent_value = "enabled"

# Prerequisite: Obtain an authorization token by Logging In.
login_url = f"{base_url}/login"

if customerName is not None:
    login_payload = json.dumps({
      "customerName": customerName,
      "username": username,
      "password": password
    })
else:
    login_payload = json.dumps({
        "username": username,
        "password": password
    })

login_headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", login_url, headers=login_headers, data=login_payload, verify=False)
YOUR_TOKEN = response.json()['token']

# Call Cloud Account Patch API to enable/disable autoConsent
cloud_account_patch_api_url = "{base_url}/cloud/{cloudType}/{accountId}"

cloud_account_patch_api_payload = json.dumps({
  "autoConsent": auto_consent_value
})

cloud_account_patch_api_headers = {
  'accept': 'application/json',
  'content-type': 'application/json',
  'x-redlock-auth': YOUR_TOKEN
}

# for cloud_type, account_ids in account_ids.items():
#     for account_id in account_ids:
#         response = requests.request(
#             method="PATCH",
#             url=cloud_account_patch_api_url.format(base_url=base_url, cloudType=cloud_type, accountId=account_id),
#             headers=cloud_account_patch_api_headers,
#             data=cloud_account_patch_api_payload,
#             verify=True
#         )

#         if response.status_code == 200:
#             print(f"Successfully updated account ID - {account_id}")
#         else:
#             print(f"Failed to update account ID {account_id}, status_code: {response.status_code}")
#             print(f"Failed to update account ID {account_id}, response: {response.text}")
#             print(f"Failed to update account ID {account_id}, status: {response.headers.get('x-redlock-status')}")

for cloud_type, account_ids in account_ids.items():
    for account_id in account_ids:
        response = requests.request(
            method="PATCH",
            url=cloud_account_patch_api_url.format(base_url=base_url, cloudType=cloud_type, accountId=account_id),
            headers=cloud_account_patch_api_headers,
            data=cloud_account_patch_api_payload,
            verify=True  # Change to True for certificate verification
        )

        if response.status_code == 200:
            print(f"Successfully updated account ID - {account_id}")
        else:
            print(f"Failed to update account ID {account_id}, status_code: {response.status_code}")
            print(f"Failed to update account ID {account_id}, response: {response.text}")
            print(f"Failed to update account ID {account_id}, status: {response.headers.get('x-redlock-status')}")
