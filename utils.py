def describe_attr(attr: str, value: bytes) -> str:
    return (
        f"{attr}: {value.hex()} ({len(value)})"
        f" | {value.decode('utf-8', errors='ignore')}"
    )
