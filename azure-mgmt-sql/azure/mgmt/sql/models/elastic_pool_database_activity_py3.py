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

from .proxy_resource import ProxyResource


class ElasticPoolDatabaseActivity(ProxyResource):
    """Represents the activity on an elastic pool.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: The geo-location where the resource lives
    :type location: str
    :ivar database_name: The database name.
    :vartype database_name: str
    :ivar end_time: The time the operation finished (ISO8601 format).
    :vartype end_time: datetime
    :ivar error_code: The error code if available.
    :vartype error_code: int
    :ivar error_message: The error message if available.
    :vartype error_message: str
    :ivar error_severity: The error severity if available.
    :vartype error_severity: int
    :ivar operation: The operation name.
    :vartype operation: str
    :ivar operation_id: The unique operation ID.
    :vartype operation_id: str
    :ivar percent_complete: The percentage complete if available.
    :vartype percent_complete: int
    :ivar requested_elastic_pool_name: The name for the elastic pool the
     database is moving into if available.
    :vartype requested_elastic_pool_name: str
    :ivar current_elastic_pool_name: The name of the current elastic pool the
     database is in if available.
    :vartype current_elastic_pool_name: str
    :ivar current_service_objective: The name of the current service objective
     if available.
    :vartype current_service_objective: str
    :ivar requested_service_objective: The name of the requested service
     objective if available.
    :vartype requested_service_objective: str
    :ivar server_name: The name of the server the elastic pool is in.
    :vartype server_name: str
    :ivar start_time: The time the operation started (ISO8601 format).
    :vartype start_time: datetime
    :ivar state: The current state of the operation.
    :vartype state: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'database_name': {'readonly': True},
        'end_time': {'readonly': True},
        'error_code': {'readonly': True},
        'error_message': {'readonly': True},
        'error_severity': {'readonly': True},
        'operation': {'readonly': True},
        'operation_id': {'readonly': True},
        'percent_complete': {'readonly': True},
        'requested_elastic_pool_name': {'readonly': True},
        'current_elastic_pool_name': {'readonly': True},
        'current_service_objective': {'readonly': True},
        'requested_service_objective': {'readonly': True},
        'server_name': {'readonly': True},
        'start_time': {'readonly': True},
        'state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'database_name': {'key': 'properties.databaseName', 'type': 'str'},
        'end_time': {'key': 'properties.endTime', 'type': 'iso-8601'},
        'error_code': {'key': 'properties.errorCode', 'type': 'int'},
        'error_message': {'key': 'properties.errorMessage', 'type': 'str'},
        'error_severity': {'key': 'properties.errorSeverity', 'type': 'int'},
        'operation': {'key': 'properties.operation', 'type': 'str'},
        'operation_id': {'key': 'properties.operationId', 'type': 'str'},
        'percent_complete': {'key': 'properties.percentComplete', 'type': 'int'},
        'requested_elastic_pool_name': {'key': 'properties.requestedElasticPoolName', 'type': 'str'},
        'current_elastic_pool_name': {'key': 'properties.currentElasticPoolName', 'type': 'str'},
        'current_service_objective': {'key': 'properties.currentServiceObjective', 'type': 'str'},
        'requested_service_objective': {'key': 'properties.requestedServiceObjective', 'type': 'str'},
        'server_name': {'key': 'properties.serverName', 'type': 'str'},
        'start_time': {'key': 'properties.startTime', 'type': 'iso-8601'},
        'state': {'key': 'properties.state', 'type': 'str'},
    }

    def __init__(self, *, location: str=None, **kwargs) -> None:
        super(ElasticPoolDatabaseActivity, self).__init__(, **kwargs)
        self.location = location
        self.database_name = None
        self.end_time = None
        self.error_code = None
        self.error_message = None
        self.error_severity = None
        self.operation = None
        self.operation_id = None
        self.percent_complete = None
        self.requested_elastic_pool_name = None
        self.current_elastic_pool_name = None
        self.current_service_objective = None
        self.requested_service_objective = None
        self.server_name = None
        self.start_time = None
        self.state = None
