"""Action registry seed for registration_application."""

from __future__ import annotations


DOC_ID = "registration_application"
ALLOWED_ACTIONS = ['create', 'submit', 'update', 'approve', 'reject', 'archive']
ACTION_RULES = {'create': {'allowed_in_states': ['draft', 'submitted', 'in_review', 'approved', 'rejected'], 'transitions_to': None}, 'submit': {'allowed_in_states': ['draft', 'submitted', 'in_review', 'approved', 'rejected'], 'transitions_to': 'submitted'}, 'update': {'allowed_in_states': ['draft', 'submitted', 'in_review', 'approved', 'rejected'], 'transitions_to': None}, 'approve': {'allowed_in_states': ['draft', 'submitted', 'in_review', 'approved', 'rejected'], 'transitions_to': 'approved'}, 'reject': {'allowed_in_states': ['draft', 'submitted', 'in_review', 'approved', 'rejected'], 'transitions_to': 'rejected'}, 'archive': {'allowed_in_states': ['draft', 'submitted', 'in_review', 'approved', 'rejected'], 'transitions_to': 'archived'}}

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
