# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where certain constructs are not being resolved correctly. It seems like some resolution functions are being skipped or called in the wrong order, causing the parsed output to be incomplete or malformed.

### Reproduction

```js
const remark = require('remark');
const processor = remark();

const markdown = `
**bold text** with _emphasis_

- list item 1
- list item 2
`;

const result = processor.parse(markdown);
// Some constructs are not properly resolved
console.log(result);
```

When parsing markdown with multiple constructs (like bold, emphasis, lists), some of them don't get processed correctly. The AST output is missing expected transformations or has incorrect structure.

### Expected behavior

All markdown constructs should be properly resolved and the resulting AST should reflect the correct structure with all resolution functions applied in the proper order.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
