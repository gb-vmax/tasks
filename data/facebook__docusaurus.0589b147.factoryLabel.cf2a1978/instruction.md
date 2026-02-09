# Bug Report

### Describe the bug

I'm encountering an issue with nested bracket parsing in directive labels. When I use directives with nested brackets in the label text, the parser doesn't correctly handle the bracket balance tracking, causing unexpected behavior.

### Reproduction

```markdown
:directive[text with [nested brackets] inside]

:directive[multiple [nested [brackets]] here]
```

The parser seems to get confused when processing the closing bracket - it's not properly decrementing the balance counter before checking if we've reached the final closing bracket. This means nested brackets aren't being parsed correctly.

### Expected behavior

The directive parser should correctly handle labels with nested brackets by properly tracking the bracket balance. When encountering a closing bracket `]`, it should first decrement the balance counter and then check if the balance is zero to determine if we've reached the end of the label.

### System Info
- remark-directive version: 3.0.0

---
Repository: /testbed
