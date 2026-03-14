"""Doc runtime hooks for government_report."""

class DocRuntime:
    doc_key = "government_report"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'approve', 'prepare_for_submission', 'archive']
