"""Action handler seed for regulatory_review_case:assign."""

from __future__ import annotations


DOC_ID = "regulatory_review_case"
ACTION_ID = "assign"
ACTION_RULE = {'allowed_in_states': ['opened', 'in_review', 'remediated'], 'transitions_to': 'in_review'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['ecosystem_filing_record', 'report_submission', 'license_renewal_case'], 'borrowed_fields': ['filing/report', 'authority context from linked docs'], 'inferred_roles': ['compliance officer', 'case owner']}, 'actors': ['compliance officer', 'case owner'], 'action_actors': {'create': ['compliance officer'], 'assign': ['compliance officer'], 'review': ['case owner'], 'close': ['case owner'], 'archive': ['case owner']}}

def handle_assign(payload: dict, context: dict | None = None) -> dict:
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
