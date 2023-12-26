def read_in(path: str) -> str:
    f = open(f"inputs/{path}")
    return f.read().strip()
