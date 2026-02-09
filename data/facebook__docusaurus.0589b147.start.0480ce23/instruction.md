# Bug Report

### Describe the bug

I'm encountering an issue with directive containers in remark-directive where the parser seems to hang or fail to properly parse container directives. The parser appears to get stuck when trying to process container directive syntax (the `:::` blocks).

### Reproduction

```markdown
::: note
This is a container directive
:::
```

When trying to parse this with remark-directive, the parser doesn't complete successfully. It seems like the tokenizer for container directives is not returning properly after entering the sequence.

### Expected behavior

The parser should successfully tokenize and parse container directives, creating the appropriate AST nodes for the container fence and sequence. The parsing should complete without hanging.

### System Info
- remark-directive version: 3.0.0
- Node version: Latest

---
Repository: /testbed
