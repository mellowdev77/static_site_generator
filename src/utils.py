from block import block_to_block_type
from htmlnode import HTMLNode
import htmlnode
from parentnode import ParentNode
from textnode import TextNode, TextType, text_node_to_html_node
from block import *
import re

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

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        text = node.text
        images = extract_markdown_images(text)
        if len(images)> 0:
            for image in images:
                text_before = text.split(f"![{image[0]}]({image[1]})",1)[0]
                text_after = text.split(f"![{image[0]}]({image[1]})",1)[1]

                new_nodes.append(TextNode(text_before, TextType.NORMAL))
                new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))

                text = text_after
        if text != "":
            if node.text_type == TextType.LINK:
                new_nodes.append(TextNode(text, node.text_type, node.url))
            else:
                new_nodes.append(TextNode(text, node.text_type))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        text = node.text
        links = extract_markdown_links(text)
        if len(links)> 0:
            for link in links:
                text_before = text.split(f"[{link[0]}]({link[1]})",1)[0]
                text_after = text.split(f"[{link[0]}]({link[1]})",1)[1]

                new_nodes.append(TextNode(text_before, TextType.NORMAL))
                new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))

                text = text_after

        if text != "":
            if node.text_type == TextType.IMAGE:
                new_nodes.append(TextNode(text, node.text_type, node.url))
            else:
                new_nodes.append(TextNode(text, node.text_type))

    return new_nodes

def text_to_textnodes(text):
    text_node = TextNode(text, TextType.NORMAL)
    nodes = split_nodes_link([text_node])
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD )
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC )
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE )

    return nodes

def markdown_to_blocks(markdown):
    lines = markdown.split("\n")
    blocks = []
    current_block = ""
    for line in lines:
        if line.strip() == "":
            if current_block != "":
                blocks.append(current_block.strip())
                current_block = ""
        else:
            current_block += line.strip() + "\n"

    if current_block != "":
         blocks.append(current_block.strip())

    return blocks

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []

    for node in text_nodes:
        htmlnode = text_node_to_html_node(node)
        children.append(htmlnode)

    return children

def find_ashtags(text):
    count = 0
    for ch in text:
        if ch == "#":
            count += 1
        else:
            break

    return count

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        type = block_to_block_type(block)
        match type:
            case BlockType.PARAGRAPH:
                paragraph_node = HTMLNode("p", "", text_to_children(block))
                html_nodes.append(paragraph_node)
            case BlockType.CODE:
                code_content = "\n".join(block.split("\n")[1:-1])
                code_node = HTMLNode("code", "", [text_node_to_html_node(TextNode(code_content+"\n", TextType.NORMAL))])
                html_nodes.append(HTMLNode("pre", "", [code_node]))
            case BlockType.ORDERED_LIST:
                list_nodes = []
                for line in block.split("\n"):
                    list_nodes.append(HTMLNode("li", "", text_to_children(line[3:])))
                html_nodes.append(HTMLNode("ol", "", list_nodes))
            case BlockType.UNORDERED_LIST:
                list_nodes = []
                for line in block.split("\n"):
                    list_nodes.append(HTMLNode("li", "", text_to_children(line[2:])))
                html_nodes.append(HTMLNode("ul", "", list_nodes))
            case BlockType.QUOTE:
                quote_node = HTMLNode("blockquote", "", text_to_children(block[1:]))
                html_nodes.append(quote_node)
            case BlockType.HEADING:
                count = find_ashtags(block)
                heading_node = HTMLNode(f"h{count}", "", text_to_children(block[count+1:]))
                html_nodes.append(heading_node)

    return HTMLNode("div", "\n", html_nodes)
