from django.apps import AppConfig
from openedx.core.djangoapps.plugins.constants import (
    PluginSettings,
    PluginURLs,
    ProjectType,
    SettingsType,
)


class RedfidLogoutConfig(AppConfig):
    name = 'redfid_logout'
    plugin_app = {
        PluginURLs.CONFIG: {
            ProjectType.LMS: {
                PluginURLs.NAMESPACE: "redfid_logout",
                PluginURLs.REGEX: r"^redfid_logout/",
                PluginURLs.RELATIVE_PATH: "urls",
            }},
        PluginSettings.CONFIG: {
            ProjectType.CMS: {
                SettingsType.COMMON: {
                    PluginSettings.RELATIVE_PATH: "settings.common"}},
            ProjectType.LMS: {
                SettingsType.COMMON: {
                    PluginSettings.RELATIVE_PATH: "settings.common"}},
        },
    }
