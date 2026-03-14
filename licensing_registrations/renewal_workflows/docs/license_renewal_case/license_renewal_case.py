"""Doc runtime hooks for license_renewal_case."""

class DocRuntime:
    doc_key = "license_renewal_case"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'assign', 'prepare', 'submit', 'renew', 'close', 'archive']
