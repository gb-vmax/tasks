# Bug Report

### Describe the bug

I'm encountering an issue with markdown parsing where certain content is not being processed correctly. It seems like the tokenizer is returning early when it shouldn't, causing some markdown elements to be skipped or not rendered properly.

### Reproduction

```js
const remark = require('remark');
const processor = remark();

const markdown = `
# Header

Some paragraph text with **bold** and *italic*.

- List item 1
- List item 2
`;

const result = processor.processSync(markdown);
console.log(result);
```

When processing markdown with multiple elements, some tokens appear to be missing from the output. The parser seems to be stopping prematurely instead of processing all the content.

### Expected behavior

All markdown elements should be tokenized and included in the output. The parser should continue processing until all content has been consumed, not return early when there's still content to process.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
