import os
from azure.appconfiguration import AzureAppConfigurationClient, ConfigurationSetting

# try:
print("Azure App Configuration - Python Quickstart")
# Quickstart code goes here

connection_string = os.getenv('AZURE_APP_CONFIG_CONNECTION_STRING')
print(connection_string)
app_config_client = AzureAppConfigurationClient.from_connection_string(
    connection_string)

filtered_settings_list = app_config_client.list_configuration_settings()
print("\nRetrieved list of configuration settings:")
for item in filtered_settings_list:
    print("Key: " + item.key + ", Value: " + item.value)


retrieved_config_setting = app_config_client.get_configuration_setting(
    key='Test:Settings:Message')
print("\nRetrieved configuration setting:")
print("Key: " + retrieved_config_setting.key +
      ", Value: " + retrieved_config_setting.value)

retrieved_config_setting = app_config_client.get_configuration_setting(
    key='db_connection_string')
print("\nRetrieved configuration setting:")
print("Key: " + retrieved_config_setting.key +
      ", Value: " + retrieved_config_setting.value)


"""
config_setting = ConfigurationSetting(
        key='TestApp:Settings:NewSetting',
        value='New setting value'
    )
    added_config_setting = app_config_client.add_configuration_setting(
        config_setting)
    print("\nAdded configuration setting:")
    print("Key: " + added_config_setting.key +
          ", Value: " + added_config_setting.value)

    filtered_settings_list = app_config_client.list_configuration_settings(
        key_filter="TestApp*")
    print("\nRetrieved list of configuration settings:")
    for item in filtered_settings_list:
        print("Key: " + item.key + ", Value: " + item.value)

    locked_config_setting = app_config_client.set_read_only(
        added_config_setting, read_only=True)
    print("\nRead-only status for " + locked_config_setting.key +
          ": " + str(locked_config_setting.read_only))

    unlocked_config_setting = app_config_client.set_read_only(
        locked_config_setting, read_only=False)
    print("\nRead-only status for " + unlocked_config_setting.key +
          ": " + str(unlocked_config_setting.read_only))

    added_config_setting.value = "Value has been updated!"
    updated_config_setting = app_config_client.set_configuration_setting(
        added_config_setting)
    print("\nUpdated configuration setting:")
    print("Key: " + updated_config_setting.key +
          ", Value: " + updated_config_setting.value)

    deleted_config_setting = app_config_client.delete_configuration_setting(
        key="TestApp:Settings:NewSetting")
    print("\nDeleted configuration setting:")
    print("Key: " + deleted_config_setting.key +
          ", Value: " + deleted_config_setting.value)
"""
# except Exception as ex:
#    print('Exception:')
#    print(ex)
