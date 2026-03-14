"""Doc runtime hooks for regulatory_review_case."""

class DocRuntime:
    doc_key = "regulatory_review_case"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'assign', 'review', 'remediate', 'close', 'archive']
