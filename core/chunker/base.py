from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Chunk:
    text: str
    metadata: dict  # e.g. {"turn_id": 12, "role": "user", "chunk_index": 0}

class BaseChunker(ABC):
    @abstractmethod
    def chunk(self, text: str, metadata: dict | None = None) -> list[Chunk]:
        """Split text into a list of Chunk objects."""
        ...