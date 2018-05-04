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

from .multiple_pipeline_trigger import MultiplePipelineTrigger


class BlobEventsTrigger(MultiplePipelineTrigger):
    """Trigger that runs everytime a Blob event occurs.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param description: Trigger description.
    :type description: str
    :ivar runtime_state: Indicates if trigger is running or not. Updated when
     Start/Stop APIs are called on the Trigger. Possible values include:
     'Started', 'Stopped', 'Disabled'
    :vartype runtime_state: str or
     ~azure.mgmt.datafactory.models.TriggerRuntimeState
    :param type: Required. Constant filled by server.
    :type type: str
    :param pipelines: Pipelines that need to be started.
    :type pipelines:
     list[~azure.mgmt.datafactory.models.TriggerPipelineReference]
    :param blob_path: Required. Expression to determine if trigger should
     fire. For example, @startswith('/records/blobs/december/') will only fire
     the trigger for blobs in the december folder under the records container.
    :type blob_path: str
    :param events: Required. The type of events that cause this trigger to
     fire.
    :type events: list[str or ~azure.mgmt.datafactory.models.BlobEventTypes]
    :param scope: Required. The ARM resource ID of the Storage Account.
    :type scope: str
    """

    _validation = {
        'runtime_state': {'readonly': True},
        'type': {'required': True},
        'blob_path': {'required': True},
        'events': {'required': True},
        'scope': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'description': {'key': 'description', 'type': 'str'},
        'runtime_state': {'key': 'runtimeState', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'pipelines': {'key': 'pipelines', 'type': '[TriggerPipelineReference]'},
        'blob_path': {'key': 'typeProperties.blobPath', 'type': 'str'},
        'events': {'key': 'typeProperties.events', 'type': '[str]'},
        'scope': {'key': 'typeProperties.scope', 'type': 'str'},
    }

    def __init__(self, *, blob_path: str, events, scope: str, additional_properties=None, description: str=None, pipelines=None, **kwargs) -> None:
        super(BlobEventsTrigger, self).__init__(additional_properties=additional_properties, description=description, pipelines=pipelines, **kwargs)
        self.blob_path = blob_path
        self.events = events
        self.scope = scope
        self.type = 'BlobEventsTrigger'