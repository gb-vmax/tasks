# Bug Report

### Describe the bug

After a recent update, container directive labels are being parsed with an incorrect node type. Instead of creating a `paragraph` node with `directiveLabel` metadata in the `data` field, the parser is now generating a `containerLabel` node type with `directiveLabel` as a direct property.

This breaks compatibility with existing code that expects directive labels to be represented as paragraph nodes with the `directiveLabel` flag in the data object.

### Reproduction

```js
const remark = require('remark')
const directive = require('remark-directive')

const input = `
:::note[This is a label]
Content here
:::
`

const ast = remark().use(directive).parse(input)

// The label node now has:
// { type: "containerLabel", directiveLabel: true, ... }
// 
// But it should have:
// { type: "paragraph", data: { directiveLabel: true }, ... }
```

### Expected behavior

Container directive labels should be parsed as `paragraph` nodes with `data.directiveLabel` set to `true`, maintaining backward compatibility with the previous AST structure.

### System Info
- remark-directive version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
