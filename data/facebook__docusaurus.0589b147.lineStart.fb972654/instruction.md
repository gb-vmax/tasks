# Bug Report

### Describe the bug

I'm encountering an issue with directive parsing where labels with nested brackets are not being handled correctly. When a directive label contains balanced brackets (e.g., `[text [nested] text]`), the parser seems to be closing the label prematurely instead of properly tracking bracket balance.

### Reproduction

```markdown
:directive[This is a label with [nested brackets] inside]

:directive[Label with [[double nested]] content]
```

The parser appears to be treating the first closing bracket `]` as the end of the label, even when there are unclosed opening brackets before it.

### Expected behavior

The parser should properly track bracket balance and only close the label when all opening brackets have been matched with their corresponding closing brackets. Labels with nested brackets should be fully captured.

For example:
- `[text [nested] text]` should parse the entire content including the nested brackets
- `[[double nested]]` should correctly handle double-nested brackets

### Additional context

This seems to affect any directive that uses bracket notation for labels when the content itself contains brackets. The bracket balancing logic doesn't appear to be working as intended.

---
Repository: /testbed
