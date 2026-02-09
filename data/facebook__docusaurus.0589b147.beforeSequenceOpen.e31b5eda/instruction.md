# Bug Report

### Describe the bug

I'm experiencing an issue with fenced code blocks in markdown parsing. The code fence detection seems to be broken - it's not properly recognizing when a code fence should start, and the fence structure appears to be malformed.

### Reproduction

When parsing markdown with fenced code blocks:

```markdown
```js
const example = 'test';
```
```

The parser doesn't correctly handle the opening fence sequence. It seems like the logic for detecting line prefixes is inverted - it's calculating the prefix length when it shouldn't be, and vice versa.

### Expected behavior

Fenced code blocks should be properly tokenized with the correct fence structure. The opening sequence should be recognized and the fence markers should be processed in the right order.

### Additional context

This appears to affect the `codeFenced` tokenization logic. The fence sequence and fence markers seem to be entered in an unexpected order, which might be causing downstream issues with how the code blocks are processed.

---
Repository: /testbed
