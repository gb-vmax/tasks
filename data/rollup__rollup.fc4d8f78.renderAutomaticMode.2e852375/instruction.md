# Bug Report

### Describe the bug

When using JSX with automatic runtime mode and a single child element, the generated code is incorrect. The child is being wrapped in an array bracket `[` when it shouldn't be, and conversely, multiple children are not being wrapped properly.

### Reproduction

```jsx
// Single child case - incorrectly adds opening bracket
<div>
  <span>Hello</span>
</div>

// Expected output: children: <span>...</span>
// Actual output: children: [<span>...</span>
```

The logic appears to be inverted - single children are getting the array bracket while multiple children are not.

### Expected behavior

- Single child elements should NOT be wrapped in an array
- Multiple children SHOULD be wrapped in an array with both opening and closing brackets

### System Info
- Rollup version: latest
- JSX transform: automatic mode

---
Repository: /testbed
