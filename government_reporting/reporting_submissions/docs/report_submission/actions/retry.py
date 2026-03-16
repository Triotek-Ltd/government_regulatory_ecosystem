"""Action handler seed for report_submission:retry."""

from __future__ import annotations


DOC_ID = "report_submission"
ACTION_ID = "retry"
ACTION_RULE = {'allowed_in_states': ['draft', 'submitted', 'accepted', 'rejected', 'completed'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['government_report', 'report_acknowledgement', 'regulatory_review_case'], 'borrowed_fields': ['report scope', 'authority from government_report'], 'inferred_roles': ['compliance officer', 'case owner']}, 'actors': ['compliance officer', 'case owner'], 'action_actors': {'create': ['compliance officer'], 'submit': ['compliance officer'], 'reject': ['compliance officer'], 'archive': ['case owner']}}

def handle_retry(payload: dict, context: dict | None = None) -> dict:
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
