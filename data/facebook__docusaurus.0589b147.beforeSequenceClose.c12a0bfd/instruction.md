# Bug Report

### Describe the bug

I'm encountering an issue with fenced code blocks in markdown parsing. When using code fences (triple backticks), the parser doesn't properly recognize the closing fence sequence and appears to be processing the code block incorrectly.

### Reproduction

```markdown
```js
function test() {
  return true;
}
```
```

When parsing this markdown, the closing fence sequence isn't being handled as expected. The code block either doesn't close properly or behaves unexpectedly.

### Expected behavior

The parser should correctly identify and match the opening and closing fence sequences (```), properly delimiting the code block content. Both the opening and closing fences should be recognized when they use the same marker character.

### Additional context

This seems to affect the tokenization logic for fenced code blocks. The issue appears when the parser encounters the closing sequence - it's not following the expected flow for matching fence markers.

---
Repository: /testbed
