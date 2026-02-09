# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where the parser seems to hang or behave incorrectly when processing certain text content. The parser appears to get stuck in an infinite loop or produces unexpected output when encountering null/EOF characters in specific scenarios.

### Reproduction

```js
// When parsing markdown text that ends abruptly or contains certain patterns
const markdown = `Some text content`;

// Parser hangs or produces incorrect output
const result = parse(markdown);
```

The issue seems to occur specifically when the parser reaches the end of input (null character) in certain text processing states. The behavior is inconsistent and doesn't match what I'd expect from normal markdown parsing.

### Expected behavior

The parser should handle end-of-file gracefully and complete parsing without hanging or producing malformed output. Text content should be properly recognized and processed even when reaching null/EOF characters.

### System Info

- remark version: 15.0.1
- Node version: Latest

This might be related to how the text tokenizer handles state transitions when encountering null characters. Any help would be appreciated!

---
Repository: /testbed
