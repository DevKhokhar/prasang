from collections import defaultdict
from gensim.models import LdaModel
import operator


class LDASpace():
    def __init__(self, tokenised_documents):
        self.token_frequency_map = self.token_frequency(tokenised_documents)
        self.id_2_word, self.token_2_id = self.compute_id_word_mappings()

    def token_frequency(self, tokenised_documents):
        word_freq = defaultdict(int)
        for token_list in tokenised_documents:
            map(lambda token: word_freq.update({token: word_freq[token] + 1}), token_list)
        return word_freq

    def id2Word(self):
        return self.id_2_word

    def doc2bow(self, vector):
        return [(self.token_2_id[token], self.token_frequency_map[token]) for token in vector]

    def compute_id_word_mappings(self):
        sorted_tokens = sorted(self.token_frequency_map.iteritems(), key=operator.itemgetter(0))
        token_2_id_map = defaultdict(int, [(token, i) for i, (token, freq) in enumerate(sorted_tokens)])
        id_2_token_map = defaultdict(int, [(i, token) for i, (token, freq) in enumerate(sorted_tokens)])
        return id_2_token_map, token_2_id_map

class LDATransformation():
    def __init__(self, input_space_vectors_map):
        self.input_space_vectors = input_space_vectors_map.values()
        self.transform()

    def transform(self):
        self.space = LDASpace(self.input_space_vectors)
        self.reduced_space = 15

        input_BOWs = [self.space.doc2bow(vector) for vector in self.input_space_vectors]
        self.lda_model = LdaModel(corpus=input_BOWs, id2word=self.space.id2Word(), num_topics=self.reduced_space, passes=100)
        return self.lda_model