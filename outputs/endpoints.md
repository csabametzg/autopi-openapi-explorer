# AutoPi OpenAPI Endpoints

## /addons/

Methods: GET

## /addons/{id}/

Methods: GET

## /addons/{id}/install/

Methods: POST

## /addons/{id}/uninstall/

Methods: POST

## /auth/account/

Methods: GET, PUT, PATCH

## /auth/account/customers/

Methods: GET, POST

## /auth/account/customers/{id}/

Methods: GET, PUT, PATCH, DELETE

## /auth/account/users/

Methods: GET, POST

## /auth/account/users/{id}/

Methods: GET, PUT, PATCH, DELETE

## /auth/account/v2/users/

Methods: GET, POST

## /auth/account/v2/users/{id}/

Methods: GET, PUT, PATCH, DELETE

## /auth/account/v2/users/{user_pk}/permissions/

Methods: GET, POST

## /auth/account/v2/users/{user_pk}/permissions/{id}/

Methods: GET, PUT, PATCH, DELETE

## /auth/account/v3/users/

Methods: GET, POST

## /auth/account/v3/users/groups/

Methods: GET

## /auth/account/v3/users/{id}/

Methods: GET, PUT, PATCH, DELETE

## /auth/account/v3/users/{user_pk}/permissions/

Methods: GET, POST

## /auth/account/v3/users/{user_pk}/permissions/{id}/

Methods: GET, PUT, PATCH, DELETE

## /auth/api_tokens/

Methods: GET, POST

## /auth/api_tokens/{id}/

Methods: DELETE

## /auth/featureflags/

Methods: GET

## /auth/login/

Methods: POST

## /auth/logout/

Methods: GET, POST

## /auth/mfa/totp-devices/

Methods: GET

## /auth/mfa/totp-devices/onboard/start/

Methods: POST

## /auth/mfa/totp-devices/{id}/disable/

Methods: POST

## /auth/mfa/totp-devices/{id}/onboard/confirm/

Methods: POST

## /auth/mfa/totp-devices/{id}/recovery_codes/regenerate/

Methods: POST

## /auth/mfa/verify/

Methods: POST

## /auth/password/change/

Methods: POST

## /auth/password/reset/

Methods: POST

## /auth/password/reset/confirm/

Methods: POST

## /auth/register/

Methods: POST

## /auth/register/verify-email/

Methods: POST

## /auth/resend-confirm-email/

Methods: POST

## /auth/user/

Methods: GET, PUT, PATCH

## /automation/fields

Methods: GET

## /automation/tags

Methods: GET

## /automation/triggers/

Methods: GET, POST

## /automation/triggers/{id}/

Methods: GET, PUT, PATCH, DELETE

## /automation/triggers/{id}/test/

Methods: POST

## /batch/

Methods: POST

## /billing/settlements/

Methods: GET

## /billing/subscriptions/active_summary/

Methods: GET

## /can_logging/channels/

Methods: GET, POST

## /can_logging/channels/meta/

Methods: GET

## /can_logging/channels/{id}/

Methods: GET, PUT, PATCH, DELETE

## /can_logging/channels/{id}/reset/

Methods: POST

## /can_logging/dbc/collections/

Methods: GET

## /can_logging/decoders/

Methods: GET, POST

## /can_logging/decoders/message_definitions/

Methods: GET

## /can_logging/decoders/meta/

Methods: GET

## /can_logging/decoders/{id}/

Methods: GET, PUT, PATCH, DELETE

## /can_logging/decoders/{uuid}/message_definition_library/

Methods: GET

## /can_logging/event_reactors/

Methods: GET, POST

## /can_logging/event_reactors/event_tags/

Methods: GET

## /can_logging/event_reactors/meta/

Methods: GET

## /can_logging/event_reactors/{id}/

Methods: GET, PUT, PATCH, DELETE

## /can_logging/frame_listeners/

Methods: GET, POST

## /can_logging/frame_listeners/meta/

Methods: GET

## /can_logging/frame_listeners/{id}/

Methods: GET, PUT, PATCH, DELETE

## /can_logging/import/dbc/

Methods: POST

## /can_logging/loggers/

Methods: GET, POST

## /can_logging/loggers/meta/

Methods: GET

## /can_logging/loggers/{id}/

Methods: GET, PUT, PATCH, DELETE

## /can_logging/output_handlers/

Methods: GET, POST

## /can_logging/output_handlers/meta/

