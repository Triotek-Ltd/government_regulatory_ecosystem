"""Action handler seed for filing_requirement:archive."""

from __future__ import annotations


DOC_ID = "filing_requirement"
ACTION_ID = "archive"
ACTION_RULE = {'allowed_in_states': ['draft', 'active', 'retired'], 'transitions_to': 'archived'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['ecosystem_filing_record', 'government_report', 'license_record'], 'borrowed_fields': [], 'inferred_roles': ['compliance officer']}, 'actors': ['compliance officer'], 'action_actors': {'create': ['compliance officer'], 'update': ['compliance officer'], 'review': ['compliance officer'], 'activate': ['compliance officer'], 'retire': ['compliance officer'], 'archive': ['compliance officer']}}

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
