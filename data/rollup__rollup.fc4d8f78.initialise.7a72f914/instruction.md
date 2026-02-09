# Bug Report

### Describe the bug

I'm experiencing an issue with `/*#__PURE__*/` annotations in my code. When I mark a function call as pure using the annotation comment, it seems like the tree-shaking behavior isn't working as expected. 

The problem appears to be related to how pure annotations are being detected - functions that should be tree-shaken away are still being included in the bundle, even when they're clearly marked as pure and their results aren't used.

### Reproduction

```js
// This function call should be tree-shaken away since it's marked pure
// and the result is not used
/*#__PURE__*/ sideEffectFreeFunction();

// Another example with multiple comments
/*#__PURE__*/
/* some other comment */
pureCall();
```

When I build with tree-shaking enabled, these calls are still appearing in the output bundle even though they're annotated as pure and their return values are unused.

### Expected behavior

Functions marked with `/*#__PURE__*/` annotations should be removed during tree-shaking when their results are not used, assuming tree-shaking annotations are enabled in the configuration.

### Additional context

This seems to have started happening recently. I have `treeshake.annotations` enabled in my rollup config. The pure annotation comments are definitely present in the source code, but they're not being respected during the build process.

---
Repository: /testbed
