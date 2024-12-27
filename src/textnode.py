from enum import Enum

TextType = Enum("TextType", ["Normal", "Bold", "Italic", "Code", "Links", "Images"])

class TextNode():
    def __init__(self, text: str, text_type: TextType, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other_textnode):
        if self.text == other_textnode.text and self.text_type == other_textnode.text_type and self.url == other_textnode.url:
            return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.name}, {self.url})"