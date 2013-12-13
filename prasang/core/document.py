from prasang.utils.text_processor import TextProcessor


class Document:
    def __init__(self, id=0,text="",text_processor=TextProcessor()):
        self.id = id
        self.text_processor = text_processor
        self.text = text_processor.remove_non_ascii(text)

    def __eq__(self, other):
        return (isinstance(other, self.__class__)
                and self.text == other.text and self.id == other.id)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.id) ^ hash(self.text)