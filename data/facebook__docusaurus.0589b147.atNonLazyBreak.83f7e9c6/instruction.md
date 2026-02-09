# Bug Report

### Describe the bug

I'm experiencing an issue with fenced code blocks in markdown parsing. When I have a fenced code block in my markdown content, the parser seems to be handling the closing fence incorrectly, causing the code block content to not be properly terminated.

### Reproduction

```markdown
```js
function test() {
  console.log('hello');
}
```
```

When parsing the above markdown with fenced code blocks, the parser doesn't correctly recognize where the code block ends. The closing fence (```) is not being processed as expected.

### Expected behavior

The parser should correctly identify the closing fence and properly terminate the fenced code block, allowing any content after the closing fence to be parsed as separate markdown elements.

### Additional context

This seems to affect code blocks with language identifiers (like ```js, ```python, etc.). The issue appears to be related to how the parser attempts to match the closing fence sequence.

---
Repository: /testbed
