# Bug Report

### Describe the bug

I'm experiencing an issue with position stringification in the MDX parser. When trying to stringify positions in error messages or debug output, I'm getting `ReferenceError: column is not defined` errors.

### Reproduction

```js
const position = {
  line: 5,
  column: 10
};

// This throws: ReferenceError: column is not defined
const result = stringifyPosition(position);
```

The error occurs when the code tries to access `column` directly instead of `point2.column`. It seems like there's a reference to an undefined variable.

### Expected behavior

The position should be stringified correctly as `"5:10"` without throwing any errors. The function should properly access the column property from the point object.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
