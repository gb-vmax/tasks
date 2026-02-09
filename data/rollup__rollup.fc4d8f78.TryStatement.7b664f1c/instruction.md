# Bug Report

### Describe the bug

I'm encountering an issue with tree-shaking behavior in try-catch-finally blocks. It appears that the finalizer (finally block) is being incorrectly evaluated for side effects instead of the catch handler. This causes code that should be removed during tree-shaking to be retained, or vice versa.

### Reproduction

```js
try {
  // some code
} catch (error) {
  console.log(error); // This has side effects but might not be detected
} finally {
  // empty finally block
}
```

In this case, the catch block contains code with side effects (console.log), but the tree-shaking logic seems to be checking the finally block instead. This results in unexpected behavior where code is either incorrectly removed or incorrectly retained during the build process.

### Expected behavior

The tree-shaking should correctly detect side effects in the catch handler (not the finalizer) and make appropriate decisions about whether to include or remove the try-catch block.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
