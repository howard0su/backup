from twindb_backup import LOG
from twindb_backup.destination.base_destination import BaseDestination
from twindb_backup.destination.exceptions import AzureDestinationError, \
    FileNotFound


class Azure(BaseDestination):

    def __init__(self, **kwargs):
        self._bucket = kwargs.get('bucket')