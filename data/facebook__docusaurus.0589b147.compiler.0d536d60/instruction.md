# Bug Report

### Describe the bug

I'm encountering an issue with nested list parsing where the last item in a list is not being properly captured. It seems like list items at the end of the document or before certain boundaries are being truncated or ignored.

### Reproduction

```markdown
- First item
- Second item
- Third item
```

When parsing this markdown, the third item doesn't get fully processed. The issue appears to be related to how the parser iterates through events - it's stopping one event too early.

### Expected behavior

All list items should be parsed correctly, including the last one. The parser should process events up to and including the final event to ensure complete list item extraction.

### Additional context

This also affects nested structures where text nodes are being attached to the wrong parent element. When processing data tokens, the node selection seems to be off by one level in the stack, causing text to be added to an incorrect parent.

---
Repository: /testbed
