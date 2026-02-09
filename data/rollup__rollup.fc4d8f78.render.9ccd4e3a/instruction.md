# Bug Report

### Describe the bug

I'm encountering an issue where semicolons are being inserted in the wrong position for expression statements. After the code is processed, semicolons appear to be placed incorrectly, which can break the generated output.

### Reproduction

When an expression statement is rendered, the semicolon insertion logic seems to check and insert at an incorrect position. This causes the semicolon to be added in the wrong location relative to the expression statement.

For example, with code like:
```js
someFunction()
```

The semicolon ends up in an unexpected position instead of being properly appended after the statement.

### Expected behavior

Semicolons should be correctly appended at the end of expression statements when they're missing. The check should verify if a semicolon already exists at the correct position and insert it at the proper location if needed.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
