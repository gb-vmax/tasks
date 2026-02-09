# Bug Report

### Describe the bug

I'm experiencing an issue with JSX member expressions when using namespaced components. The component hierarchy seems to be inverted or not properly constructed when dealing with nested member expressions.

### Reproduction

```js
// When trying to use a namespaced component like:
<Components.UI.Button />

// The resulting JSX member expression appears to be incorrectly structured
// Expected: Components.UI.Button
// Actual: The nesting order is wrong
```

This affects any component that uses dot notation for namespacing. The deeper the nesting, the more obvious the problem becomes.

### Expected behavior

JSX member expressions should properly nest from left to right. For example, `A.B.C` should create a structure where `A` is the root object, `B` is a property of `A`, and `C` is a property of `B`.

### Additional context

This seems to have started happening recently. Components with simple names (no dots) work fine, but anything with namespacing breaks. The issue is subtle and might not be caught by simple test cases.

---
Repository: /testbed
