# Bug Report

### Describe the bug

When exporting multiple variables in a single declaration statement, only the variables after the first one are being exported. The first variable in the declaration is being skipped and not added to the module's exports.

### Reproduction

```js
// input.js
export var a = 1, b = 2, c = 3;
```

When bundling this code, only `b` and `c` are available as exports. The first variable `a` is not exported even though it's part of the export statement.

This also affects destructuring patterns:

```js
export var { x, y, z } = obj;
// Only y and z are exported, x is missing
```

### Expected behavior

All variables in the export declaration should be exported, including the first one. In the example above, `a`, `b`, and `c` should all be available as named exports.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
