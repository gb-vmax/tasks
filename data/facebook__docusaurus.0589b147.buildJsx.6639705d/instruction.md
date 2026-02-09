# Bug Report

### Describe the bug

After a recent update, JSX children are being rendered in reverse order. Elements that should appear first are now appearing last, and vice versa.

### Reproduction

```jsx
<div>
  <span>First</span>
  <span>Second</span>
  <span>Third</span>
</div>
```

Expected output:
```
First Second Third
```

Actual output:
```
Third Second First
```

This affects all JSX elements with multiple children, including:
- Regular elements with multiple child nodes
- Text nodes mixed with element nodes
- Expression containers alongside other children

### Expected behavior

Children should be rendered in the order they are written in the source code. The first child should appear first, not last.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
