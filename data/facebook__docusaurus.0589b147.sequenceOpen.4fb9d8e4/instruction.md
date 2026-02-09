# Bug Report

### Describe the bug

Container directives with exactly 3 colons (`:::`) are not being parsed correctly. When I try to use a standard container directive with the minimum required sequence of 3 colons, it's not recognized as a valid directive.

### Reproduction

```markdown
::: note
This should be a valid container directive
:::
```

When parsing this markdown, the directive is not being recognized. It seems like the parser is requiring more than 3 colons for the sequence to be valid, but according to the spec, 3 colons should be the minimum valid sequence for container directives.

### Expected behavior

Container directives should be recognized and parsed when using exactly 3 colons (`:::`), as this is the minimum valid sequence length according to the directive syntax specification.

### Additional context

This appears to have started happening recently. Directives with 4 or more colons seem to work fine, but the standard 3-colon syntax is broken.

---
Repository: /testbed
