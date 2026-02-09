# Bug Report

### Describe the bug

I'm experiencing an issue with annotation removal in the code generation process. When multiple annotations are present on a node, they're not being removed correctly from the output, leaving extra characters or malformed code.

### Reproduction

```js
// Given a node with multiple annotations like:
/* @__PURE__ */ /* @__NO_SIDE_EFFECTS__ */ function foo() {}

// After processing, the output has unexpected characters or incomplete removal
```

The issue seems to occur specifically when there are multiple consecutive annotations. Single annotations appear to work fine, but with multiple ones the generated code ends up with stray characters or partial annotation text remaining.

### Expected behavior

All annotations should be cleanly removed from the generated code without leaving any extra characters or partial text behind. The output should be:

```js
function foo() {}
```

### System Info
- Rollup version: latest
- Node version: 18.x

Has anyone else run into this? It's causing issues with our minified builds.

---
Repository: /testbed