Methods: GET

## /can_logging/output_handlers/{id}/

Methods: GET, PUT, PATCH, DELETE

## /can_logging/pgns/

Methods: GET

## /can_logging/pgns/{id}/

Methods: GET

## /can_logging/pids/

Methods: GET

## /can_logging/pids/{id}/

Methods: GET

## /can_logging/queries/

Methods: GET, POST

## /can_logging/queries/meta/

Methods: GET

## /can_logging/queries/{id}/

Methods: GET, PUT, PATCH, DELETE

## /can_logging/query_collections/

Methods: GET, POST

## /can_logging/workflow_hooks/

Methods: GET, POST

## /can_logging/workflow_hooks/create-default/

Methods: POST

## /can_logging/workflow_hooks/meta/

Methods: GET

## /can_logging/workflow_hooks/{id}/

Methods: GET, PUT, PATCH, DELETE

## /dashboard/customer_layout/

Methods: GET, POST

## /dashboard/customer_layout/fetch_related/

Methods: GET

## /dashboard/customer_layout/{id}/

Methods: GET, PUT, PATCH, DELETE

## /dashboard/customer_layout/{id}/copy_to_user/

Methods: POST

## /dashboard/customer_layout/{id}/duplicate/

Methods: POST

## /dashboard/layout/

Methods: GET, POST

## /dashboard/layout/{id}/

Methods: GET, PUT, PATCH, DELETE

## /dashboard/layout/{id}/duplicate/

Methods: POST

## /dashboard/map_overlays/

Methods: GET

## /dashboard/map_overlays/{id}/

Methods: GET

## /dashboard/map_overlays/{id}/download/{field_name}/

Methods: GET

## /docker/projects/

Methods: GET, POST

## /docker/projects/{id}/

Methods: GET, PUT, PATCH, DELETE

## /docker/projects/{project_pk}/releases/

Methods: GET, POST

## /docker/projects/{project_pk}/releases/active/

Methods: GET

## /docker/projects/{project_pk}/releases/{id}/

Methods: GET, PUT, PATCH

## /docker/projects/{project_pk}/releases/{release_pk}/deployments/

Methods: GET

## /docker/registries/

Methods: GET, POST

## /docker/registries/{id}/

Methods: GET, PUT, PATCH, DELETE

## /dongle/alerts/

Methods: GET

## /dongle/alerts/choices/

Methods: GET

## /dongle/alerts/clear/

Methods: POST

## /dongle/alerts/dismiss/

Methods: POST

## /dongle/alerts/{id}/

Methods: DELETE

## /dongle/alerts/{id}/dismiss/

Methods: POST

## /dongle/devices/

Methods: GET

## /dongle/devices/batch_cancel_scheduled_update/

Methods: POST

## /dongle/devices/batch_schedule_update/

Methods: POST

## /dongle/devices/by_eth_address/{eth_address}/

Methods: GET

## /dongle/devices/by_unit_id/{unit_id}/

Methods: GET

## /dongle/devices/devices_lean/

Methods: GET

## /dongle/devices/devices_lean_paged/

Methods: GET

## /dongle/devices/hw_board_versions/

Methods: GET

## /dongle/devices/lookup/

Methods: POST

## /dongle/devices/move_devices/

Methods: POST

## /dongle/devices/release_versions/

Methods: GET

## /dongle/devices/{device_pk}/accesstokens/

Methods: GET, POST

## /dongle/devices/{device_pk}/accesstokens/{id}/

Methods: GET

## /dongle/devices/{device_pk}/accesstokens/{id}/decrypt/

Methods: POST

## /dongle/devices/{device_pk}/alerts/

Methods: GET

## /dongle/devices/{device_pk}/alerts/choices/

Methods: GET

## /dongle/devices/{device_pk}/alerts/dismiss/

Methods: POST

## /dongle/devices/{device_pk}/alerts/resolve/

Methods: POST

## /dongle/devices/{device_pk}/alerts/summary/

Methods: GET

## /dongle/devices/{device_pk}/alerts/{id}/dismiss/

Methods: POST

## /dongle/devices/{device_pk}/alerts/{id}/resolve/

Methods: POST

## /dongle/devices/{device_pk}/can_logging/channels/

Methods: GET

## /dongle/devices/{device_pk}/environment_variables/

Methods: GET, POST

## /dongle/devices/{device_pk}/environment_variables/merged/

Methods: GET

