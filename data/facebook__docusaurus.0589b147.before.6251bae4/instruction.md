# Bug Report

### Describe the bug

I'm encountering an issue with ATX heading parsing where the heading sequence token is being entered after the sequence has already been opened. This causes the token structure to be malformed and breaks the expected order of effects.

### Reproduction

When parsing markdown with ATX headings (headings that use `#` symbols), the tokenizer is calling `sequenceOpen()` before entering the `atxHeadingSequence` token, which results in an incorrect token tree structure.

```markdown
# Heading 1
## Heading 2
### Heading 3
```

The current implementation attempts to return the result of `sequenceOpen()` before properly entering the heading sequence token, which means the token boundaries are not correctly established before the sequence is consumed.

### Expected behavior

The `atxHeadingSequence` token should be entered **before** calling `sequenceOpen()` to ensure proper token nesting and that all effects are applied in the correct order. The sequence should only be opened after the token context has been properly established.

### System Info
- Package: @mdx-js/mdx
- Version: 3.0.0

---
Repository: /testbed
