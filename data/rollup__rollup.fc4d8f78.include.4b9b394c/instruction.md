# Bug Report

### Describe the bug

I'm experiencing an issue with tree-shaking where member expressions are not being properly included in the output bundle. It seems like the object part of a member expression is sometimes being excluded from the bundle even when it should be included.

### Reproduction

```js
// input.js
const obj = {
  nested: {
    value: 42
  }
};

export const result = obj.nested.value;
```

When bundling this code, the `obj` variable and its nested structure are not being included correctly in the output. The bundle appears to be missing parts of the member expression chain.

### Expected behavior

The entire member expression chain (object, property access, nested property) should be included in the bundle when the final value is exported. All parts of `obj.nested.value` should be present in the output.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started happening recently. The bundled output is missing critical parts of the code that are actually needed at runtime.

---
Repository: /testbed
