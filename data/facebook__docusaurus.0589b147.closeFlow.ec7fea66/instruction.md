# Bug Report

### Describe the bug

I'm encountering an issue where the markdown parser crashes when processing certain document structures. The error occurs during the flow closing phase and results in an attempt to call a method on an undefined object.

### Reproduction

```js
const remark = require('remark');

const markdown = `
# Heading

Some content with nested structures

- List item 1
- List item 2
`;

// This causes a crash
remark().parse(markdown);
```

The parser throws an error when trying to close the flow context, specifically when it attempts to write to a flow object that has already been set to undefined.

### Expected behavior

The markdown should parse successfully without throwing any errors. The parser should properly handle the cleanup of flow contexts in the correct order.

### System Info
- remark version: 15.0.1
- Node.js version: 18.x

This seems to be a regression as similar markdown was parsing fine in previous versions. Any help would be appreciated!

---
Repository: /testbed
