"""Doc runtime hooks for report_submission."""

class DocRuntime:
    doc_key = "report_submission"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'submit', 'retry', 'accept', 'reject', 'archive']
