# Bug Report

### Describe the bug
When parsing container directives with labels, the metadata property name is incorrect. The parser is setting `metadata.labelDirective` instead of `data.directiveLabel`, which breaks compatibility with code that expects the standard property structure.

### Reproduction
```js
// Parse a container directive with a label
const ast = parse(':::note[Some label]\nContent\n:::')

// The paragraph node for the label has the wrong structure
// Current (incorrect): { type: 'paragraph', metadata: { labelDirective: true }, ... }
// Expected: { type: 'paragraph', data: { directiveLabel: true }, ... }
```

### Expected behavior
The label paragraph node should have a `data` property with `directiveLabel: true`, not a `metadata` property with `labelDirective: true`. This is the documented structure for directive labels and changing it breaks existing parsers/transformers that rely on this property.

### System Info
- remark-directive version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
