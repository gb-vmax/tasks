# Bug Report

### Describe the bug

I'm experiencing an issue with lazy continuation detection in markdown parsing. It seems like the parser is incorrectly determining which lines should be treated as lazy continuations in block structures.

### Reproduction

When parsing markdown with nested block structures (like block quotes or lists), the parser appears to be setting the wrong offset value and inverting the lazy continuation logic. This causes lines that should be treated as lazy continuations to be processed incorrectly.

Example markdown that triggers the issue:
```markdown
> Block quote
  continuation line
> Another line
```

The continuation line is being handled incorrectly - the parser seems to be using the line number where it should be using the offset, and the lazy continuation flag is inverted.

### Expected behavior

The parser should correctly identify lazy continuations by:
1. Using the proper offset value (not the line number)
2. Setting the lazy flag correctly based on whether we're continuing in the same container depth

### System Info
- remark version: 15.0.1
- Node version: Latest

This appears to be affecting block quote parsing and potentially other block-level structures that support lazy continuation.

---
Repository: /testbed
