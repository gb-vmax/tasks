# Bug Report

### Describe the bug

I'm experiencing an issue with fenced code blocks in MDX. When a fenced code block is followed by certain content, the parser seems to incorrectly handle the continuation logic. The code block doesn't close properly and subsequent content gets parsed incorrectly.

### Reproduction

```mdx
```js
const example = 'test';
```

Some text after the code block
```

The parser appears to be checking for null values in the wrong way when processing non-lazy continuation, causing the code block tokenization to fail. This results in the code block not being recognized correctly and the following content being misinterpreted.

### Expected behavior

The fenced code block should be properly closed and parsed, and any content following it should be treated as regular MDX content. The null check in the continuation logic should allow the code block to terminate correctly.

### System Info
- @mdx-js/mdx version: 3.0.0
- Parser: micromark-based tokenizer

---
Repository: /testbed