## /dongle/devices/{device_pk}/environment_variables/{id}/

Methods: GET, PUT, PATCH, DELETE

## /dongle/devices/{device_pk}/environment_variables/{id}/override/

Methods: POST

## /dongle/devices/{device_pk}/pending_syncs/

Methods: GET

## /dongle/devices/{device_pk}/pending_syncs/{id}/

Methods: DELETE

## /dongle/devices/{id}/

Methods: GET, PUT, PATCH

## /dongle/devices/{id}/accept_key/

Methods: POST

## /dongle/devices/{id}/callback/{jid}/

Methods: GET

## /dongle/devices/{id}/cancel_scheduled_update/

Methods: POST

## /dongle/devices/{id}/command_result/{jid}/

Methods: GET

## /dongle/devices/{id}/data_usage/

Methods: GET

## /dongle/devices/{id}/delete_denied_key/

Methods: POST

## /dongle/devices/{id}/execute/

Methods: POST

## /dongle/devices/{id}/execute_raw/

Methods: POST

## /dongle/devices/{id}/explicit_permissions/

Methods: GET

## /dongle/devices/{id}/factory_reset/

Methods: POST

## /dongle/devices/{id}/regenerate_token/

Methods: POST

## /dongle/devices/{id}/schedule_update/

Methods: POST

## /dongle/devices/{id}/wake/

Methods: POST

## /dongle/engines/

Methods: GET, POST

## /dongle/engines/by_name/{name}/

Methods: GET, PUT, PATCH

## /dongle/engines/meta/

Methods: GET

## /dongle/engines/{id}/

Methods: GET, PUT, PATCH, DELETE

## /dongle/engines/{id}/render_settings_preview/

Methods: GET

## /dongle/environment_variables/

Methods: GET, POST

## /dongle/environment_variables/{id}/

Methods: GET, PUT, PATCH, DELETE

## /dongle/export/export_csv/

Methods: GET

## /dongle/geofences/

Methods: GET, POST

## /dongle/geofences/get_all_geofences/

Methods: GET

## /dongle/geofences/templated/

Methods: GET

## /dongle/geofences/{id}/

Methods: GET, PUT, PATCH, DELETE

## /dongle/hooks/

Methods: GET, POST

## /dongle/hooks/{id}/

Methods: GET, PUT, PATCH, DELETE

## /dongle/jobs/

Methods: GET, POST

## /dongle/jobs/{id}/

Methods: GET, PUT, PATCH, DELETE

## /dongle/mini/geofences/

Methods: GET, POST

## /dongle/mini/geofences/{id}/

Methods: GET, PUT, PATCH, DELETE

## /dongle/modules/

Methods: GET, POST

## /dongle/modules/{id}/

Methods: GET, PUT, PATCH, DELETE

## /dongle/pending_syncs/

Methods: GET

## /dongle/pending_syncs/{id}/

Methods: DELETE

## /dongle/reactors/

Methods: GET, POST

## /dongle/reactors/{id}/

Methods: GET, PUT, PATCH, DELETE

## /dongle/settings/

Methods: GET, POST

## /dongle/settings/schema/

Methods: GET

## /dongle/state_runs/

Methods: GET

## /dongle/sync_results/

Methods: GET

## /dongle/tags/

Methods: GET

## /dongle/templates/

Methods: GET, POST

## /dongle/templates/{id}/

Methods: GET, PUT, PATCH, DELETE

## /dongle/templates/{id}/apply/

Methods: POST

## /dongle/templates/{id}/apply_async/

Methods: POST

## /dongle/templates/{id}/apply_explicit/

Methods: POST

## /dongle/templates/{id}/apply_explicit_async/

Methods: POST

## /dongle/templates/{id}/duplicate/

Methods: POST

## /dongle/templates/{id}/unassociate_devices/

Methods: POST

## /dongle/templates/{template_pk}/can_logging/channels/

Methods: GET

## /dongle/templates/{template_pk}/devices/

Methods: GET

## /dongle/update_logs/

Methods: GET

## /dongle/update_logs/{id}/

Methods: GET

## /dongle/workers/

Methods: GET, POST

## /dongle/workers/{id}/

Methods: GET, PUT, PATCH, DELETE

## /dongle/{unit_id}/device/refresh_pillar/

Methods: POST

## /dongle/{unit_id}/execute/

Methods: POST

## /dongle/{unit_id}/execute_raw/

Methods: POST

