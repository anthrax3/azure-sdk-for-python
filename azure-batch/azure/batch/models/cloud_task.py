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


class CloudTask(Model):
    """An Azure Batch task.

    Batch will retry tasks when a recovery operation is triggered on a compute
    node. Examples of recovery operations include (but are not limited to) when
    an unhealthy compute node is rebooted or a compute node disappeared due to
    host failure. Retries due to recovery operations are independent of and are
    not counted against the maxTaskRetryCount. Even if the maxTaskRetryCount is
    0, an internal retry due to a recovery operation may occur. Because of
    this, all tasks should be idempotent. This means tasks need to tolerate
    being interrupted and restarted without causing any corruption or duplicate
    data. The best practice for long running tasks is to use some form of
    checkpointing.

    :param id: A string that uniquely identifies the task within the job. The
     ID can contain any combination of alphanumeric characters including
     hyphens and underscores, and cannot contain more than 64 characters.
    :type id: str
    :param display_name: A display name for the task. The display name need
     not be unique and can contain any Unicode characters up to a maximum
     length of 1024.
    :type display_name: str
    :param url: The URL of the task.
    :type url: str
    :param e_tag: The ETag of the task. This is an opaque string. You can use
     it to detect whether the task has changed between requests. In particular,
     you can be pass the ETag when updating a task to specify that your changes
     should take effect only if nobody else has modified the task in the
     meantime.
    :type e_tag: str
    :param last_modified: The last modified time of the task.
    :type last_modified: datetime
    :param creation_time: The creation time of the task.
    :type creation_time: datetime
    :param exit_conditions: How the Batch service should respond when the task
     completes.
    :type exit_conditions: ~azure.batch.models.ExitConditions
    :param state: The current state of the task. Possible values include:
     'active', 'preparing', 'running', 'completed'
    :type state: str or ~azure.batch.models.TaskState
    :param state_transition_time: The time at which the task entered its
     current state.
    :type state_transition_time: datetime
    :param previous_state: The previous state of the task. This property is
     not set if the task is in its initial Active state. Possible values
     include: 'active', 'preparing', 'running', 'completed'
    :type previous_state: str or ~azure.batch.models.TaskState
    :param previous_state_transition_time: The time at which the task entered
     its previous state. This property is not set if the task is in its initial
     Active state.
    :type previous_state_transition_time: datetime
    :param command_line: The command line of the task. For multi-instance
     tasks, the command line is executed as the primary task, after the primary
     task and all subtasks have finished executing the coordination command
     line. The command line does not run under a shell, and therefore cannot
     take advantage of shell features such as environment variable expansion.
     If you want to take advantage of such features, you should invoke the
     shell in the command line, for example using "cmd /c MyCommand" in Windows
     or "/bin/sh -c MyCommand" in Linux. If the command line refers to file
     paths, it should use a relative path (relative to the task working
     directory), or use the Batch provided environment variable
     (https://docs.microsoft.com/en-us/azure/batch/batch-compute-node-environment-variables).
    :type command_line: str
    :param container_settings: The settings for the container under which the
     task runs. If the pool that will run this task has containerConfiguration
     set, this must be set as well. If the pool that will run this task doesn't
     have containerConfiguration set, this must not be set. When this is
     specified, all directories recursively below the AZ_BATCH_NODE_ROOT_DIR
     (the root of Azure Batch directories on the node) are mapped into the
     container, all task environment variables are mapped into the container,
     and the task command line is executed in the container.
    :type container_settings: ~azure.batch.models.TaskContainerSettings
    :param resource_files: A list of files that the Batch service will
     download to the compute node before running the command line. For
     multi-instance tasks, the resource files will only be downloaded to the
     compute node on which the primary task is executed.
    :type resource_files: list[~azure.batch.models.ResourceFile]
    :param output_files: A list of files that the Batch service will upload
     from the compute node after running the command line. For multi-instance
     tasks, the files will only be uploaded from the compute node on which the
     primary task is executed.
    :type output_files: list[~azure.batch.models.OutputFile]
    :param environment_settings: A list of environment variable settings for
     the task.
    :type environment_settings: list[~azure.batch.models.EnvironmentSetting]
    :param affinity_info: A locality hint that can be used by the Batch
     service to select a compute node on which to start the new task.
    :type affinity_info: ~azure.batch.models.AffinityInformation
    :param constraints: The execution constraints that apply to this task.
    :type constraints: ~azure.batch.models.TaskConstraints
    :param user_identity: The user identity under which the task runs. If
     omitted, the task runs as a non-administrative user unique to the task.
    :type user_identity: ~azure.batch.models.UserIdentity
    :param execution_info: Information about the execution of the task.
    :type execution_info: ~azure.batch.models.TaskExecutionInformation
    :param node_info: Information about the compute node on which the task
     ran.
    :type node_info: ~azure.batch.models.ComputeNodeInformation
    :param multi_instance_settings: An object that indicates that the task is
     a multi-instance task, and contains information about how to run the
     multi-instance task.
    :type multi_instance_settings: ~azure.batch.models.MultiInstanceSettings
    :param stats: Resource usage statistics for the task.
    :type stats: ~azure.batch.models.TaskStatistics
    :param depends_on: The tasks that this task depends on. This task will not
     be scheduled until all tasks that it depends on have completed
     successfully. If any of those tasks fail and exhaust their retry counts,
     this task will never be scheduled.
    :type depends_on: ~azure.batch.models.TaskDependencies
    :param application_package_references: A list of application packages that
     the Batch service will deploy to the compute node before running the
     command line. Application packages are downloaded and deployed to a shared
     directory, not the task working directory. Therefore, if a referenced
     package is already on the compute node, and is up to date, then it is not
     re-downloaded; the existing copy on the compute node is used. If a
     referenced application package cannot be installed, for example because
     the package has been deleted or because download failed, the task fails.
    :type application_package_references:
     list[~azure.batch.models.ApplicationPackageReference]
    :param authentication_token_settings: The settings for an authentication
     token that the task can use to perform Batch service operations. If this
     property is set, the Batch service provides the task with an
     authentication token which can be used to authenticate Batch service
     operations without requiring an account access key. The token is provided
     via the AZ_BATCH_AUTHENTICATION_TOKEN environment variable. The operations
     that the task can carry out using the token depend on the settings. For
     example, a task can request job permissions in order to add other tasks to
     the job, or check the status of the job or of other tasks under the job.
    :type authentication_token_settings:
     ~azure.batch.models.AuthenticationTokenSettings
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'e_tag': {'key': 'eTag', 'type': 'str'},
        'last_modified': {'key': 'lastModified', 'type': 'iso-8601'},
        'creation_time': {'key': 'creationTime', 'type': 'iso-8601'},
        'exit_conditions': {'key': 'exitConditions', 'type': 'ExitConditions'},
        'state': {'key': 'state', 'type': 'TaskState'},
        'state_transition_time': {'key': 'stateTransitionTime', 'type': 'iso-8601'},
        'previous_state': {'key': 'previousState', 'type': 'TaskState'},
        'previous_state_transition_time': {'key': 'previousStateTransitionTime', 'type': 'iso-8601'},
        'command_line': {'key': 'commandLine', 'type': 'str'},
        'container_settings': {'key': 'containerSettings', 'type': 'TaskContainerSettings'},
        'resource_files': {'key': 'resourceFiles', 'type': '[ResourceFile]'},
        'output_files': {'key': 'outputFiles', 'type': '[OutputFile]'},
        'environment_settings': {'key': 'environmentSettings', 'type': '[EnvironmentSetting]'},
        'affinity_info': {'key': 'affinityInfo', 'type': 'AffinityInformation'},
        'constraints': {'key': 'constraints', 'type': 'TaskConstraints'},
        'user_identity': {'key': 'userIdentity', 'type': 'UserIdentity'},
        'execution_info': {'key': 'executionInfo', 'type': 'TaskExecutionInformation'},
        'node_info': {'key': 'nodeInfo', 'type': 'ComputeNodeInformation'},
        'multi_instance_settings': {'key': 'multiInstanceSettings', 'type': 'MultiInstanceSettings'},
        'stats': {'key': 'stats', 'type': 'TaskStatistics'},
        'depends_on': {'key': 'dependsOn', 'type': 'TaskDependencies'},
        'application_package_references': {'key': 'applicationPackageReferences', 'type': '[ApplicationPackageReference]'},
        'authentication_token_settings': {'key': 'authenticationTokenSettings', 'type': 'AuthenticationTokenSettings'},
    }

    def __init__(self, **kwargs):
        super(CloudTask, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.display_name = kwargs.get('display_name', None)
        self.url = kwargs.get('url', None)
        self.e_tag = kwargs.get('e_tag', None)
        self.last_modified = kwargs.get('last_modified', None)
        self.creation_time = kwargs.get('creation_time', None)
        self.exit_conditions = kwargs.get('exit_conditions', None)
        self.state = kwargs.get('state', None)
        self.state_transition_time = kwargs.get('state_transition_time', None)
        self.previous_state = kwargs.get('previous_state', None)
        self.previous_state_transition_time = kwargs.get('previous_state_transition_time', None)
        self.command_line = kwargs.get('command_line', None)
        self.container_settings = kwargs.get('container_settings', None)
        self.resource_files = kwargs.get('resource_files', None)
        self.output_files = kwargs.get('output_files', None)
        self.environment_settings = kwargs.get('environment_settings', None)
        self.affinity_info = kwargs.get('affinity_info', None)
        self.constraints = kwargs.get('constraints', None)
        self.user_identity = kwargs.get('user_identity', None)
        self.execution_info = kwargs.get('execution_info', None)
        self.node_info = kwargs.get('node_info', None)
        self.multi_instance_settings = kwargs.get('multi_instance_settings', None)
        self.stats = kwargs.get('stats', None)
        self.depends_on = kwargs.get('depends_on', None)
        self.application_package_references = kwargs.get('application_package_references', None)
        self.authentication_token_settings = kwargs.get('authentication_token_settings', None)
