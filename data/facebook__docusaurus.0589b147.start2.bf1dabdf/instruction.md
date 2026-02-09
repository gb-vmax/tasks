# Bug Report

### Describe the bug

I'm encountering an issue with code fence parsing in MDX. When a code fence is followed by a null character or end of file, the parser is not handling it correctly. The tokenizer seems to be consuming the line ending and then calling the wrong continuation function, which causes unexpected parsing behavior.

### Reproduction

```mdx
```js
const example = 'test';
```
[EOF]
```

When the parser encounters the end of a fenced code block followed by end-of-file or null, it doesn't properly validate the continuation state before proceeding.

### Expected behavior

The parser should check for null/EOF conditions before attempting to process line endings in the non-lazy continuation tokenizer. Code fences should be properly closed and validated even when they appear at the end of a document.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
