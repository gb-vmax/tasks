# Bug Report

### Describe the bug

I'm experiencing an issue with tree-shaking in for-loops. Code that should be removed during the build process is being kept, and conversely, code that should be retained is being removed. This is causing unexpected behavior in the bundled output.

### Reproduction

```js
// This for-loop should be tree-shaken but isn't
for (let i = 0; i < 10; i++) {
  // side-effect free code
  const unused = i * 2;
}

// This for-loop should be kept but is being removed
for (let i = 0; i < arr.length; i++) {
  console.log(arr[i]); // has side effects
}
```

The first loop contains no side effects and should be removed during optimization, but it appears in the final bundle. The second loop has clear side effects (console.log) but gets incorrectly tree-shaken away.

### Expected behavior

For-statements with side effects in the init, test, update, or body should be retained in the bundle. For-statements without any side effects should be removed during tree-shaking.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started happening recently. Any ideas what might be causing this?

---
Repository: /testbed
