# Bug Report

### Describe the bug

I'm encountering an issue with the markdown parser where it appears to be processing tokens with arguments in the wrong order. When parsing markdown content, the tokenizer seems to be receiving parameters in an unexpected sequence, which leads to incorrect parsing behavior.

### Reproduction

```js
const parser = parse(options);
const tokenizer = parser.text(from);
// The tokenizer receives 'from' and 'initial' in wrong order
// This causes parsing to fail or produce unexpected results
```

When creating a tokenizer through the `create()` function, the parameters being passed to `createTokenizer` don't match what's expected, resulting in malformed token processing.

### Expected behavior

The tokenizer should receive the correct parameters in the proper order so that markdown content is parsed correctly. The `createTokenizer` function should get the parser, initial value, and from value in the right sequence.

### System Info
- remark version: 15.0.1
- Environment: Node.js

This seems to have broken basic markdown parsing functionality. Any text processing that relies on the tokenizer is affected.

---
Repository: /testbed
