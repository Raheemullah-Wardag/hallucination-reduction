from core.chunker.base import BaseChunker, Chunk


class FixedSizeChunker(BaseChunker):
    """Splits text into fixed-size character windows with overlap."""

    def __init__(self, chunk_size: int = 800, overlap: int = 150):
        if overlap >= chunk_size:
            raise ValueError("overlap must be smaller than chunk_size")
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk(self, text: str, metadata: dict | None = None) -> list[Chunk]:
        base_metadata = metadata or {}
        text = text.strip()
        if not text:
            return []

        chunks: list[Chunk] = []
        start = 0
        index = 0
        step = self.chunk_size - self.overlap

        while start < len(text):
            end = min(start + self.chunk_size, len(text))
            piece = text[start:end].strip()

            if piece:
                chunks.append(
                    Chunk(
                        text=piece,
                        metadata={
                            **base_metadata,
                            "chunk_index": index,
                            "char_start": start,
                            "char_end": end,
                        },
                    )
                )
                index += 1

            if end == len(text):
                break
            start += step

        return chunks