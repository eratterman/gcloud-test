import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


COLLECTION = 'juvi_whale'
CREDS = './.p/pytest-313001-a61375332c23.json'


class DbConnect(object):
    def __init__(self):
        cred = credentials.Certificate(CREDS)
        try:
            firebase_admin.initialize_app(cred)
            self.db = firestore.client()
        except Exception as e:
            print(f'Failed to connect to DB: {e}')
            raise

        self.docs = {}
        self.collection = COLLECTION

    def get_documents(self):
        try:
            docs_ref = self.db.collection(self.collection)
            docs = docs_ref.stream()
        except Exception as e:
            print(f'Failed to get docs from collection: {self.collection}: {e}')
            return self.docs

        self.docs = {d.id: d.to_dict().get('value', 0) for d in docs}
        return self.docs

    def add_document(self, name, value):
        # pull current docs and check for name and value
        self.get_documents()
        doc_val = self.docs.get(name, None)

        try:
            doc_ref = self.db.collection(self.collection).document(name)
        except Exception as e:
            print(f'Failed to get document {name}: {e}')
            return None

        if doc_val is None:
            # if current doc does not exist, add new doc
            doc_ref.set({'value': value})
        else:
            # if doc already exists, increment value
            doc_ref.set({'value': doc_val + value})

        return self.get_documents()

    def __repr__(self):
        return f'<Firestore DB Connection: {self.collection}>'


if __name__ == '__main__':
    pass
    # # print(add_name('hello', 4))
    # db = DbConnect()
    # db.add_document('foo_bar', 4)
