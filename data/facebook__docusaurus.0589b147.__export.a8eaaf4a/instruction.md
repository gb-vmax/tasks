# Bug Report

### Describe the bug

After a recent update, exported properties from MDX modules are no longer enumerable and appear to be static values instead of getters. This breaks code that relies on iterating over module exports or expects lazy evaluation of exported values.

### Reproduction

```js
// Example MDX module
import * as mdxModule from './example.mdx'

// Try to enumerate exports
console.log(Object.keys(mdxModule)) // Returns empty array or missing expected keys

// Or when iterating over exports
for (const key in mdxModule) {
  console.log(key) // Nothing is logged
}
```

When trying to access exports programmatically or iterate over them, the properties are not visible even though they exist and can be accessed directly.

### Expected behavior

Module exports should be enumerable so they can be discovered via `Object.keys()`, `for...in` loops, or similar enumeration methods. This was working in previous versions.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
