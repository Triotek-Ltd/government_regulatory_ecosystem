"""Action handler seed for ecosystem_filing_record:archive."""

from __future__ import annotations


DOC_ID = "ecosystem_filing_record"
ACTION_ID = "archive"
ACTION_RULE = {'allowed_in_states': ['draft', 'prepared', 'submitted', 'accepted', 'rejected'], 'transitions_to': 'archived'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['filing_requirement', 'regulatory_review_case', 'regulatory_filing'], 'borrowed_fields': ['authority', 'due rule', 'obligation context from filing_requirement'], 'inferred_roles': ['compliance officer', 'case owner']}, 'actors': ['compliance officer', 'case owner'], 'action_actors': {'create': ['compliance officer'], 'submit': ['compliance officer'], 'close': ['case owner'], 'archive': ['case owner']}}

def handle_archive(payload: dict, context: dict | None = None) -> dict:
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
