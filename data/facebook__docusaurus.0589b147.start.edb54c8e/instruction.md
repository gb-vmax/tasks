# Bug Report

### Describe the bug

I'm experiencing an issue with markdown link parsing where the parser seems to be entering/exiting token states in an incorrect order. When processing link labels, the parser behavior appears inconsistent and may be causing malformed output or parsing errors.

### Reproduction

```markdown
[example link](https://example.com)
```

When the above markdown is parsed, the link label tokenization doesn't work as expected. The token state transitions appear to be happening in the wrong sequence, which could lead to incorrect AST generation.

### Expected behavior

Link labels should be properly tokenized with correct entry/exit order for the labelLink and labelMarker states. The parser should maintain proper nesting of token states throughout the parsing process.

### Additional context

This seems to affect basic link syntax parsing. Not sure if this impacts all link types or just specific cases, but wanted to report what I'm seeing.

---
Repository: /testbed
