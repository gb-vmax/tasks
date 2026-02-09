# Bug Report

### Describe the bug

I'm encountering an issue with JSX member expression handling where property access is being computed incorrectly. When using JSX elements with member expressions, the `computed` property is being set to the opposite of what it should be, causing incorrect property access patterns.

### Reproduction

```jsx
// Example JSX with member expression
<Component.SubComponent />

// Or with dynamic property access
<obj[prop] />
```

The member expression object is being generated with inverted `computed` values - literal properties are marked as computed and identifier properties are marked as non-computed. This affects how the JSX is transformed and can lead to runtime errors or unexpected behavior.

Additionally, when converting JSX names to identifiers, valid identifier names are being treated as literals and vice versa, which breaks the expected transformation.

### Expected behavior

- Member expressions with literal properties (like `obj["prop"]`) should have `computed: true`
- Member expressions with identifier properties (like `obj.prop`) should have `computed: false`
- Valid identifier names should be converted to `Identifier` nodes, not `Literal` nodes
- Invalid identifier names should be converted to `Literal` nodes

### System Info

- MDX version: 3.0.0
- Using JSX transformation pipeline

---
Repository: /testbed
