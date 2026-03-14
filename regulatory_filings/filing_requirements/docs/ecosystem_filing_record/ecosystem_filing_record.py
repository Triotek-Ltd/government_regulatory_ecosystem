"""Doc runtime hooks for ecosystem_filing_record."""

class DocRuntime:
    doc_key = "ecosystem_filing_record"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'prepare', 'submit', 'amend', 'close', 'archive']
