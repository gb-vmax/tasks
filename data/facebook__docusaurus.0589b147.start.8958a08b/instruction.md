# Bug Report

### Describe the bug

I'm experiencing an issue with inline code parsing in markdown. When trying to parse text containing backtick-delimited code spans, the parser seems to be producing incorrect token ordering or failing to properly tokenize the content.

### Reproduction

```js
// Parsing markdown with inline code
const markdown = 'This is `inline code` in text';

// The tokenization appears to be broken
// Expected: proper code text tokens
// Actual: incorrect token structure or parsing failure
```

### Expected behavior

Inline code blocks wrapped in backticks should be properly tokenized with the correct token hierarchy. The `codeText` and `codeTextSequence` tokens should be created in the proper order to allow correct parsing of the markdown content.

### System Info
- remark version: 15.0.1
- Node version: Latest

This seems to have broken recently and is affecting all inline code parsing in my markdown documents. Any help would be appreciated!

---
Repository: /testbed
