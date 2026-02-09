# Bug Report

### Describe the bug

I'm encountering an issue with fenced code block parsing where the closing fence is not being recognized properly. It seems like the parser is treating the closing fence delimiter as content instead of as the end of the code block.

### Reproduction

```markdown
```js
const x = 1;
```
```

When parsing the above markdown, the closing fence (the second set of backticks) is being included as part of the code block content rather than being recognized as the delimiter that ends the code block.

### Expected behavior

The parser should correctly identify the closing fence and terminate the code block. The closing fence should not be included in the code block's content.

### Additional context

This appears to affect all fenced code blocks regardless of the info string (language identifier). The issue manifests when the parser encounters what should be a valid closing fence - it continues parsing as if it's still inside the code block content.

---
Repository: /testbed
