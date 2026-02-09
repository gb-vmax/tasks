# Bug Report

### Describe the bug

I'm encountering an issue with fenced code blocks in MDX where the closing fence is not being recognized correctly. It seems like the parser is consuming characters incorrectly when processing the end of code blocks, causing the fence to not close properly.

### Reproduction

```mdx
```js
const example = 'test';
```
```

When parsing the above MDX content, the closing fence (```) doesn't work as expected. The code block either doesn't close or behaves unexpectedly.

### Expected behavior

The fenced code block should close properly when encountering the closing fence marker. The parser should correctly identify and process the fence closing sequence.

### Additional context

This appears to be related to how line endings are being processed in the tokenizer. The issue manifests when the parser tries to exit a code fence - something seems off with how the tokens are being consumed and labeled during the closing sequence.

---
Repository: /testbed
