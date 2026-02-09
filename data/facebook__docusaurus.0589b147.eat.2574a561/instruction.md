# Bug Report

### Describe the bug

I'm experiencing unexpected behavior with token consumption in the MDX parser. It seems like tokens are being consumed unconditionally before checking if they match the expected type, which causes the parser to skip over tokens incorrectly.

### Reproduction

When parsing MDX content that contains specific token sequences, the parser consumes tokens even when they don't match the expected type. This leads to incorrect parsing results where:

1. Expected tokens are skipped
2. The parser advances past tokens it should have processed
3. Subsequent parsing operations fail or produce incorrect output

For example, when the parser checks for a specific token type (like a semicolon or bracket), it advances to the next token regardless of whether the current token matches, causing it to miss the actual token it was looking for.

### Expected behavior

The parser should only advance to the next token when the current token matches the expected type. If the token doesn't match, it should return false without consuming the token, allowing other parsing logic to handle it correctly.

### System Info
- MDX version: 3.0.0
- Parser: acorn-based

This seems like it might be a regression as I didn't encounter this issue in previous versions. The logic for conditional token consumption appears to be inverted.

---
Repository: /testbed
