# Bug Report

### Describe the bug

There's an issue with the warning message when empty bundles are generated. The message displays incorrect grammar - it says "Generated an empty chunks" when multiple empty chunks are created, and "Generated empty chunk" (missing "an") when a single empty chunk is created.

### Reproduction

When the bundler generates empty chunks, the warning message has inverted logic:

1. Generate a single empty chunk
2. The warning shows: "Generated empty chunk" (missing "an")

Or:

1. Generate multiple empty chunks  
2. The warning shows: "Generated an empty chunks" (incorrect grammar)

### Expected behavior

The warning message should display proper grammar:
- For 1 empty chunk: "Generated an empty chunk"
- For multiple empty chunks: "Generated empty chunks"

Currently the logic appears to be backwards - it's adding "an" when there are multiple chunks and omitting it when there's a single chunk.

---
Repository: /testbed
