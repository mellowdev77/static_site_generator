from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST= "ordered_list"

def block_to_block_type(markdown):
    type = None
    if markdown != "":
        match markdown[0]:
            case "#":
                count = 0
                for c in markdown:
                    if c == "#":
                        count += 1
                        continue
                    if c == " " and count <=6:
                        type = BlockType.HEADING
                        continue
                    break
            case "`":
                if len(markdown) > 6 and markdown[:3] == "```" and markdown[-3:] == "```":
                    type = BlockType.CODE
            case ">":
                type = BlockType.QUOTE
            case "-":
                if markdown.startswith("- "):
                       for line in markdown.split("\n"):
                           if not line.startswith("- "):
                               return BlockType.PARAGRAPH
                       return BlockType.UNORDERED_LIST
            case "1":
                if markdown.startswith("1. "):
                        i = 1
                        for line in markdown.split("\n"):
                            if not line.startswith(f"{i}. "):
                                return BlockType.PARAGRAPH
                            i += 1
                        return BlockType.ORDERED_LIST
            case _:
                type = BlockType.PARAGRAPH

    if type == None:
        return BlockType.PARAGRAPH
    return type
