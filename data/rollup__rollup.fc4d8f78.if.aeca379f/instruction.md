# Bug Report

### Describe the bug

I'm encountering an issue with circular re-exports in my module. When I have a module that re-exports everything from another module using `export * from`, and that creates a circular dependency, the re-exports are not being resolved correctly on subsequent calls.

### Reproduction

```js
// moduleA.js
export * from './moduleB.js'
export const a = 1

// moduleB.js
export * from './moduleA.js'
export const b = 2

// main.js
import * as A from './moduleA.js'
// First access works fine
console.log(A)
// But subsequent module resolution doesn't return the expected re-exports
```

The problem seems to be that when `getReexports()` is called multiple times in a circular re-export scenario, it returns an empty array instead of the actual re-exports after the first call.

### Expected behavior

The `getReexports()` method should consistently return the same re-exports on every call, even in circular re-export scenarios. An empty array that was set to prevent infinite recursion should not be cached and returned as the final result.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
