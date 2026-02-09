# Bug Report

### Describe the bug

I'm encountering an issue with fenced code blocks in markdown parsing. When using code fences with backticks, the closing fence doesn't seem to be recognized properly in certain cases. The code block continues beyond where it should close, treating subsequent content as part of the code block instead of regular markdown.

### Reproduction

```markdown
```js
const foo = 'bar';
```

This text should be outside the code block but appears to be treated as part of it.
```

When parsing this markdown, the closing fence (the second set of three backticks) isn't being recognized correctly, causing the parser to treat everything after it as still being inside the fenced code block.

### Expected behavior

The closing fence should properly close the code block when it has the same number of backticks as the opening fence. Content after the closing fence should be parsed as normal markdown, not as part of the code block.

### System Info
- remark version: 15.0.1
- Node version: Latest

This seems to have started happening recently. Not sure if it's related to a recent change but wanted to report it in case others are seeing the same issue.

---
Repository: /testbed
