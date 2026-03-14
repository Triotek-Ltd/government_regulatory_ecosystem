"""Doc runtime hooks for registration_application."""

class DocRuntime:
    doc_key = "registration_application"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'submit', 'update', 'approve', 'reject', 'archive']
