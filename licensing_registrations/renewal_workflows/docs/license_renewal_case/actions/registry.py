"""Action registry seed for license_renewal_case."""

from __future__ import annotations


DOC_ID = "license_renewal_case"
ALLOWED_ACTIONS = ['create', 'assign', 'prepare', 'submit', 'renew', 'close', 'archive']
ACTION_RULES = {'create': {'allowed_in_states': ['opened', 'preparing', 'submitted', 'renewed', 'expired'], 'transitions_to': None}, 'assign': {'allowed_in_states': ['opened', 'preparing', 'submitted', 'renewed', 'expired'], 'transitions_to': None}, 'prepare': {'allowed_in_states': ['opened', 'preparing', 'submitted', 'renewed', 'expired'], 'transitions_to': None}, 'submit': {'allowed_in_states': ['opened', 'preparing', 'submitted', 'renewed', 'expired'], 'transitions_to': 'submitted'}, 'renew': {'allowed_in_states': ['opened', 'preparing', 'submitted', 'renewed', 'expired'], 'transitions_to': 'renewed'}, 'close': {'allowed_in_states': ['opened', 'preparing', 'submitted', 'renewed', 'expired'], 'transitions_to': 'closed'}, 'archive': {'allowed_in_states': ['opened', 'preparing', 'submitted', 'renewed', 'expired'], 'transitions_to': 'archived'}}

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
