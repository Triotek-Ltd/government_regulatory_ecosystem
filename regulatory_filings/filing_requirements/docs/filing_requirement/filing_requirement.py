"""Doc runtime hooks for filing_requirement."""

class DocRuntime:
    doc_key = "filing_requirement"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'update', 'review', 'activate', 'retire', 'archive']
