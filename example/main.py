from google.cloud import storage
# import httplib2

from gcp_process_credentials.credentials import ProcessCredentials
import os

e = os.environ.copy()
e.update({'foo': 'bar'})

pc = ProcessCredentials(command=["/usr/bin/cat"],  args=['/tmp/token.txt'], env=e,)
# pc.refresh(httplib2.Http())
# print(pc.token)

# def gcloud_parser(req):
#     data = {}
#     data["access_token"] = ''.join(req.decode().split('\n'))
#     data["expires_in"] = 3600
#     data["token_type"] = "Bearer"
#     return str(json.dumps(data))

# pc = ProcessCredentials(command=["gcloud"],  args=['auth', 'print-access-token'], env=e, parser=gcloud_parser)
# pc.refresh(httplib2.Http())
# print(pc.token)

project_id = 'core-eso'

storage_client = storage.Client(project=project_id, credentials=pc)
buckets = storage_client.list_buckets()
for bkt in buckets:
    print(bkt.name)
