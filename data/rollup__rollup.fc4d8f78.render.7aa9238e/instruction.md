# Bug Report

### Describe the bug

When using JSX attributes with the `key` prop in automatic JSX mode, the attribute is being transformed incorrectly. The `key` attribute should be preserved as-is in automatic mode, but it's getting the colon syntax treatment (`: `) added to it.

### Reproduction

```jsx
// Input JSX
<div key="item-1">Content</div>

// In automatic JSX mode, the key attribute is being transformed when it shouldn't be
// Expected: key should remain as a special prop
// Actual: key is being treated like a regular attribute with colon syntax
```

### Expected behavior

In automatic JSX mode, the `key` attribute should be handled specially and not have the object property syntax applied to it. It should maintain its original form as `key` is a reserved prop in React's automatic runtime.

### Additional context

This appears to affect JSX transformation when using automatic JSX runtime mode. The `key` prop has special semantics and should be treated differently from regular attributes.

---
Repository: /testbed
