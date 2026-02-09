# Bug Report

### Describe the bug

I'm experiencing an issue where invalid annotations (like `@__PURE__` or `/* @__PURE__ */`) placed in incorrect positions are not being properly logged as warnings. The annotations are being removed from the output code, but the warning messages that should inform developers about these invalid placements are not appearing.

### Reproduction

```js
// Example code with invalid pure annotation
/* @__PURE__ */ 
const x = 5;

// Or with noSideEffects
/* @__NO_SIDE_EFFECTS__ */
function myFunc() {
  return 42;
}
```

When bundling code with invalid annotations like the above, the annotations get removed but no warning is logged to inform the user that these annotations were invalid.

### Expected behavior

When invalid `@__PURE__` or `@__NO_SIDE_EFFECTS__` annotations are encountered, the bundler should:
1. Remove the invalid annotations from the output
2. Log a warning message to inform the developer that the annotation was invalid and where it was found

Currently only step 1 is happening - the annotations are silently removed without any warning being shown.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
