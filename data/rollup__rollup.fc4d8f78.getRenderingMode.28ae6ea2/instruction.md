# Bug Report

### Describe the bug

When using JSX in automatic mode, the factory function selection appears to be inverted. Elements with a single child are being rendered with `jsxs` (plural) while elements with multiple children are being rendered with `jsx` (singular). This is causing incorrect runtime behavior.

### Reproduction

```jsx
// Single child element - incorrectly uses jsxs
<div>
  <span>Hello</span>
</div>

// Multiple children - incorrectly uses jsx
<div>
  <span>Hello</span>
  <span>World</span>
</div>
```

When compiling with `jsx: 'automatic'`, the factory selection seems backwards. Single-child elements should use `jsx` but are getting `jsxs`, and multi-child elements should use `jsxs` but are getting `jsx`.

### Expected behavior

- Elements with 0 or 1 rendered children should use the `jsx` factory
- Elements with more than 1 rendered child should use the `jsxs` factory

This is causing issues at runtime since the wrong factory function is being called for the number of children present.

### System Info

- Rollup version: latest
- JSX mode: automatic

---
Repository: /testbed
