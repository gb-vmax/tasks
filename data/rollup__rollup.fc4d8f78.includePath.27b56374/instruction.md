# Bug Report

### Describe the bug

I'm experiencing an issue with deeply nested property access in object paths. When accessing properties beyond a certain depth level, the bundler seems to be tracking the wrong properties or losing track of nested paths entirely.

### Reproduction

```js
const obj = {
  level1: {
    level2: {
      level3: {
        level4: {
          level5: {
            value: 'test'
          }
        }
      }
    }
  }
}

// Accessing deeply nested properties
const result = obj.level1.level2.level3.level4.level5.value
```

When the nesting goes beyond a certain depth, the property tracking appears to behave incorrectly. It seems like the path resolution is either:
1. Including properties at the wrong depth level
2. Slicing the path incorrectly when it exceeds the maximum depth

### Expected behavior

Deeply nested property access should be tracked correctly regardless of depth, with proper handling when the maximum path depth is reached. The bundler should maintain accurate property paths for tree-shaking and side-effect analysis.

### System Info

- Rollup version: latest
- Node version: 18.x

This might be related to how object paths are being constructed when dealing with member expressions that exceed the maximum tracking depth.

---
Repository: /testbed
