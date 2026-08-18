from core.chunker.base import BaseChunker, Chunk


class TurnBasedChunker(BaseChunker):
    """One chunk per conversational turn. Falls back to paragraph/hard
    splitting only if a single turn is unusually long.
    """

    def __init__(self, turns_per_chunk: int = 1, max_chars: int = 2000):
        self.turns_per_chunk = turns_per_chunk
        self.max_chars = max_chars

    def chunk(self, text: str, metadata: dict | None = None) -> list[Chunk]:
        base_metadata = metadata or {}
        text = text.strip()
        if not text:
            return []

        if len(text) <= self.max_chars:
            return [Chunk(text=text, metadata={**base_metadata, "chunk_index": 0})]

        chunks: list[Chunk] = []
        index = 0
        for para in text.split("\n\n"):
            para = para.strip()
            if not para:
                continue
            for i in range(0, len(para), self.max_chars):
                piece = para[i : i + self.max_chars].strip()
                if piece:
                    chunks.append(
                        Chunk(text=piece, metadata={**base_metadata, "chunk_index": index})
                    )
                    index += 1
        return chunks