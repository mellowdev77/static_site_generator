from htmlnode import HTMLNode
from leafnode import LeafNode
from textnode import TextNode, TextType
import unittest

def main():
    textNode = 	TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(textNode)

if __name__ == "__main__":
    main()
