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


class JobCollectionItem(ProxyResource):
    """Job collection item properties.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource Id for the resource
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :ivar runbook: The runbook association.
    :vartype runbook: ~azure.mgmt.automation.models.RunbookAssociationProperty
    :ivar job_id: The id of the job.
    :vartype job_id: str
    :ivar creation_time: The creation time of the job.
    :vartype creation_time: datetime
    :ivar status: The status of the job. Possible values include: 'New',
     'Activating', 'Running', 'Completed', 'Failed', 'Stopped', 'Blocked',
     'Suspended', 'Disconnected', 'Suspending', 'Stopping', 'Resuming',
     'Removing'
    :vartype status: str or ~azure.mgmt.automation.models.JobStatus
    :ivar start_time: The start time of the job.
    :vartype start_time: datetime
    :ivar end_time: The end time of the job.
    :vartype end_time: datetime
    :ivar last_modified_time: The last modified time of the job.
    :vartype last_modified_time: datetime
    :param provisioning_state: The current provisioning state of the job.
    :type provisioning_state:
     ~azure.mgmt.automation.models.JobProvisioningStateProperty
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'runbook': {'readonly': True},
        'job_id': {'readonly': True},
        'creation_time': {'readonly': True},
        'status': {'readonly': True},
        'start_time': {'readonly': True},
        'end_time': {'readonly': True},
        'last_modified_time': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'runbook': {'key': 'properties.runbook', 'type': 'RunbookAssociationProperty'},
        'job_id': {'key': 'properties.jobId', 'type': 'str'},
        'creation_time': {'key': 'properties.creationTime', 'type': 'iso-8601'},
        'status': {'key': 'properties.status', 'type': 'str'},
        'start_time': {'key': 'properties.startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'properties.endTime', 'type': 'iso-8601'},
        'last_modified_time': {'key': 'properties.lastModifiedTime', 'type': 'iso-8601'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'JobProvisioningStateProperty'},
    }

    def __init__(self, provisioning_state=None):
        super(JobCollectionItem, self).__init__()
        self.runbook = None
        self.job_id = None
        self.creation_time = None
        self.status = None
        self.start_time = None
        self.end_time = None
        self.last_modified_time = None
        self.provisioning_state = provisioning_state
