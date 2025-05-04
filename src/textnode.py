from enum import Enum
from htmlnode import HTMLNode
from leafnode import LeafNode

class TextType(Enum):
	NORMAL = "normal text"
	BOLD = "bold text"
	ITALIC = "italic"
	CODE = "code"
	LINK = "link"
	IMAGE = "image"

class TextNode():
	def __init__(self, text, text_type: TextType, url = None):
		self.text = text
		self.text_type = text_type
		self.url = url

	def __eq__(self, node2):
		return self.text == node2.text and self.text_type == node2.text_type and self.url == node2.url

	def __repr__(self):
		return f"TextNode({self.text},{self.text_type.value},{self.url})"

def text_node_to_html_node(text_node: TextNode) -> HTMLNode:
    type = text_node.text_type
    html_node = HTMLNode()
    match type:
        case TextType.NORMAL:
            html_node = LeafNode(None,text_node.text)
        case TextType.BOLD:
            html_node = LeafNode("b",text_node.text)
        case TextType.ITALIC:
            html_node = LeafNode("i",text_node.text)
        case TextType.CODE:
            html_node = LeafNode("code",text_node.text)
        case TextType.LINK:
            html_node = LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            html_node = LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("text type not valid")

    return html_node
