# Bug Report

### Describe the bug

I'm experiencing an issue with fenced code blocks in markdown parsing. When a code fence closing delimiter has leading whitespace, the parser doesn't handle it correctly. The code block either doesn't close properly or the whitespace handling seems inverted from what it should be.

### Reproduction

```markdown
```js
const example = 'test';
```
```

When the closing fence has spaces before the backticks, the code block parsing breaks. It seems like the parser is treating whitespace incorrectly when checking for the closing fence sequence.

### Expected behavior

The parser should properly handle closing code fences with leading whitespace (up to the indent limit), and correctly identify when a closing fence is valid. The whitespace should be consumed before checking for the fence sequence, not after.

### Additional context

This affects any markdown document with indented closing code fences, which is a common pattern especially in nested contexts like list items or blockquotes. The issue appears to be related to how the tokenizer processes whitespace when looking for the closing fence marker.

---
Repository: /testbed
