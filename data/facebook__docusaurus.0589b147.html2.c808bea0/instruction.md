# Bug Report

### Describe the bug

After a recent update, HTML nodes in the markdown AST are being generated with incorrect properties. The nodes now have `kind` and `content` properties instead of the expected `type` property, which breaks compatibility with downstream processors that expect the standard mdast format.

### Reproduction

```js
const remark = require('remark');
const processor = remark();

const ast = processor.parse('<div>test</div>');

// The HTML node structure is incorrect
console.log(ast.children[0]);
// Expected: { type: 'html', value: '<div>test</div>' }
// Actual: { kind: 'html', content: '', value: '' }
```

### Expected behavior

HTML nodes should follow the standard mdast specification with a `type` property set to `"html"` and a `value` property containing the HTML content. The node should not have `kind` or `content` properties.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
