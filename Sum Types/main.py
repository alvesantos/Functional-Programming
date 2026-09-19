class MaybeParsed:
    pass


# Don't touch above this line


class Parsed(MaybeParsed):
    def __init__(self, doc_name: str, text: str) -> None:
        pass


class ParseError(MaybeParsed):
    def __init__(self, doc_name: str, err: str) -> None:
        pass
