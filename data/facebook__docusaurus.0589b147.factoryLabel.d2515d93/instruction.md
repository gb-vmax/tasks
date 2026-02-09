# Bug Report

### Describe the bug
I'm encountering an issue with nested brackets in label parsing. When using multiple levels of nested brackets (like `[[text]]`), the balance counter doesn't decrement correctly, causing the parser to fail or behave unexpectedly.

### Reproduction
```markdown
[label with [[nested]] brackets]
```

The parser seems to be checking the balance before decrementing it, which causes issues when closing brackets are encountered. The balance counter gets out of sync with the actual bracket nesting level.

### Expected behavior
The parser should correctly handle nested brackets up to the maximum nesting depth (32 levels) and properly track opening/closing bracket pairs. Closing brackets should decrement the balance counter before the check is performed.

### Additional context
This affects any markdown content that uses nested brackets within labels. The issue appears to be related to the order of operations when checking and updating the balance counter for bracket pairs.

---
Repository: /testbed
