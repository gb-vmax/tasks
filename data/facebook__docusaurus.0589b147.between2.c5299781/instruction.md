# Bug Report

### Describe the bug

I'm experiencing an issue with inline code parsing in markdown. When I have spaces inside backtick code blocks, they're not being handled correctly. The parser seems to be ignoring or skipping over spaces (character code 32) in certain situations.

### Reproduction

```js
// This markdown isn't being parsed correctly:
const markdown = "This is `some code` with spaces";

// The space characters inside the backticks are not being processed as expected
```

When parsing inline code that contains spaces, the tokenizer appears to skip the space handling logic. This affects any markdown content with inline code that has spaces.

### Expected behavior

Spaces inside inline code blocks (backticks) should be properly tokenized and preserved. The parser should recognize character code 32 (space) and handle it appropriately during the tokenization process.

### System Info
- remark version: 15.0.1
- Node version: Latest

This seems to have broken recently. Any help would be appreciated!

---
Repository: /testbed
