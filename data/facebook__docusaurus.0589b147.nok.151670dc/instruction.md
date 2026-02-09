# Bug Report

### Describe the bug

I'm experiencing an issue with the markdown parser where it seems to be skipping constructs during tokenization. When parsing certain markdown content, the parser appears to be jumping over valid constructs and not processing them correctly.

### Reproduction

```js
const remark = require('remark');

const markdown = `
# Test Header
Some text with **bold** and *italic*
- List item 1
- List item 2
`;

const result = remark().parse(markdown);
console.log(result);
```

When running this, some of the markdown constructs are not being parsed as expected. It seems like the tokenizer is incrementing through the construct list incorrectly and missing valid matches.

### Expected behavior

All markdown constructs should be properly tokenized and parsed. The parser should try each construct in the list until it finds a match, without skipping any.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
