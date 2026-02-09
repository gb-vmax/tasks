# Bug Report

### Describe the bug

I'm encountering an issue where annotations are not being removed correctly from the code. After removing annotations, there seems to be leftover characters in the output that should have been stripped away.

### Reproduction

```js
// Given a node with annotations like:
/* @__PURE__ */ someFunction()

// After calling removeAnnotations(), the output still contains extra characters
// Expected: someFunction()
// Actual: someFunction()  (with trailing character from annotation)
```

The problem appears when processing nodes that have multiple annotations attached to them. The annotations are supposed to be completely removed from the generated code, but some trailing characters remain.

### Expected behavior

When `removeAnnotations()` is called on a node, all annotation comments should be completely removed from the code without leaving any artifacts or extra characters behind.

### Additional context

This seems to affect tree-shaking annotations and other comment-based hints that need to be stripped during the build process. The issue becomes more noticeable when there are multiple annotations on the same node.

---
Repository: /testbed
