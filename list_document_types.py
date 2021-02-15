from PPPForgivenessSDK.client import Client

# to run file 'list_dcument_types.py', use valid token (page parameter can be changed )
client = Client(
    access_token='c1fad04273b482eba7c8e14c4db57479defbbfc7',
    vendor_key='2139dbe1-3fca-4729-9d29-724cd3d63672',
    environment='sandbox'
)

document_type_api = client.document_types

# read first page of document types
result = document_type_api.list(page=1)

if result['status'] == 200:
    print(result['data'])
else:
    print("An error occurred." + str(result['status']))
    print(result['data'])


