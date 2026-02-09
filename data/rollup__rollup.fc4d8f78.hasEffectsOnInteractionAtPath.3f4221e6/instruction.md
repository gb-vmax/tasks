# Bug Report

### Describe the bug

I'm experiencing an issue with object expressions where side effects are not being properly detected when accessing nested properties. It seems like the analysis is incorrectly reporting that certain operations have no side effects when they actually do.

### Reproduction

```js
const obj = {
  nested: {
    prop: getValue()
  }
}

// Accessing obj.nested.prop should be detected as having potential side effects
// but it's being treated as side-effect free
```

When the bundler analyzes code with nested property accesses on object literals, it's not correctly tracking whether those accesses might have side effects. This can lead to incorrect tree-shaking where code that should be kept gets removed.

### Expected behavior

The bundler should properly detect and preserve side effects for nested property accesses on object expressions. If a nested property might have side effects (like calling a function), the access should be marked as having effects.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started happening recently. Let me know if you need more details to reproduce!

---
Repository: /testbed
