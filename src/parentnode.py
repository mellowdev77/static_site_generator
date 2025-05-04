from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, children = children, props=props)

    def to_html_recur(self):
        if self.tag == None:
            raise ValueError("Parent node needs a tag")

        if self.children == None:
            raise ValueError("No children on ParentNode")

        if len(self.children) == 0:
            return f"<{self.tag}>{self.value}</{self.tag}>"

        text = f"<{self.tag}>"
        for child in self.children:
            if child.children != None:
                text += child.to_html_recur()
            else:
                text += f"<{child.tag}>{child.value}</{child.tag}>"

        return text + f"</{self.tag}>"