## /dongle/{unit_id}/obd/bus/{bus_id}/can/db/

Methods: GET

## /dongle/{unit_id}/obd/commands/

Methods: GET

## /dongle/{unit_id}/obd/dtc/

Methods: GET

## /dongle/{unit_id}/obd/dtc/clear/

Methods: POST

## /dongle/{unit_id}/obd/query/{command}/

Methods: POST

## /dongle/{unit_id}/retrieve_job/{jid}/

Methods: GET

## /dongle/{unit_id}/salt/engines/

Methods: GET

## /dongle/{unit_id}/salt/geofence/

Methods: GET

## /dongle/{unit_id}/salt/schedule/

Methods: GET

## /fleet/alerts/

Methods: GET

## /fleet/alerts/choices/

Methods: GET

## /fleet/alerts/dismiss/

Methods: POST

## /fleet/alerts/resolve/

Methods: POST

## /fleet/alerts/summary/

Methods: GET

## /fleet/alerts/{id}/dismiss/

Methods: POST

## /fleet/alerts/{id}/resolve/

Methods: POST

## /fleet/geofences/

Methods: GET, POST

## /fleet/geofences/{fleetgeofence_pk}/vehicle-groups/

Methods: GET

## /fleet/geofences/{fleetgeofence_pk}/vehicle-groups/modify/

Methods: POST

## /fleet/geofences/{fleetgeofence_pk}/vehicles/

Methods: GET

## /fleet/geofences/{fleetgeofence_pk}/vehicles/modify/

Methods: POST

## /fleet/geofences/{id}/

Methods: GET, PUT, PATCH, DELETE

## /fleet/locations/

Methods: GET, POST

## /fleet/locations/{id}/

Methods: GET, PUT, PATCH, DELETE

## /fleet/notification_channels/

Methods: GET, POST

## /fleet/notification_channels/{id}/

Methods: PUT, PATCH, DELETE

## /fleet/notification_channels/{id}/test_notification_channel/

Methods: GET

## /fleet/notification_types/

Methods: GET

## /fleet/templates/

Methods: GET, POST

## /fleet/templates/{id}/

Methods: GET, PUT, PATCH, DELETE

## /fleet/templates/{id}/apply/

Methods: POST

## /fleet/templates/{id}/apply_async/

Methods: POST

## /fleet/templates/{id}/apply_explicit/

Methods: POST

## /fleet/templates/{id}/apply_explicit_async/

Methods: POST

## /fleet/templates/{id}/duplicate/

Methods: POST

## /fleet/templates/{id}/unassociate_devices/

Methods: POST

## /fleet/vehicle-groups-list/

Methods: GET

## /fleet/vehicle_fleet_states/

Methods: GET, POST

## /fleet/vehicle_fleet_states/{id}/

Methods: GET, PUT, PATCH, DELETE

## /fleet/vehicle_states/

Methods: GET, POST

## /fleet/vehicle_states/{id}/

Methods: GET, PUT, PATCH, DELETE

## /fleet/vehicles-list/

Methods: GET

## /fleet/vehicles/

Methods: GET, POST

## /fleet/vehicles/archived/

Methods: GET

## /fleet/vehicles/assign_users/

Methods: POST

## /fleet/vehicles/create_default_fleet_states/

Methods: POST

## /fleet/vehicles/create_default_vehicle_states/

Methods: POST

## /fleet/vehicles/fleet_states/

Methods: GET

## /fleet/vehicles/import_batch_edit/

Methods: POST

## /fleet/vehicles/import_csv/

Methods: POST

## /fleet/vehicles/states/

Methods: GET

## /fleet/vehicles/{id}/

Methods: GET, PUT, PATCH, DELETE

## /fleet/vehicles/{id}/fleet_states/

Methods: GET

## /fleet/vehicles/{id}/rewards/

Methods: GET

## /fleet/vehicles/{id}/states/

Methods: GET

## /fleet/vehicles/{vehicle_pk}/alert_summary/

Methods: GET

## /fleet/vehicles/{vehicle_pk}/alerts/

Methods: GET

## /fleet/vehicles/{vehicle_pk}/alerts/choices/

Methods: GET

## /fleet/vehicles/{vehicle_pk}/alerts/dismiss/

Methods: POST

## /fleet/vehicles/{vehicle_pk}/alerts/resolve/

Methods: POST

## /fleet/vehicles/{vehicle_pk}/alerts/summary/

Methods: GET

