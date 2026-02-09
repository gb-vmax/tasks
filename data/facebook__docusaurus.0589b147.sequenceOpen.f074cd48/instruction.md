# Bug Report

### Describe the bug

I'm experiencing an issue with inline code parsing in markdown. When using backticks to create inline code spans, the parser seems to be breaking on certain patterns, particularly when multiple consecutive backticks are used.

### Reproduction

```js
const markdown = '`code`';
// Parse this markdown string
```

When parsing markdown with inline code (backticks), the tokenizer appears to exit the code text sequence prematurely. This affects any markdown content that uses backticks for inline code formatting.

### Expected behavior

The parser should correctly tokenize inline code sequences and properly handle the opening backtick sequence before moving to the content between the backticks. The tokenizer should continue processing the opening sequence until all backticks are consumed.

### Additional context

This seems to affect the `tokenizeCodeText` function in the remark parser. The issue manifests when trying to parse any markdown content with inline code blocks using backticks.

---
Repository: /testbed
