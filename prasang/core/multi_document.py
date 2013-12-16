from collections import defaultdict
import os
from prasang.core import LDATransformation, DocumentModel
from prasang.utils import FileReader
from pattern.vector import Model

class MultiDocumentModel(Model):
    def tokenised_sentences(self):
        sentences = defaultdict(list)
        for document in self.documents:
            sentences.update(document.tokenised_sentences_dict())
        return sentences

    def generate_topic_model(self):
        tokenised_sentences = self.tokenised_sentences()
        transformation = LDATransformation(tokenised_sentences)
        topic_tags = transformation.transform()
        return topic_tags

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
            doc = DocumentModel(string=text, name=text_file)
            documents.append(doc)

        return MultiDocumentModel(documents=documents)

    def _list_files(self):
        path = os.path.abspath(self.path)
        return [listed for listed in os.listdir(path) if os.path.isfile(os.path.join(path, listed))]