from textnode import TextNode, TextType

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None:
            return ""
        attr_list = [f' {key}="{value}"' for key, value in self.props.items()]
        return "".join(attr_list)
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value is None or self.value == "":
            raise ValueError("LeafNode must have a value.")
        if self.tag is None or self.tag == "":
            return str(self.value)
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)
        if self.tag == None:
            raise ValueError("ParentNode must have a tag.")
        if self.children == None:
            raise ValueError("ParentNode must have children.")

    def to_html(self):
        children_html = "".join(child.to_html() for child in self.children)
        return f"<{self.tag}>{children_html}</{self.tag}>"
    
def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.NORMAL:
        return LeafNode(tag=None, value=str(text_node.text))
    elif text_node.text_type == TextType.BOLD:
        return LeafNode(tag="b", value=text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode(tag="i", value=text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode(tag="code", value=text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode(tag="a", value=text_node.text, props={"href": str(text_node.url)})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode(tag="img", value="", props={"src": str(text_node.url), "alt": str(text_node.text)})
    raise Exception("TextNode must be a valid text type.")