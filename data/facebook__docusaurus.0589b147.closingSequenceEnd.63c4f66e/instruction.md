# Bug Report

### Describe the bug

I'm experiencing an issue with directive container parsing where the closing fence is not being validated correctly. It appears that containers are being closed even when there's content after the closing fence on the same line, which shouldn't be allowed according to the directive syntax spec.

### Reproduction

```markdown
:::note
Some content here
::: extra text that should invalidate the closing fence
```

The parser is treating the third line as a valid closing fence even though it has "extra text" after the colons. This causes the container to close prematurely instead of treating that line as content within the container.

### Expected behavior

The closing fence should only be valid if it's followed by a line ending (or EOF). Any additional content on the same line should invalidate it as a closing fence, and the line should be treated as part of the container's content instead.

A valid closing would be:
```markdown
:::note
Some content here
:::
```

But this should NOT close the container:
```markdown
:::note
Some content here
::: this text invalidates the fence
```

### System Info
- remark-directive version: 3.0.0
- Parser: micromark

---
Repository: /testbed
