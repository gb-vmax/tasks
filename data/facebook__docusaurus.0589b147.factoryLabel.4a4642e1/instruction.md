# Bug Report

### Describe the bug

I'm encountering an issue with nested bracket handling in directive labels. When using directives with labels containing balanced brackets, the parser seems to incorrectly handle the closing bracket detection, especially in edge cases where the bracket balance count becomes negative.

### Reproduction

```markdown
::directive[label with [nested] brackets]
```

The parser appears to have issues when processing labels with nested brackets. The bracket balance tracking doesn't work correctly, which can lead to incorrect parsing of the label content or premature termination of label parsing.

### Expected behavior

The parser should correctly handle nested brackets in directive labels by:
1. Properly tracking opening `[` and closing `]` brackets
2. Only closing the label when the bracket balance returns to zero
3. Handling edge cases where bracket counts might go negative

The current implementation seems to check the balance in a way that doesn't correctly decrement before comparison, which could cause the wrong bracket to be treated as the label's closing bracket.

### System Info
- remark-directive version: 3.0.0
- Parser: micromark-based

---
Repository: /testbed
