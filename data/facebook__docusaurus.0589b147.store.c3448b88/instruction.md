# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where the parser position tracking seems to be getting corrupted during tokenization. After certain parsing operations, the parser appears to lose track of its current position in the document and starts parsing from the wrong location.

### Reproduction

This seems to happen when the tokenizer needs to backtrack and restore a previous state. The parser position doesn't get properly restored, causing subsequent parsing to occur at incorrect positions in the source text.

Example scenario:
1. Parser encounters a construct that requires lookahead
2. Parser stores current state to potentially backtrack
3. Parser attempts to parse the construct
4. Parser restores previous state
5. Parser position is now incorrect and parsing continues from wrong location

### Expected behavior

When the parser backtracks and restores a previous state, it should restore the exact position (line and column) where it was before attempting the construct. The parser should continue from the correct position in the source document.

### Additional context

This appears to be related to state management in the tokenizer's `store()` and `restore()` functions. The issue manifests as parsing errors or incorrect AST generation for valid MDX documents, particularly those with complex nested structures.

---
Repository: /testbed
