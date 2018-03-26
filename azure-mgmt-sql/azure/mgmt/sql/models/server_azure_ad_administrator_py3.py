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


class ServerAzureADAdministrator(ProxyResource):
    """An server Active Directory Administrator.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar administrator_type: Required. The type of administrator. Default
     value: "ActiveDirectory" .
    :vartype administrator_type: str
    :param login: Required. The server administrator login value.
    :type login: str
    :param sid: Required. The server administrator Sid (Secure ID).
    :type sid: str
    :param tenant_id: Required. The server Active Directory Administrator
     tenant id.
    :type tenant_id: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'administrator_type': {'required': True, 'constant': True},
        'login': {'required': True},
        'sid': {'required': True},
        'tenant_id': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'administrator_type': {'key': 'properties.administratorType', 'type': 'str'},
        'login': {'key': 'properties.login', 'type': 'str'},
        'sid': {'key': 'properties.sid', 'type': 'str'},
        'tenant_id': {'key': 'properties.tenantId', 'type': 'str'},
    }

    administrator_type = "ActiveDirectory"

    def __init__(self, *, login: str, sid: str, tenant_id: str, **kwargs) -> None:
        super(ServerAzureADAdministrator, self).__init__(, **kwargs)
        self.login = login
        self.sid = sid
        self.tenant_id = tenant_id
