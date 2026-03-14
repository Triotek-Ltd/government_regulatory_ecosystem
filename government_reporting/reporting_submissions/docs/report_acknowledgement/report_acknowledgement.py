"""Doc runtime hooks for report_acknowledgement."""

class DocRuntime:
    doc_key = "report_acknowledgement"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['record', 'link', 'archive']
