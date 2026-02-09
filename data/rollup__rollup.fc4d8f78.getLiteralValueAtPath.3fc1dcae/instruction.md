# Bug Report

### Describe the bug

Template literals are not being correctly evaluated as literal values during the compilation process. When using a simple template literal without any expressions (e.g., `` `hello` ``), the compiler is not recognizing it as a static string value and instead treats it as an unknown value.

### Reproduction

```js
// This template literal should be recognized as a literal string
const str = `hello world`;

// The compiler should be able to optimize this during bundling
// but it's treating it as an unknown value instead
```

When bundling code that contains template literals without any interpolated expressions, the optimization step fails to recognize these as static values. This affects tree-shaking and other optimizations that rely on knowing literal values at compile time.

### Expected behavior

Template literals without any expressions (just plain strings wrapped in backticks) should be treated the same as regular string literals. The compiler should be able to extract their literal value for optimization purposes.

For example:
- `` `test` `` should be recognized as the literal string `"test"`
- `` `hello ${name}` `` can remain as unknown (since it has expressions)
- `` `static` `` should be optimized like `"static"`

### System Info
- Rollup version: latest
- Node version: 18.x

This seems like a regression as template literals were being handled correctly before. Any help would be appreciated!

---
Repository: /testbed
