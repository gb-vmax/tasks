# Bug Report

### Describe the bug

I'm encountering an issue with dynamic imports where the `options` parameter seems to be incorrectly handled during the inclusion phase. When using dynamic imports with certain configurations, the path inclusion behavior appears inverted from what's expected.

### Reproduction

```js
// When shouldIncludeDynamicAttributes is true
import('./module.js')

// The UNKNOWN_PATH should be included via options?.includePath()
// but it's not being called as expected
```

The problem manifests when:
1. Creating a dynamic import expression
2. The import has `shouldIncludeDynamicAttributes` set to true
3. The `includePath` method should be invoked with `UNKNOWN_PATH`

### Expected behavior

When `shouldIncludeDynamicAttributes` is true, the `options?.includePath(UNKNOWN_PATH, context)` should be called during the node inclusion. Currently it seems like the logic might be inverted - the path is only included when `shouldIncludeDynamicAttributes` is false, which doesn't make sense for the intended behavior.

### System Info
- Rollup version: latest
- Node version: 18.x

This is affecting builds where dynamic imports need to track their attributes properly. Any insights would be appreciated!

---
Repository: /testbed
