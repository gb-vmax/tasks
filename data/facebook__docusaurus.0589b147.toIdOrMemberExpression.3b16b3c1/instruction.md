# Bug Report

### Describe the bug

I'm encountering an issue with member expression generation when using dot notation with object properties. The `computed` property seems to be set incorrectly, causing bracket notation to be used when it shouldn't be (and vice versa).

### Reproduction

```js
// When building a member expression from identifiers
const ids = ['obj', 'property', 'nested'];
const result = toIdOrMemberExpression(ids);

// Expected: obj.property.nested
// Actual: obj['property']['nested'] (or similar incorrect behavior)
```

The problem appears when constructing member expressions from an array of identifiers. The logic for determining whether to use bracket notation (`computed: true`) vs dot notation (`computed: false`) seems inverted.

### Expected behavior

When all identifiers are valid JavaScript property names, the generated member expression should use dot notation (e.g., `obj.property.nested`). Bracket notation should only be used when the property name is not a valid identifier or is a literal value.

### Additional context

This affects MDX compilation where nested object access is converted to AST nodes. The incorrect `computed` flag causes the generated JavaScript to use the wrong property access syntax.

---
Repository: /testbed
