class HTMLNode():
    def __init__(self, tag = None, value= None, children= None, props= None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        if self.children is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"

        children_html = ""
        for child in self.children:
            children_html += child.to_html()

        return f"<{self.tag}>{children_html}</{self.tag}>"

    def props_to_html(self):
        return_string = ""

        if self.props != None:
            return_string = " "
            for k,v in self.props.items():
                return_string += f"{k}='{v}'"

        return return_string.rstrip()

    def __repr__(self):
        return f"HTMLNode, {self.tag}, {self.value}, {self.children}, {self.props}"
