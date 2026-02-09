# Bug Report

### Describe the bug

I'm encountering an issue with code fence parsing in MDX where fenced code blocks are not being properly recognized or tokenized. The parser seems to fail silently when processing markdown with code fences, resulting in incorrect output or the code blocks not being rendered at all.

### Reproduction

```mdx
# Test Document

Some text before the code block.

```js
const example = 'test';
console.log(example);
```

More text after the code block.
```

When parsing this MDX content, the code fence doesn't get properly tokenized and the output is malformed.

### Expected behavior

The code fence should be correctly identified and parsed, with the fenced code block being properly rendered in the output. The tokenizer should handle the sequence of backticks and process the code content within the fence boundaries.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This appears to have started happening recently. Any help would be appreciated!

---
Repository: /testbed
