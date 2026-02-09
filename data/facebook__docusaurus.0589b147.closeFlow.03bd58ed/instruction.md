# Bug Report

### Describe the bug

I'm encountering an issue with the remark parser where it seems to be handling flow content incorrectly in certain cases. When processing markdown documents with nested container structures, the parser appears to be passing invalid data internally.

### Reproduction

```js
const remark = require('remark');

const markdown = `
> Block quote with nested content
> 
> - List item 1
> - List item 2
`;

const processor = remark();
const result = processor.parse(markdown);
```

When parsing markdown with nested block structures (like block quotes containing lists), the parser throws an error or produces unexpected results. This seems to be related to how the document flow is being closed/finalized.

### Expected behavior

The parser should correctly handle nested container structures and properly close flow content without errors. The markdown should parse successfully and produce a valid AST.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
