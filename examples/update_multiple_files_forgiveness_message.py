from PPPForgivenessSDK.client import Client

# to run file 'read_forgiveness_message.py', use valid token and slug associated with a valid thread
client = Client(
    access_token='{{YOUR_TOKEN_HERE}}',
    vendor_key='{{YOUR_VENDOR_KEY}}',
    environment='sandbox'
)

message_api = client.messages

document_types = []
document_types.append(int('{{DOCUMENT_TYPE}}'))
document_types.append(int('{{DOCUMENT_TYPE}}'))
document_name=['{{DOCUMENT_NAME}}','{{DOCUMENT_NAME}}']
documents = []
documents.append(open('{{PATH_TO_DOCUMENT_FILE_HERE}}','rb'))
documents.append(open('{{PATH_TO_DOCUMENT_FILE_HERE}}','rb'))
slug = '{{SLUG}}'

result = message_api.update_with_multiple_files(slug, document_types, document_name, documents, message_text='{{MESSAGE}}')


if result['status'] == 200:
    print(result['data'])
else:
    print("An error occurred." + str(result['status']))
    print(result['data'])



# read info for single forgiveness request
# result = message_api.update(slug='{{SLUG HERE}}', document_type, document_name, document, message_text=''):
# if result['status'] == 200:
#     print(result['data'])
# else:
#     print("An error occurred." + str(result['status']))
#     print(result['data'])
