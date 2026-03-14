"""Action registry seed for report_acknowledgement."""

from __future__ import annotations


DOC_ID = "report_acknowledgement"
ALLOWED_ACTIONS = ['record', 'link', 'archive']
ACTION_RULES = {'record': {'allowed_in_states': ['received', 'linked'], 'transitions_to': None}, 'link': {'allowed_in_states': ['received', 'linked'], 'transitions_to': None}, 'archive': {'allowed_in_states': ['received', 'linked'], 'transitions_to': 'archived'}}

STATE_FIELD = 'workflow_state'

def get_action_handler_name(action_id: str) -> str:
    return f"handle_{action_id}"

def get_action_module_path(action_id: str) -> str:
    return f"actions/{action_id}.py"

def action_contract(action_id: str) -> dict:
    return {
        "state_field": STATE_FIELD,
        "rule": ACTION_RULES.get(action_id, {}),
    }
