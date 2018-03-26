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


class ElasticPoolPerDatabaseMaxDtuCapability(Model):
    """The max per-database DTU capability.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar limit: The maximum DTUs per database.
    :vartype limit: long
    :ivar status: The status of the capability. Possible values include:
     'Visible', 'Available', 'Default', 'Disabled'
    :vartype status: str or ~azure.mgmt.sql.models.CapabilityStatus
    :ivar supported_per_database_min_dtus: The list of supported min database
     DTUs.
    :vartype supported_per_database_min_dtus:
     list[~azure.mgmt.sql.models.ElasticPoolPerDatabaseMinDtuCapability]
    """

    _validation = {
        'limit': {'readonly': True},
        'status': {'readonly': True},
        'supported_per_database_min_dtus': {'readonly': True},
    }

    _attribute_map = {
        'limit': {'key': 'limit', 'type': 'long'},
        'status': {'key': 'status', 'type': 'CapabilityStatus'},
        'supported_per_database_min_dtus': {'key': 'supportedPerDatabaseMinDtus', 'type': '[ElasticPoolPerDatabaseMinDtuCapability]'},
    }

    def __init__(self, **kwargs):
        super(ElasticPoolPerDatabaseMaxDtuCapability, self).__init__(**kwargs)
        self.limit = None
        self.status = None
        self.supported_per_database_min_dtus = None
