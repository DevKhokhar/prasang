from unittest import TestCase
import os.path as ospath
from prasang.core import MultiDocumentCorpus, MultiDocumentModel, DocumentModel


class TestDocument(TestCase):
    def setUp(self):
        self.test_document_path = ospath.join(ospath.dirname(__file__), "test_data/test_document_dataset")

    def test_shouldCreateDocumentGivenADirectoryPath(self):
        document_text1 = """This is content of the file1\nWith line separated. blabla !!!"""
        document_text2 = """This is content of the file.\nWith line separated. blabla"""

        document1 = DocumentModel(string=document_text1, name="1.txt")
        document2 = DocumentModel(string=document_text2, name="2.txt")

        expected_multi_document = MultiDocumentModel(documents=[document1, document2])
        actual_multi_document = MultiDocumentCorpus(self.test_document_path).multi_document()

        self.assertEquals(actual_multi_document, expected_multi_document)

    def test_shouldGenerateTopicModelGivenADocumentCorpus(self):
        test_documents_path = ospath.join(ospath.dirname(__file__), "test_data/movie_review_dataset")
        documents = MultiDocumentCorpus(test_documents_path).multi_document()
        context = documents.generate_topic_model()
        for topic in context.print_topics(topics=context.num_topics):
            print topic