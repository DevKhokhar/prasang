import os
from prasang.core import Document
from prasang.utils import FileReader


class MultiDocument:
    def __init__(self, documents=None):
        if not documents: documents = list()
        if not isinstance(documents[0], Document): raise RuntimeError(
            "Illegal MultiDocument, A Multi Document is a collection of Documents")
        self.documents = documents

    def __eq__(self, other):
        return (isinstance(other, self.__class__)
                and set(self.documents) == set(other.documents))

    def __ne__(self, other):
        return not self.__eq__(other)


class MultiDocumentCorpus:
    def __init__(self, directory_path):
        self.path = directory_path

    def multi_document(self):
        documents = []
        abs_path = os.path.abspath(self.path)
        text_files = sorted(self._list_files())
        for text_file in text_files:
            filepath = os.path.join(abs_path, text_file)
            text = FileReader.read(filepath)
            documents.append(Document(id=text_file, text=text))

        return MultiDocument(documents=documents)

    def _list_files(self):
        path = os.path.abspath(self.path)
        return [listed for listed in os.listdir(path) if os.path.isfile(os.path.join(path, listed))]