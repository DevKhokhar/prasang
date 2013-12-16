from collections import defaultdict
from pattern.vector import Document
from prasang.utils import TextProcessor

class DocumentModel(Document):

    def tokenised_sentences_dict(self):
        sentences = defaultdict(list)
        sentence_list = TextProcessor().nltk_sentences(' '.join(self.terms.keys()))
        for id, sentence in enumerate(sentence_list):
            stopped_sentence = TextProcessor().stopped_tokenize(sentence)
            if stopped_sentence:
                sentences[self.sent_hashKey(id)] = stopped_sentence
        return sentences

    def sent_hashKey(self,sent_number):
        return "doc" + str(self.id) + "-" + "sent" + str(sent_number)

    def __eq__(self, other):
        return (isinstance(other, self.__class__)
                and set(self.terms.keys()) == set(other.terms.keys()) and self.name == other.name)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.name) ^ hash(' '.join(self.terms.keys()))