from textnode import TextNode, TextType

def main():
    a = TextNode("This is some anchor text", TextType.LINK_TEXT, "https://www.boot.dev")
    print(a)

if __name__ == "__main__":
    main()