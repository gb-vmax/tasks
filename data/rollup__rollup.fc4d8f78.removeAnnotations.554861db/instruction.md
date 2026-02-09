# Bug Report

### Describe the bug

When using sequence expressions (comma operator) in the code, annotations are being removed from the wrong expression. The annotations should be removed from the last expression in the sequence, but they're currently being removed from the first one instead.

### Reproduction

```js
/* @__PURE__ */ foo(), /* @__PURE__ */ bar(), baz()
```

When processing this sequence expression, the annotation removal is targeting the first expression (`foo()`) instead of the last one (`baz()`). This causes incorrect behavior when tree-shaking or optimizing code with pure annotations.

### Expected behavior

The `removeAnnotations` method should process the last expression in the sequence (the one that actually represents the value of the entire sequence expression), not the first one.

### Additional context

This affects code that uses the comma operator with multiple annotated expressions. The last expression in a sequence is what determines the final value, so that's where annotation handling should be focused.

---
Repository: /testbed
