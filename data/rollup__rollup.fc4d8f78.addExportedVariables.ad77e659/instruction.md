# Bug Report

### Describe the bug

I've encountered an issue with array destructuring patterns where the code fails to parse/compile correctly. It seems like something is broken in how array patterns are being processed.

### Reproduction

```js
// This causes an error during compilation
const [first, second, ...rest] = someArray;

// Also fails with nested destructuring
const [a, [b, c]] = nestedArray;

// And with default values
const [x = 1, y = 2] = values;
```

The compilation process breaks and the bundler throws an error when trying to process files with array destructuring patterns.

### Expected behavior

Array destructuring should work correctly and the code should compile without errors. This is standard JavaScript syntax and was working fine before.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started happening recently. Any help would be appreciated!

---
Repository: /testbed
