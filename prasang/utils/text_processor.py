class TextProcessor():
    def __init__(self):
        pass

    def remove_non_ascii(self, text):
        return "".join(filter(lambda x: ord(x)<128, text))