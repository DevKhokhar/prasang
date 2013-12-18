from pattern.vector import Document

class DocumentModel(Document):

    def sent_hashKey(self,sent_number):
        return "doc" + str(self.id) + "-" + "sent" + str(sent_number)

    def __eq__(self, other):
        return (isinstance(other, self.__class__)
                and set(self.terms.keys()) == set(other.terms.keys()) and self.name == other.name)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.name) ^ hash(' '.join(self.terms.keys()))