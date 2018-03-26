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

from .resource import Resource


class DatabaseUpdate(Resource):
    """Represents a database update.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param collation: The collation of the database. If createMode is not
     Default, this value is ignored.
    :type collation: str
    :ivar creation_date: The creation date of the database (ISO8601 format).
    :vartype creation_date: datetime
    :ivar containment_state: The containment state of the database.
    :vartype containment_state: long
    :ivar current_service_objective_id: The current service level objective ID
     of the database. This is the ID of the service level objective that is
     currently active.
    :vartype current_service_objective_id: str
    :ivar database_id: The ID of the database.
    :vartype database_id: str
    :ivar earliest_restore_date: This records the earliest start date and time
     that restore is available for this database (ISO8601 format).
    :vartype earliest_restore_date: datetime
    :param create_mode: Specifies the mode of database creation.
     Default: regular database creation.
     Copy: creates a database as a copy of an existing database.
     sourceDatabaseId must be specified as the resource ID of the source
     database.
     OnlineSecondary/NonReadableSecondary: creates a database as a (readable or
     nonreadable) secondary replica of an existing database. sourceDatabaseId
     must be specified as the resource ID of the existing primary database.
     PointInTimeRestore: Creates a database by restoring a point in time backup
     of an existing database. sourceDatabaseId must be specified as the
     resource ID of the existing database, and restorePointInTime must be
     specified.
     Recovery: Creates a database by restoring a geo-replicated backup.
     sourceDatabaseId must be specified as the recoverable database resource ID
     to restore.
     Restore: Creates a database by restoring a backup of a deleted database.
     sourceDatabaseId must be specified. If sourceDatabaseId is the database's
     original resource ID, then sourceDatabaseDeletionDate must be specified.
     Otherwise sourceDatabaseId must be the restorable dropped database
     resource ID and sourceDatabaseDeletionDate is ignored. restorePointInTime
     may also be specified to restore from an earlier point in time.
     RestoreLongTermRetentionBackup: Creates a database by restoring from a
     long term retention vault. recoveryServicesRecoveryPointResourceId must be
     specified as the recovery point resource ID.
     Copy, NonReadableSecondary, OnlineSecondary and
     RestoreLongTermRetentionBackup are not supported for DataWarehouse
     edition. Possible values include: 'Copy', 'Default',
     'NonReadableSecondary', 'OnlineSecondary', 'PointInTimeRestore',
     'Recovery', 'Restore', 'RestoreLongTermRetentionBackup'
    :type create_mode: str or ~azure.mgmt.sql.models.CreateMode
    :param source_database_id: Conditional. If createMode is Copy,
     NonReadableSecondary, OnlineSecondary, PointInTimeRestore, Recovery, or
     Restore, then this value is required. Specifies the resource ID of the
     source database. If createMode is NonReadableSecondary or OnlineSecondary,
     the name of the source database must be the same as the new database being
     created.
    :type source_database_id: str
    :param source_database_deletion_date: Conditional. If createMode is
     Restore and sourceDatabaseId is the deleted database's original resource
     id when it existed (as opposed to its current restorable dropped database
     id), then this value is required. Specifies the time that the database was
     deleted.
    :type source_database_deletion_date: datetime
    :param restore_point_in_time: Conditional. If createMode is
     PointInTimeRestore, this value is required. If createMode is Restore, this
     value is optional. Specifies the point in time (ISO8601 format) of the
     source database that will be restored to create the new database. Must be
     greater than or equal to the source database's earliestRestoreDate value.
    :type restore_point_in_time: datetime
    :param recovery_services_recovery_point_resource_id: Conditional. If
     createMode is RestoreLongTermRetentionBackup, then this value is required.
     Specifies the resource ID of the recovery point to restore from.
    :type recovery_services_recovery_point_resource_id: str
    :param edition: The edition of the database. The DatabaseEditions
     enumeration contains all the valid editions. If createMode is
     NonReadableSecondary or OnlineSecondary, this value is ignored. To see
     possible values, query the capabilities API
     (/subscriptions/{subscriptionId}/providers/Microsoft.Sql/locations/{locationID}/capabilities)
     referred to by operationId: "Capabilities_ListByLocation." or use the
     Azure CLI command `az sql db list-editions -l westus --query [].name`.
     Possible values include: 'Web', 'Business', 'Basic', 'Standard',
     'Premium', 'PremiumRS', 'Free', 'Stretch', 'DataWarehouse', 'System',
     'System2'
    :type edition: str or ~azure.mgmt.sql.models.DatabaseEdition
    :param max_size_bytes: The max size of the database expressed in bytes. If
     createMode is not Default, this value is ignored. To see possible values,
     query the capabilities API
     (/subscriptions/{subscriptionId}/providers/Microsoft.Sql/locations/{locationID}/capabilities)
     referred to by operationId: "Capabilities_ListByLocation."
    :type max_size_bytes: str
    :param requested_service_objective_id: The configured service level
     objective ID of the database. This is the service level objective that is
     in the process of being applied to the database. Once successfully
     updated, it will match the value of currentServiceObjectiveId property. If
     requestedServiceObjectiveId and requestedServiceObjectiveName are both
     updated, the value of requestedServiceObjectiveId overrides the value of
     requestedServiceObjectiveName. To see possible values, query the
     capabilities API
     (/subscriptions/{subscriptionId}/providers/Microsoft.Sql/locations/{locationID}/capabilities)
     referred to by operationId: "Capabilities_ListByLocation." or use the
     Azure CLI command `az sql db list-editions --location <location> --query
     [].supportedServiceLevelObjectives[].name` .
    :type requested_service_objective_id: str
    :param requested_service_objective_name: The name of the configured
     service level objective of the database. This is the service level
     objective that is in the process of being applied to the database. Once
     successfully updated, it will match the value of serviceLevelObjective
     property. To see possible values, query the capabilities API
     (/subscriptions/{subscriptionId}/providers/Microsoft.Sql/locations/{locationID}/capabilities)
     referred to by operationId: "Capabilities_ListByLocation." or use the
     Azure CLI command `az sql db list-editions --location <location> --query
     [].supportedServiceLevelObjectives[].name`. Possible values include:
     'System', 'System0', 'System1', 'System2', 'System3', 'System4',
     'System2L', 'System3L', 'System4L', 'Free', 'Basic', 'S0', 'S1', 'S2',
     'S3', 'S4', 'S6', 'S7', 'S9', 'S12', 'P1', 'P2', 'P3', 'P4', 'P6', 'P11',
     'P15', 'PRS1', 'PRS2', 'PRS4', 'PRS6', 'DW100', 'DW200', 'DW300', 'DW400',
     'DW500', 'DW600', 'DW1000', 'DW1200', 'DW1000c', 'DW1500', 'DW1500c',
     'DW2000', 'DW2000c', 'DW3000', 'DW2500c', 'DW3000c', 'DW6000', 'DW5000c',
     'DW6000c', 'DW7500c', 'DW10000c', 'DW15000c', 'DW30000c', 'DS100',
     'DS200', 'DS300', 'DS400', 'DS500', 'DS600', 'DS1000', 'DS1200', 'DS1500',
     'DS2000', 'ElasticPool'
    :type requested_service_objective_name: str or
     ~azure.mgmt.sql.models.ServiceObjectiveName
    :ivar service_level_objective: The current service level objective of the
     database. Possible values include: 'System', 'System0', 'System1',
     'System2', 'System3', 'System4', 'System2L', 'System3L', 'System4L',
     'Free', 'Basic', 'S0', 'S1', 'S2', 'S3', 'S4', 'S6', 'S7', 'S9', 'S12',
     'P1', 'P2', 'P3', 'P4', 'P6', 'P11', 'P15', 'PRS1', 'PRS2', 'PRS4',
     'PRS6', 'DW100', 'DW200', 'DW300', 'DW400', 'DW500', 'DW600', 'DW1000',
     'DW1200', 'DW1000c', 'DW1500', 'DW1500c', 'DW2000', 'DW2000c', 'DW3000',
     'DW2500c', 'DW3000c', 'DW6000', 'DW5000c', 'DW6000c', 'DW7500c',
     'DW10000c', 'DW15000c', 'DW30000c', 'DS100', 'DS200', 'DS300', 'DS400',
     'DS500', 'DS600', 'DS1000', 'DS1200', 'DS1500', 'DS2000', 'ElasticPool'
    :vartype service_level_objective: str or
     ~azure.mgmt.sql.models.ServiceObjectiveName
    :ivar status: The status of the database.
    :vartype status: str
    :param elastic_pool_name: The name of the elastic pool the database is in.
     If elasticPoolName and requestedServiceObjectiveName are both updated, the
     value of requestedServiceObjectiveName is ignored. Not supported for
     DataWarehouse edition.
    :type elastic_pool_name: str
    :ivar default_secondary_location: The default secondary region for this
     database.
    :vartype default_secondary_location: str
    :ivar service_tier_advisors: The list of service tier advisors for this
     database. Expanded property
    :vartype service_tier_advisors:
     list[~azure.mgmt.sql.models.ServiceTierAdvisor]
    :ivar transparent_data_encryption: The transparent data encryption info
     for this database.
    :vartype transparent_data_encryption:
     list[~azure.mgmt.sql.models.TransparentDataEncryption]
    :ivar recommended_index: The recommended indices for this database.
    :vartype recommended_index: list[~azure.mgmt.sql.models.RecommendedIndex]
    :ivar failover_group_id: The resource identifier of the failover group
     containing this database.
    :vartype failover_group_id: str
    :param read_scale: Conditional. If the database is a geo-secondary,
     readScale indicates whether read-only connections are allowed to this
     database or not. Not supported for DataWarehouse edition. Possible values
     include: 'Enabled', 'Disabled'
    :type read_scale: str or ~azure.mgmt.sql.models.ReadScale
    :param sample_name: Indicates the name of the sample schema to apply when
     creating this database. If createMode is not Default, this value is
     ignored. Not supported for DataWarehouse edition. Possible values include:
     'AdventureWorksLT'
    :type sample_name: str or ~azure.mgmt.sql.models.SampleName
    :param zone_redundant: Whether or not this database is zone redundant,
     which means the replicas of this database will be spread across multiple
     availability zones.
    :type zone_redundant: bool
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'creation_date': {'readonly': True},
        'containment_state': {'readonly': True},
        'current_service_objective_id': {'readonly': True},
        'database_id': {'readonly': True},
        'earliest_restore_date': {'readonly': True},
        'service_level_objective': {'readonly': True},
        'status': {'readonly': True},
        'default_secondary_location': {'readonly': True},
        'service_tier_advisors': {'readonly': True},
        'transparent_data_encryption': {'readonly': True},
        'recommended_index': {'readonly': True},
        'failover_group_id': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'collation': {'key': 'properties.collation', 'type': 'str'},
        'creation_date': {'key': 'properties.creationDate', 'type': 'iso-8601'},
        'containment_state': {'key': 'properties.containmentState', 'type': 'long'},
        'current_service_objective_id': {'key': 'properties.currentServiceObjectiveId', 'type': 'str'},
        'database_id': {'key': 'properties.databaseId', 'type': 'str'},
        'earliest_restore_date': {'key': 'properties.earliestRestoreDate', 'type': 'iso-8601'},
        'create_mode': {'key': 'properties.createMode', 'type': 'str'},
        'source_database_id': {'key': 'properties.sourceDatabaseId', 'type': 'str'},
        'source_database_deletion_date': {'key': 'properties.sourceDatabaseDeletionDate', 'type': 'iso-8601'},
        'restore_point_in_time': {'key': 'properties.restorePointInTime', 'type': 'iso-8601'},
        'recovery_services_recovery_point_resource_id': {'key': 'properties.recoveryServicesRecoveryPointResourceId', 'type': 'str'},
        'edition': {'key': 'properties.edition', 'type': 'str'},
        'max_size_bytes': {'key': 'properties.maxSizeBytes', 'type': 'str'},
        'requested_service_objective_id': {'key': 'properties.requestedServiceObjectiveId', 'type': 'str'},
        'requested_service_objective_name': {'key': 'properties.requestedServiceObjectiveName', 'type': 'str'},
        'service_level_objective': {'key': 'properties.serviceLevelObjective', 'type': 'str'},
        'status': {'key': 'properties.status', 'type': 'str'},
        'elastic_pool_name': {'key': 'properties.elasticPoolName', 'type': 'str'},
        'default_secondary_location': {'key': 'properties.defaultSecondaryLocation', 'type': 'str'},
        'service_tier_advisors': {'key': 'properties.serviceTierAdvisors', 'type': '[ServiceTierAdvisor]'},
        'transparent_data_encryption': {'key': 'properties.transparentDataEncryption', 'type': '[TransparentDataEncryption]'},
        'recommended_index': {'key': 'properties.recommendedIndex', 'type': '[RecommendedIndex]'},
        'failover_group_id': {'key': 'properties.failoverGroupId', 'type': 'str'},
        'read_scale': {'key': 'properties.readScale', 'type': 'ReadScale'},
        'sample_name': {'key': 'properties.sampleName', 'type': 'str'},
        'zone_redundant': {'key': 'properties.zoneRedundant', 'type': 'bool'},
    }

    def __init__(self, *, tags=None, collation: str=None, create_mode=None, source_database_id: str=None, source_database_deletion_date=None, restore_point_in_time=None, recovery_services_recovery_point_resource_id: str=None, edition=None, max_size_bytes: str=None, requested_service_objective_id: str=None, requested_service_objective_name=None, elastic_pool_name: str=None, read_scale=None, sample_name=None, zone_redundant: bool=None, **kwargs) -> None:
        super(DatabaseUpdate, self).__init__(, **kwargs)
        self.tags = tags
        self.collation = collation
        self.creation_date = None
        self.containment_state = None
        self.current_service_objective_id = None
        self.database_id = None
        self.earliest_restore_date = None
        self.create_mode = create_mode
        self.source_database_id = source_database_id
        self.source_database_deletion_date = source_database_deletion_date
        self.restore_point_in_time = restore_point_in_time
        self.recovery_services_recovery_point_resource_id = recovery_services_recovery_point_resource_id
        self.edition = edition
        self.max_size_bytes = max_size_bytes
        self.requested_service_objective_id = requested_service_objective_id
        self.requested_service_objective_name = requested_service_objective_name
        self.service_level_objective = None
        self.status = None
        self.elastic_pool_name = elastic_pool_name
        self.default_secondary_location = None
        self.service_tier_advisors = None
        self.transparent_data_encryption = None
        self.recommended_index = None
        self.failover_group_id = None
        self.read_scale = read_scale
        self.sample_name = sample_name
        self.zone_redundant = zone_redundant
