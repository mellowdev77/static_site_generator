from htmlnode import HTMLNode
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        count = 0
        if node.text_type == TextType.NORMAL:
            for text in node.text.split(delimiter):
                if text != "":
                    type = TextType.NORMAL
                    if count % 2 != 0:
                        if count + 1 != len(node.text.split(delimiter)):
                            type = text_type
                    new_nodes.append(TextNode(text, type))
                count += 1
        else:
            new_nodes.append(node)

    return new_nodes
