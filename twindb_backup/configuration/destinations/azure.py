"""Azure Storage destination configuration"""


class AzureConfig(object):
    """Azure Storage configuration."""
    __attr__ = [
        'azure_access_key',
        'azure_account',
        'bucket',
        'endpoint'
    ]

    def __init__(self, **kwargs):

        # give default value for endpoint
        setattr(self, '_endpoint', 'core.windows.net')
        for opt in self.__attr__:
            setattr(self, '_%s' % opt, kwargs.get(opt))

    @property
    def azure_access_key(self):
        """AZURE_ACCESS_KEY"""
        return getattr(self, '_azure_access_key')

    @property
    def azure_account(self):
        """AZURE_ACCOUNT"""
        return getattr(self, '_azure_account')

    @property
    def bucket(self):
        """Azure bucket"""
        return getattr(self, '_bucket')

    @property
    def endpoint(self):
        """ Azure Endpoint"""
        return getattr(self, '_endpoint')
