# Bug Report

### Describe the bug

I'm encountering an issue with fenced code blocks in markdown parsing. When a code fence is immediately followed by EOF (end of file) without any line ending, the parser seems to hang or behave unexpectedly. The code block doesn't get properly recognized and the document structure appears corrupted.

### Reproduction

```js
const markdown = '```javascript';
// No newline or closing fence, just EOF

// Parser fails to handle this correctly
```

Try parsing a markdown document that has a fenced code block opener (like ````javascript`) but ends immediately without a newline character or closing fence. The parser should handle this gracefully but instead produces unexpected results.

### Expected behavior

The parser should properly handle edge cases where code fences are at the end of a file without line endings. It should either:
- Treat it as an unclosed code fence and handle it appropriately
- Not hang or produce corrupted output

### Additional context

This seems related to how the tokenizer checks for null vs line endings when processing code fence info. The issue appears when there's no content after the opening fence markers.

---
Repository: /testbed
