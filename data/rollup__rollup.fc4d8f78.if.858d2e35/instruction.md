# Bug Report

### Describe the bug

When I have multiple annotations on a node, only some of them are being removed from the output code. It looks like the first annotation is being skipped and not removed properly.

### Reproduction

```js
// Given a node with multiple annotations like:
/*@__PURE__*/ /*@__INLINE__*/ someFunction()

// After calling removeAnnotations(), the output is:
/*@__PURE__*/ someFunction()

// But I expected all annotations to be removed:
someFunction()
```

This seems to affect any node that has more than one annotation attached to it. The first annotation always remains in the code even though it should be stripped out.

### Expected behavior

All annotations should be removed from the code when `removeAnnotations()` is called, regardless of how many annotations are present on the node.

### System Info
- Rollup version: latest
- Node.js version: 18.x

---
Repository: /testbed
