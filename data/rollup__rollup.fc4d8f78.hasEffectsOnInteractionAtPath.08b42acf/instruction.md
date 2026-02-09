# Bug Report

### Describe the bug

I'm experiencing an issue where template literals are being incorrectly tree-shaken from the bundle. When accessing properties on template literal expressions, they're being removed during the build process even though they have side effects.

### Reproduction

```js
// This gets removed from the bundle when it shouldn't
const result = `hello ${world}`.toLowerCase();

// Also affected:
const str = `${foo} ${bar}`;
const prop = str.someProperty;
```

The template literal expressions are being treated as if they have no effects when their properties are accessed, causing them to be eliminated during dead code elimination.

### Expected behavior

Template literals should be retained in the bundle when their properties are accessed or their methods are called, as these operations can have observable effects.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
