import json

from .base_api import BaseApi, UnknownException


class MessageApi(BaseApi):
    def list(self, sba_number=None, is_complete=False, page=1):
        """

        :param sba_number: str (optional)
        :param is_complete: bool (optional)
        :param page:
        :return:
        """
        assert (isinstance(page, int)), "page must be an integer"
        assert (isinstance(is_complete, bool)), "is_complete must be True or False"

        http_method = "GET"
        endpoint = "ppp_loan_forgiveness_messages/"

        uri = self.client.api_uri + endpoint

        params = {'page': page}
        if sba_number:
            params['sba_number'] = str(sba_number)

        params['is_complete'] = is_complete

        try:
            response = self.execute(http_method=http_method,
                                    url=uri,
                                    query_params=params)

            return {'status': response.status_code,
                    'data': json.loads(response.text)}
        except:
            raise UnknownException

    def get(self, slug):
        """

        :param slug: THe slug for the message thread
        :return:
        """

        http_method = "GET"
        endpoint = "ppp_loan_forgiveness_messages/{0}/".format(str(slug))

        uri = self.client.api_uri + endpoint

        try:
            response = self.execute(http_method=http_method,
                                    url=uri)

            return {'status': response.status_code,
                    'data': json.loads(response.text)}
        except:
            raise UnknownException

    def update(self, slug, document_type, document_name, document, message_text=''):
        """
        :param slug: The slug for the message thread
        :param document_type: Id of the document_type
        :param document: Path to a file to upload
        :param message_text: (optional) Message to include with the document
        :return:
        """
        http_method = "PUT"
        endpoint = "ppp_loan_forgiveness_message_reply/{0}/".format(str(slug))
        uri = self.client.api_uri + endpoint
        params = {'document_type': document_type, 'content': message_text, 'document_name': document_name}
        files = {'document': open(document, 'rb')}
        try:
            response = self.execute(http_method=http_method,
                                    url=uri,
                                    data=params,
                                    files=files)
            return {'status': response.status_code,
                    'data': json.loads(response.text)}
        except:
            raise UnknownException

    def update_with_multiple_files(self, slug, document_types, document_names, documents, message_text=''):
        """
        :param slug: The slug for the message thread
        :param document_types: Array of Id's of the document_types
        :param documents: Array of files to upload (Path to a file to upload for each element)
        :param message_text: (optional) Message to include with the document
        :return:
        """
        http_method = "PUT"
        endpoint = "ppp_loan_forgiveness_message_reply/{0}/".format(str(slug))
        uri = self.client.api_uri + endpoint
        params = {'document_type': document_types, 'content': message_text, 'document_name': document_names}
        #files = {'document': documents}

        files = []
        for document in documents:
            doc = ('document', document)
            files.append(doc)

        try:
            response = self.execute(http_method=http_method,
                                    url=uri,
                                    data=params,
                                    files=files)
            return {'status': response.status_code,
                    'data': json.loads(response.text)}
        except:
            raise UnknownException