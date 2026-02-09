# Bug Report

### Describe the bug

I'm experiencing an issue with syntax extension merging where hooks are not being properly combined. When multiple extensions define the same hook, the resulting combined extension seems to have incorrect or missing properties.

### Reproduction

```js
const extension1 = {
  myHook: {
    code1: ['handler1']
  }
}

const extension2 = {
  myHook: {
    code2: ['handler2']
  }
}

const combined = combineExtensions([extension1, extension2])

// Expected: combined.myHook should have both code1 and code2
// Actual: Properties are missing or overwritten incorrectly
```

When combining extensions that share the same hook name but have different code points, the second extension's properties don't get merged correctly into the first one.

### Expected behavior

When combining multiple syntax extensions with overlapping hook names, all code points from both extensions should be preserved in the combined result. Each hook should contain the union of all code points defined across the extensions.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
