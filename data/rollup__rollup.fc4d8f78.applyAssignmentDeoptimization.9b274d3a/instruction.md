# Bug Report

### Describe the bug

I'm encountering an issue where member expression assignments are not being properly tree-shaken in certain cases. It seems like the deoptimization logic isn't working correctly, causing code that should be removed during tree-shaking to be retained in the final bundle.

### Reproduction

```js
// Example code that demonstrates the issue
const obj = {};

// This assignment should trigger proper deoptimization
obj.property = value;

// When the property has side effects, the tree-shaking behavior
// appears inconsistent
```

The problem occurs specifically when:
1. A member expression is assigned a value
2. The property has read side effects enabled
3. The member is bound but not a variable and not undefined

In these cases, the deoptimization doesn't seem to happen at the right time, leading to incorrect tree-shaking results.

### Expected behavior

Member expression assignments should be properly deoptimized before the assignment state is marked as complete, ensuring that tree-shaking correctly handles properties with side effects.

### System Info
- Rollup version: latest
- Node version: 18.x

Has anyone else run into this? It's causing some unexpected code to remain in production builds.

---
Repository: /testbed
