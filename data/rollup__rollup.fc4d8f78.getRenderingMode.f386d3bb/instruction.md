# Bug Report

### Describe the bug

When using JSX in automatic mode, single-child JSX elements are being rendered with the wrong factory function. Elements with exactly one child are incorrectly using `jsx` instead of `jsxs`.

### Reproduction

```jsx
// This JSX element has one child
const element = <div>Hello</div>;

// Expected: Should use 'jsxs' factory
// Actual: Uses 'jsx' factory instead
```

The issue occurs specifically when:
- JSX mode is set to 'automatic'
- The element has exactly 1 rendered child

### Expected behavior

JSX elements with one or more children should use the `jsxs` factory function. Only elements with zero children should use the `jsx` factory.

According to the React JSX transform specification, `jsxs` should be used for elements with static children (1 or more), while `jsx` is for elements without children or with dynamic children.

### System Info
- Rollup version: latest
- JSX mode: automatic

---
Repository: /testbed
