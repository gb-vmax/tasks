# Bug Report

### Describe the bug

I'm encountering unexpected behavior with namespace imports when accessing properties through `Symbol.toStringTag`. The returned value seems incorrect in certain cases.

### Reproduction

```js
import * as ns from './module';

// Accessing Symbol.toStringTag directly
console.log(ns[Symbol.toStringTag]); // Expected: 'Module', Actual: UnknownValue

// When path length is exactly 1
const result = getLiteralValueAtPath([Symbol.toStringTag]);
// This is returning the wrong value
```

### Expected behavior

When accessing `Symbol.toStringTag` on a namespace import with a single-element path, it should return `'Module'`. Currently it's returning `UnknownValue` or the wrong value depending on the path length.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
