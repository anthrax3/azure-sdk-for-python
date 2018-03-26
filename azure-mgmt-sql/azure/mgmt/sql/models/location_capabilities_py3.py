# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class LocationCapabilities(Model):
    """The capabilities for a location.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: The location name.
    :vartype name: str
    :ivar status: Azure SQL Database's status for the location. Possible
     values include: 'Visible', 'Available', 'Default', 'Disabled'
    :vartype status: str or ~azure.mgmt.sql.models.CapabilityStatus
    :ivar supported_server_versions: The list of supported server versions.
    :vartype supported_server_versions:
     list[~azure.mgmt.sql.models.ServerVersionCapability]
    """

    _validation = {
        'name': {'readonly': True},
        'status': {'readonly': True},
        'supported_server_versions': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'status': {'key': 'status', 'type': 'CapabilityStatus'},
        'supported_server_versions': {'key': 'supportedServerVersions', 'type': '[ServerVersionCapability]'},
    }

    def __init__(self, **kwargs) -> None:
        super(LocationCapabilities, self).__init__(**kwargs)
        self.name = None
        self.status = None
        self.supported_server_versions = None
