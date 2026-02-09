# Bug Report

### Describe the bug

I'm experiencing an issue with HTML node parsing in the remark processor. When parsing markdown that contains HTML elements, the nodes are being created with incorrect type and value properties. Instead of getting HTML nodes with proper string values, I'm getting text nodes with null values.

### Reproduction

```js
const remark = require('remark');
const processor = remark();

const markdown = `
Some text with <span>inline HTML</span>
`;

const ast = processor.parse(markdown);
// Inspect the AST nodes - HTML elements are not being parsed correctly
console.log(ast);
```

### Expected behavior

HTML elements in markdown should be parsed as nodes with:
- `type: "html"`
- `value: ""` (empty string or the actual HTML content)

Instead, they appear to be created as text nodes with null values, which causes issues when trying to process or stringify the AST.

### System Info
- remark version: 15.0.1
- Node.js version: 18.x

This is breaking my markdown processing pipeline since downstream tools expect proper HTML node types. Any help would be appreciated!

---
Repository: /testbed
