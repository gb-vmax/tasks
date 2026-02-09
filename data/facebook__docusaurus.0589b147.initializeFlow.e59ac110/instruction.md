# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where blank lines and line endings are not being handled correctly. It seems like the parser is not properly tracking the current construct state when processing line endings, which causes unexpected behavior in the tokenization flow.

### Reproduction

```js
const remark = require('remark');

const markdown = `
First paragraph

Second paragraph
`;

const result = remark.parse(markdown);
// The AST structure is malformed - line ending tokens are missing proper state transitions
```

When parsing markdown with multiple paragraphs separated by blank lines, the tokenizer doesn't correctly reset its state between constructs. This leads to incorrect AST generation where line endings aren't properly categorized as blank or regular line endings.

### Expected behavior

The parser should correctly identify and tokenize blank line endings and regular line endings, maintaining proper construct state throughout the parsing process. Each line ending should be properly entered/exited with the correct token type, and the `currentConstruct` should be reset appropriately between different markdown constructs.

### System Info
- remark version: 15.0.1
- Node.js version: 18.x

---
Repository: /testbed
