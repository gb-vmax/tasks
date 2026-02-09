# Bug Report

### Describe the bug

I'm experiencing an issue with directive label parsing in remark-directive. When using directives with labels, the parser seems to be behaving incorrectly - it's either not properly handling the label content or exiting the parsing state prematurely.

### Reproduction

```markdown
:directive[some label text]

::directive[multi-line
label content]
```

When parsing directives with labels like the examples above, the parser doesn't correctly process the label content. It appears to be skipping or incorrectly handling the string content between the brackets.

### Expected behavior

The directive labels should be properly parsed and the content between `[` and `]` should be captured as the label text. The parser should correctly handle both simple and multi-line label content.

### Additional context

This seems to affect any directive that uses the label syntax with square brackets. The issue manifests when the parser encounters the opening bracket and tries to determine whether it's an empty label or one with content.

---
Repository: /testbed
