# Bug Report

### Describe the bug

I'm experiencing an issue with directive container parsing where the closing fence is not being validated correctly. It appears that any content after the closing fence sequence is now being accepted, when it should only accept the fence if it's followed by a line ending or EOF.

### Reproduction

```markdown
:::note
Some content
::: extra text that should not be allowed
```

The parser is incorrectly treating this as a valid closing fence even though there's additional text after the fence sequence. According to the CommonMark directive spec, the closing fence should only be valid if followed by optional whitespace and then a line ending or end of file.

### Expected behavior

The closing fence should only be recognized as valid when followed by whitespace and a line ending (or EOF). Any other characters after the fence sequence should cause the fence to be rejected, and the line should be treated as regular content within the container.

So the example above should NOT close the container, and instead the `:::` with extra text should be parsed as content within the note directive.

### System Info
- remark-directive version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
