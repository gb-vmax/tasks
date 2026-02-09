# Bug Report

### Describe the bug

I'm experiencing an issue with object member path resolution in nested object interactions. When accessing deeply nested properties through object members, the path order seems to be incorrect, causing side effects to be evaluated in the wrong order.

### Reproduction

```js
const obj = {
  a: {
    b: {
      c: someFunction()
    }
  }
}

// Accessing obj.a.b.c
// The path resolution appears to be reversed when checking for side effects
```

When the bundler analyzes nested object member accesses, it's not correctly tracking the interaction path. This leads to incorrect side effect analysis for deeply nested property accesses.

### Expected behavior

The path should be resolved in the correct order when checking for side effects on nested object member interactions. The interaction context should properly reflect the full path from the root object to the target property.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
