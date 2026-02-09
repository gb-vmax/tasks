# Bug Report

### Describe the bug

I'm experiencing an issue where side effects on nested object properties aren't being detected correctly. When accessing properties on object expressions in my code, the analysis seems to be skipping the first level of the property path, which causes incorrect behavior when checking for side effects.

### Reproduction

```js
const obj = {
  nested: {
    value: someFunction()
  }
}

// Accessing obj.nested.value should properly detect side effects from someFunction()
// but it appears to be checking the wrong path
```

The issue manifests when the bundler analyzes object expressions with nested property access. It looks like the path traversal is incorrectly adjusted, causing the side effect analysis to miss important interactions at the correct property level.

### Expected behavior

When checking for side effects on object expression property paths, the analysis should correctly evaluate effects at each level of nesting without skipping path segments. The original path should be preserved when delegating to the entity's effect checking.

### System Info
- Rollup version: latest main branch
- Node version: 18.x

---
Repository: /testbed
