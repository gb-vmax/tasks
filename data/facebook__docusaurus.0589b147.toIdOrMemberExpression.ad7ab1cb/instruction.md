# Bug Report

### Describe the bug

I'm experiencing an issue with member expression generation where the `computed` property is being set incorrectly. When converting identifiers to member expressions, the logic for determining whether bracket notation should be used appears to be inverted.

### Reproduction

```js
// When converting a chain of identifiers like ['foo', 'bar']
// to a member expression, the computed property is backwards

const ids = ['foo', 'bar'];
const result = toIdOrMemberExpression(ids);

// Expected: foo.bar (computed: false for Identifier)
// Actual: foo['bar'] (computed: true for Identifier)
```

The issue seems to affect how property access is generated - identifiers are being treated as if they need bracket notation when they should use dot notation, and vice versa.

### Expected behavior

- When the property is an `Identifier`, `computed` should be `false` (use dot notation: `obj.prop`)
- When the property is a `Literal`, `computed` should be `true` (use bracket notation: `obj['prop']`)

Currently it's doing the opposite of what it should.

### System Info

- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
