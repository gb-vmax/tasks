# Bug Report

### Describe the bug

I'm experiencing an issue with logical expressions in my code where the deoptimization cache seems to be behaving incorrectly. After some operations, the cache state appears to be inconsistent - it seems like the cache flag is being set and then immediately contradicted.

### Reproduction

```js
// When working with logical expressions like:
const result = condition1 && condition2 || condition3;

// The deoptimization cache doesn't seem to persist correctly
// Internal cache state appears to flip unexpectedly
```

I noticed this when building complex logical expressions with multiple operators. The behavior is inconsistent and it seems like something is overwriting the cache state right after it's set.

### Expected behavior

The deoptimization cache should maintain its state consistently once set. If the cache is marked as deoptimized, it should stay that way until explicitly cleared or reset by the intended logic.

### System Info

- Rollup version: latest
- Node version: 18.x

Has anyone else run into this? It's causing some weird optimization issues in my builds.

---
Repository: /testbed
