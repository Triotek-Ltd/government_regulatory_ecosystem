"""Integration-service seed for registration_application."""

from __future__ import annotations


DOC_ID = "registration_application"
INTEGRATION_RULES = {'external_refs': [{'field_id': 'external_reference', 'kind': 'external', 'label': 'External Reference'}], 'sync_rules': []}

class IntegrationService:
    def sync_rules(self) -> list:
        return INTEGRATION_RULES.get("sync_rules", [])

    def integration_profile(self) -> dict:
        return {'external_sync_enabled': True, 'tracks_external_refs': True}
