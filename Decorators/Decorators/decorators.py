from collections.abc import Callable

def markdown_to_text_decorator(func: Callable[..., str]) -> Callable[..., str]:
    def wrapper(*args: str, **kwargs: str) -> str:
        md_to_args = list(map(convert_md_to_txt, args))
        md_to_kwargs = {}

        for key, value in kwargs.items():
            md_txt = convert_md_to_txt(value)
            md_to_kwargs[key] = md_txt

        return func(*md_to_args, **md_to_kwargs)

    return wrapper


# Don't touch below this line
def convert_md_to_txt(doc: str) -> str:
    lines = doc.split("\n")
    for i in range(len(lines)):
        line = lines[i]
        lines[i] = line.lstrip("# ")
    return "\n".join(lines)