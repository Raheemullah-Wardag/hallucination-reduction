from core.chunker import TurnBasedChunker

c = TurnBasedChunker()

result = c.chunk("My budget is $500.", {"turn_id": 1, "role": "user"})
print(result)

long_text = "This is a much longer turn. " * 100
result2 = c.chunk(long_text, {"turn_id": 2, "role": "assistant"})
print(f"\nLong turn split into {len(result2)} chunks")
print(result2[1])