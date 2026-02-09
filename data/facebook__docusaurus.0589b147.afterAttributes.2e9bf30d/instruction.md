# Bug Report

### Describe the bug

I'm encountering an issue with directive parsing where the whitespace handling after attributes seems to be broken. When using leaf directives with attributes, the parser is not correctly processing the whitespace that follows.

### Reproduction

```markdown
::directive[label]{attr="value"} some text
```

When parsing the above directive, the whitespace after the attributes block is not being handled properly, which causes the parser to fail or behave unexpectedly.

### Expected behavior

The directive should parse correctly with proper whitespace handling after the attributes section. The whitespace between the closing brace `}` and any following content should be consumed appropriately.

### System Info
- remark-directive version: 3.0.0

---
Repository: /testbed
