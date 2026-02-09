# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where blank lines with leading whitespace are not being handled correctly. The parser seems to be applying the wrong tokenization logic for lines that contain only spaces/tabs before a line ending.

### Reproduction

```js
const markdown = `
First paragraph

    
Second paragraph
`;

// Parse the markdown
const result = remark.parse(markdown);

// The blank line with leading spaces is not recognized properly
// Expected: blank line should be tokenized correctly regardless of whitespace
// Actual: parsing behavior is incorrect for blank lines with prefix spaces
```

### Expected behavior

Blank lines should be properly recognized and tokenized even when they contain leading whitespace (spaces or tabs) before the line ending. The `linePrefix` factory should be applied when markdown spaces are detected, not skipped.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This seems to have broken the handling of indented blank lines in markdown documents. The tokenizer is now taking the wrong branch when it encounters spaces at the start of what should be a blank line.

---
Repository: /testbed
