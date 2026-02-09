# Bug Report

### Describe the bug

I'm encountering an issue with code fence parsing where fenced code blocks are not being properly recognized and closed. The parser seems to be rejecting valid code fence closings, causing markdown with code blocks to fail parsing or render incorrectly.

### Reproduction

```markdown
```js
const example = 'test';
```
```

When trying to parse the above markdown with a fenced code block, the closing fence is not being recognized properly. The parser appears to be treating valid closing sequences as invalid.

### Expected behavior

Code fences should be properly closed when encountering a matching fence sequence followed by either:
- End of file (null)
- A line ending

The closing fence should be accepted in both cases and the code block should parse correctly.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
