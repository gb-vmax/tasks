# Bug Report

### Describe the bug

I'm encountering an issue with directive container parsing in remark-directive. When using container directives with closing fences, the parser is not correctly recognizing valid closing sequences. It seems like the closing fence validation logic is inverted or has the wrong conditions.

### Reproduction

```markdown
:::note
This is a container directive
:::
```

When parsing the above markdown, the closing fence `:::` is not being properly recognized. The parser either:
1. Accepts closing fences that should be rejected (when they have trailing content)
2. Rejects closing fences that should be accepted (when they match or exceed the opening fence length)

### Expected behavior

The parser should correctly identify closing fences that:
- Have the same or greater number of colons as the opening fence
- Are followed only by whitespace or end of line
- Don't have any other trailing content

The closing fence should properly close the container directive and allow the content to be parsed as expected.

### System Info
- remark-directive version: 3.0.0
- Node version: Latest

---
Repository: /testbed
