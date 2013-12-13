from unittest import TestCase
import os.path as ospath
from prasang.core import Document, MultiDocumentCorpus, MultiDocument


class TestDocument(TestCase):
    def setUp(self):
        self.test_document_path = ospath.join(ospath.dirname(__file__), "test_data/test_document_dataset")

    def test_shouldCreateDocumentGivenADirectoryPath(self):
        document_text1 = """This is content of the file1\nWith line separated. blabla !!!"""
        document_text2 = """This is content of the file.\nWith line separated. blabla"""

        document1 = Document(id="1.txt", text=document_text1)
        document2 = Document(id="2.txt", text=document_text2)

        expected_multi_document = MultiDocument(documents=[document1, document2])
        actual_multi_document = MultiDocumentCorpus(self.test_document_path).multi_document()

        self.assertEquals(actual_multi_document, expected_multi_document)