## /fleet/vehicles/{vehicle_pk}/alerts/{id}/dismiss/

Methods: POST

## /fleet/vehicles/{vehicle_pk}/alerts/{id}/resolve/

Methods: POST

## /fleet/vehicles/{vehicle_pk}/data_request/

Methods: POST

## /fleet/vehicles/{vehicle_pk}/faultoccurrances/

Methods: GET

## /fleet/vehicles/{vehicle_pk}/faultoccurrances/{id}/

Methods: GET, DELETE

## /fleet/vehicles/{vehicle_pk}/faultoccurrances/{id}/clear/

Methods: POST

## /fleet/vehicles/{vehicle_pk}/geofence_summary/

Methods: GET

## /hub/trips/

Methods: POST

## /hub/trips/close_trip/

Methods: POST

## /hub/trips/{id}/

Methods: DELETE

## /logbook/charging_sessions/

Methods: GET

## /logbook/diagnostics/

Methods: GET

## /logbook/events/

Methods: GET

## /logbook/events_histogram/

Methods: GET

## /logbook/fleet_summary/alerts/

Methods: GET

## /logbook/fleet_summary/devices/

Methods: GET

## /logbook/fleet_summary/diagnostics/

Methods: GET

## /logbook/fleet_summary/geofences/

Methods: GET

## /logbook/fleet_summary/timedistance/

Methods: GET

## /logbook/fleet_summary/vehicles/

Methods: GET

## /logbook/most_recent_vehicle_positions/

Methods: GET

## /logbook/raw/

Methods: GET

## /logbook/recent_stats/

Methods: GET

## /logbook/requeue_events/

Methods: POST

## /logbook/rfid_status/

Methods: GET

## /logbook/simplified_events/

Methods: GET

## /logbook/storage/data_fields/

Methods: GET

## /logbook/storage/fields/

Methods: GET

## /logbook/storage/raw/

Methods: GET

## /logbook/storage/read/

Methods: GET

## /logbook/storage/v2/raw/

Methods: GET

## /logbook/trips/

Methods: GET

## /logbook/trips/{id}/

Methods: GET, PUT, PATCH

## /logbook/v2/most_recent_position/

Methods: GET

## /logbook/v2/most_recent_positions/

Methods: GET

## /logbook/v2/recent_stats/

Methods: GET

## /logbook/v2/trips/

Methods: GET

## /logbook/v2/trips/{id}/

Methods: GET, PUT, PATCH

## /logbook/v2/trips/{id}/edit_trip_times/

Methods: PATCH

## /obd/canmessages/

Methods: GET, POST

## /obd/canmessages/{canmessage_pk}/signals/

Methods: GET

## /obd/canmessages/{canmessage_pk}/signals/{id}/

Methods: DELETE

## /obd/canmessages/{id}/

Methods: GET, PUT, PATCH, DELETE

## /obd/canmessages/{id}/associate_to_busses/

Methods: POST

## /obd/canmessages/{id}/associate_to_vehicle/

Methods: POST

## /obd/canmessages/{id}/buses/

Methods: GET

## /obd/canmessages/{id}/duplicate/

Methods: POST

## /obd/canmessages/{id}/pull_pending_changes/

Methods: POST

## /obd/canmessages/{id}/remove_parent_relationship/

Methods: POST

## /obd/canmessagestemplate/

Methods: GET, POST

## /obd/canmessagestemplate/{id}/

Methods: GET, PUT, PATCH, DELETE

## /obd/canmessagestemplate/{id}/associate_to_busses/

Methods: POST

## /obd/canmessagestemplate/{id}/associate_to_vehicle/

Methods: POST

## /obd/canmessagestemplate/{id}/duplicate/

Methods: POST

## /obd/canmessagestemplate/{id}/pull_pending_changes/

Methods: POST

## /obd/canmessagestemplate/{id}/remove_parent_relationship/

Methods: POST

## /obd/community/search/

Methods: GET

## /obd/diagnostics/

Methods: GET

## /obd/faultdefinitions/

Methods: GET, POST

## /obd/faultdefinitions/{id}/

Methods: GET, PUT, PATCH, DELETE

## /obd/faultoccurrances/

Methods: GET

## /obd/faultoccurrances/{id}/

Methods: GET, DELETE

## /obd/faultoccurrances/{id}/clear/

Methods: POST

## /obd/library/import/can/

Methods: POST

## /obd/library/search/

Methods: GET

## /obd/loggers/

