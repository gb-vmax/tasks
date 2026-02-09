# Bug Report

### JSX automatic runtime using wrong factory function for single children

I'm encountering an issue with JSX transformation in automatic mode where single child elements are being transformed incorrectly.

### Reproduction

When I have a JSX element with a single child, it seems to be using the wrong factory function:

```jsx
// Single child element
<div>
  <span>Hello</span>
</div>
```

The transformation appears to be using `jsxs` (multiple children factory) even when there's only one child element, when it should be using `jsx` (single child factory).

### Expected behavior

- Elements with a single child should use the `jsx` factory function
- Elements with multiple children should use the `jsxs` factory function

This is causing issues with runtime behavior since the factory functions expect different argument structures.

### System Info
- JSX mode: automatic
- Using jsxImportSource configuration

---
Repository: /testbed
