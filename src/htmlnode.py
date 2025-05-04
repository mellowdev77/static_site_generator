class HTMLNode():
    def __init__(self, tag = None, value= None, children= None, props= None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        return_string = ""

        if self.props != None:
            return_string = " "
            for k,v in self.props.items():
                return_string += f"{k}='{v}' "

        return return_string.rstrip()

    def __repr__(self):
        return f"HTMLNode, {self.tag}, {self.value}, {self.children}, {self.props}"
