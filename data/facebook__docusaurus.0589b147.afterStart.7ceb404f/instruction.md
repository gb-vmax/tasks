# Bug Report

### Describe the bug

I'm encountering an issue with directive labels in remark-directive where empty labels (e.g., `[]`) are not being parsed correctly. The parser seems to be handling the closing bracket in the wrong order, which causes the label parsing to fail or produce unexpected results.

### Reproduction

```markdown
:directive[]

:directive[some text]
```

When parsing directives with empty labels or labels with content, the output is malformed. The closing bracket isn't being processed in the correct sequence, leading to incorrect AST generation.

### Expected behavior

Directives with empty labels should be parsed correctly and produce a valid AST node. The label markers should be properly entered and exited in the correct order during tokenization.

### Additional context

This appears to be related to how the `afterStart` function handles the label closing bracket (code 93). The marker entry/exit sequence seems to be out of order, which might be causing the parser state machine to get confused.

---
Repository: /testbed