Methods: GET

## /obd/loggers/can/

Methods: GET, POST

## /obd/loggers/can/{id}/

Methods: GET, PUT, DELETE

## /obd/loggers/mini/

Methods: GET, POST

## /obd/loggers/mini/{id}/

Methods: GET, PUT, DELETE

## /obd/loggers/pid/

Methods: GET, POST

## /obd/loggers/pid/{id}/

Methods: GET, PUT, DELETE

## /obd/loggers/restore/

Methods: POST

## /obd/mini/loggers/

Methods: GET, POST

## /obd/mini/loggers/{id}/

Methods: GET, PUT, DELETE

## /obd/mini/parameters/

Methods: GET

## /obd/mini/parameters/{id}/

Methods: GET

## /obd/pgns/

Methods: GET, POST

## /obd/pgns/meta/

Methods: GET

## /obd/pgns/{id}/

Methods: GET, PUT, PATCH, DELETE

## /obd/pids/

Methods: GET, POST

## /obd/pids/{id}/

Methods: GET, PUT, PATCH, DELETE

## /obd/pids/{id}/associate_to_busses/

Methods: POST

## /obd/pids/{id}/associate_to_vehicle/

Methods: POST

## /obd/pids/{id}/buses/

Methods: GET

## /obd/pids/{id}/duplicate/

Methods: POST

## /obd/pids/{id}/pull_pending_changes/

Methods: POST

## /obd/pids/{id}/remove_parent_relationship/

Methods: POST

## /obd/pidstemplate/

Methods: GET, POST

## /obd/pidstemplate/{id}/

Methods: GET, PUT, PATCH, DELETE

## /obd/pidstemplate/{id}/associate_to_busses/

Methods: POST

## /obd/pidstemplate/{id}/associate_to_vehicle/

Methods: POST

## /obd/pidstemplate/{id}/duplicate/

Methods: POST

## /obd/pidstemplate/{id}/pull_pending_changes/

Methods: POST

## /obd/pidstemplate/{id}/remove_parent_relationship/

Methods: POST

## /obd/spns/

Methods: GET, POST

## /obd/spns/{id}/

Methods: GET, PUT, PATCH, DELETE

## /obd/supportedcanmessages/

Methods: GET

## /obd/v2/library/import/can/

Methods: POST

## /obd/v2/library/import/pid/

Methods: POST

## /reporting/reports/

Methods: GET, POST

## /reporting/reports/available_geofences/

Methods: GET

## /reporting/reports/unique_vehicles_count/

Methods: GET

## /reporting/reports/user_emails/

Methods: GET

## /reporting/reports/{id}/

Methods: GET, DELETE

## /reporting/reports/{id}/data/

Methods: GET

## /reporting/reports/{id}/download/

Methods: GET

## /reporting/reports/{id}/render/

Methods: GET

## /reporting/schedules/

Methods: GET, POST

## /reporting/schedules/preview/

Methods: POST

## /reporting/schedules/{id}/

Methods: GET, PUT, PATCH, DELETE

## /tasks/

Methods: GET, POST

## /tasks/enqueue_export/

Methods: POST

## /tasks/in_progress/

Methods: GET

## /tasks/{id}/

Methods: GET, DELETE

## /tasks/{id}/clear_result/

Methods: POST

## /tasks/{id}/progress/

Methods: GET

## /tasks/{id}/result_trip_export/

Methods: GET

## /vehicle/busses/

Methods: GET, POST

## /vehicle/busses/{id}/

Methods: GET, PUT, PATCH, DELETE

## /vehicle/group/

Methods: GET, POST

## /vehicle/group/vehicles/

Methods: GET

## /vehicle/group/{id}/

Methods: GET, PUT, PATCH, DELETE

## /vehicle/group/{id}/vehicles/

Methods: GET

## /vehicle/makes/

Methods: GET

## /vehicle/models/

Methods: GET

## /vehicle/models/{make_id}/

Methods: GET

## /vehicle/profile/

Methods: GET, POST

## /vehicle/profile/{id}/

Methods: GET, PUT, PATCH, DELETE

## /vehicle/profile/{profile_pk}/recharge_sessions/

Methods: GET

## /vehicle/profile/{profile_pk}/recharge_sessions/{id}/

Methods: GET

## /vehicle/v2/profile/

Methods: GET, POST

## /vehicle/v2/profile/{id}/

Methods: GET, PUT, PATCH, DELETE

