"""Doc runtime hooks for license_record."""

class DocRuntime:
    doc_key = "license_record"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'update', 'renew', 'suspend', 'archive']
