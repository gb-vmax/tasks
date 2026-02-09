# Bug Report

### Describe the bug

When using JSX with the automatic runtime mode, the output is incorrectly wrapping children in arrays. Single children are being wrapped in array brackets when they shouldn't be, and multiple children are not being wrapped when they should be.

### Reproduction

```jsx
// Single child - should NOT be wrapped in array
<div>
  <span>Hello</span>
</div>

// Multiple children - SHOULD be wrapped in array
<div>
  <span>First</span>
  <span>Second</span>
</div>
```

The generated output appears to have the wrapping logic inverted - single children get `[...]` brackets while multiple children don't.

### Expected behavior

- Single child elements should be passed directly without array wrapping
- Multiple child elements should be wrapped in an array

The automatic runtime mode should correctly differentiate between single and multiple children scenarios.

### System Info
- Rollup version: latest
- JSX preset: automatic

---
Repository: /testbed
