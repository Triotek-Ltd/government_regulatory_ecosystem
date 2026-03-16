"""Action handler seed for license_record:renew."""

from __future__ import annotations


DOC_ID = "license_record"
ACTION_ID = "renew"
ACTION_RULE = {'allowed_in_states': ['active', 'suspended', 'expired'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['registration_application', 'license_renewal_case', 'filing_requirement'], 'borrowed_fields': ['authority/program context from filing_requirement where linked'], 'inferred_roles': ['case owner']}, 'actors': ['case owner'], 'action_actors': {'create': ['case owner'], 'update': ['case owner'], 'archive': ['case owner']}}

def handle_renew(payload: dict, context: dict | None = None) -> dict:
    context = context or {}
    next_state = ACTION_RULE.get("transitions_to")
    updates = {STATE_FIELD: next_state} if STATE_FIELD and next_state else {}
    return {
        "doc_id": DOC_ID,
        "action_id": ACTION_ID,
        "payload": payload,
        "context": context,
        "allowed_in_states": ACTION_RULE.get("allowed_in_states", []),
        "next_state": next_state,
        "updates": updates,
        "workflow_objective": WORKFLOW_HINTS.get("business_objective"),
    }
