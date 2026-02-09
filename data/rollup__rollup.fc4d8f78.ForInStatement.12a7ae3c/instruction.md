# Bug Report

### Describe the bug

I'm encountering an issue with `for...in` loops where the loop variable assignment is not being included correctly during tree-shaking. When `includeChildrenRecursively` is `false`, the left-hand side (loop variable) is still being fully included as if `includeChildrenRecursively` was `true`.

### Reproduction

```js
// Input code with for...in loop
for (const key in obj) {
  // Some code that should be tree-shaken
}
```

When bundling with tree-shaking enabled and `includeChildrenRecursively` set to `false`, the loop variable declaration is incorrectly included in the output bundle even when it shouldn't be.

### Expected behavior

The loop variable assignment should respect the `includeChildrenRecursively` parameter. When `includeChildrenRecursively` is `false`, it should not force full inclusion of the left-hand side assignment target.

Currently it seems like the left side is always being included recursively regardless of the `includeChildrenRecursively` value passed to the `include` method.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
