# Bug Report

### Describe the bug

After a recent update, code fencing in MDX files is completely broken. The parser seems to have lost the ability to properly tokenize fenced code blocks, causing the entire parsing process to fail.

### Reproduction

Try to parse any MDX file with a fenced code block:

```mdx
# My Document

```js
const example = 'test';
```

Some text after the code block.
```

The parser fails to recognize the code fence and throws errors or produces unexpected output.

### Expected behavior

Fenced code blocks should be properly tokenized and parsed. The `beforeSequenceOpen` function should initialize the fence sequence and handle the code block opening correctly.

### Additional context

This appears to affect all MDX files that contain triple backtick code blocks. The tokenization logic for code fences seems to have been replaced with unrelated normalization code, which doesn't make sense in this context.

---
Repository: /testbed
