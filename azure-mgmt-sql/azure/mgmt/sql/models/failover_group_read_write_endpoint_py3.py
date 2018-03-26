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


class FailoverGroupReadWriteEndpoint(Model):
    """Read-write endpoint of the failover group instance.

    All required parameters must be populated in order to send to Azure.

    :param failover_policy: Required. Failover policy of the read-write
     endpoint for the failover group. If failoverPolicy is Automatic then
     failoverWithDataLossGracePeriodMinutes is required. Possible values
     include: 'Manual', 'Automatic'
    :type failover_policy: str or
     ~azure.mgmt.sql.models.ReadWriteEndpointFailoverPolicy
    :param failover_with_data_loss_grace_period_minutes: Grace period before
     failover with data loss is attempted for the read-write endpoint. If
     failoverPolicy is Automatic then failoverWithDataLossGracePeriodMinutes is
     required.
    :type failover_with_data_loss_grace_period_minutes: int
    """

    _validation = {
        'failover_policy': {'required': True},
    }

    _attribute_map = {
        'failover_policy': {'key': 'failoverPolicy', 'type': 'str'},
        'failover_with_data_loss_grace_period_minutes': {'key': 'failoverWithDataLossGracePeriodMinutes', 'type': 'int'},
    }

    def __init__(self, *, failover_policy, failover_with_data_loss_grace_period_minutes: int=None, **kwargs) -> None:
        super(FailoverGroupReadWriteEndpoint, self).__init__(**kwargs)
        self.failover_policy = failover_policy
        self.failover_with_data_loss_grace_period_minutes = failover_with_data_loss_grace_period_minutes
