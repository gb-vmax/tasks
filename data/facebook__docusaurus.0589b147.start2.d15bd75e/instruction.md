# Bug Report

### Describe the bug

I'm encountering an issue with fenced code blocks in markdown parsing. When a code fence closing delimiter has leading spaces, it's not being recognized properly and the code block doesn't close as expected.

### Reproduction

```markdown
```js
const example = 'test';
    ```
```

The closing fence with leading spaces should close the code block, but it seems to be treated as part of the code content instead.

### Expected behavior

According to the CommonMark spec, closing code fences can have up to 3 spaces of indentation (or 4 if code indentation is not disabled). The parser should recognize the closing delimiter even when it has leading whitespace within the allowed range.

### Additional context

This appears to affect how code blocks are parsed when the closing fence isn't flush left. The opening fence works fine, but closing fences with indentation are not being handled correctly.

---
Repository: /testbed
