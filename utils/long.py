def split(text, limit=2000):
    """
    Splits a long string into a list of strings each <= limit characters.
    Splits on newline if possible to keep messages readable.
    """
    chunks = []
    while len(text) > limit:
        # Try to break on the last newline before limit
        split_at = text.rfind('\n', 0, limit)
        if split_at == -1:
            # No newline found, hard split at limit
            split_at = limit
        chunks.append(text[:split_at])
        text = text[split_at:].lstrip('\n')  # remove leading newlines
    chunks.append(text)
    return chunks

