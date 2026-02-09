# Bug Report

### Describe the bug

I'm experiencing an issue with the markdown parser where it's skipping elements when processing nested structures. It seems like the parser is popping elements from the stack incorrectly, causing some content to be lost or misprocessed.

### Reproduction

```js
const remark = require('remark');

const markdown = `
- Item 1
  - Nested item 1
  - Nested item 2
- Item 2
`;

const result = remark().parse(markdown);
console.log(result);
```

When parsing nested lists or other nested markdown structures, some items appear to be missing from the output. The structure seems corrupted and doesn't match the input.

### Expected behavior

The parser should correctly handle all nested elements and preserve the complete structure of the markdown document. All list items should be present in the parsed output.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
