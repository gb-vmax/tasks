# Bug Report

### Describe the bug

When using JSX automatic runtime mode with single child elements, the children are incorrectly being wrapped in an array bracket. This causes the output to have malformed syntax where single children get `children: [` prepended instead of `children: `.

### Reproduction

```jsx
// Input JSX
<div>Single child text</div>

// Expected output (automatic mode)
jsx('div', { children: 'Single child text' })

// Actual output
jsx('div', { children: ['Single child text' })
```

The issue occurs specifically when:
1. Using JSX automatic runtime mode
2. Element has a single child (not multiple children)
3. The child rendering logic incorrectly adds opening bracket for single children

### Expected behavior

Single children should not be wrapped in array brackets. Only multiple children should be wrapped in `[...]`. The current behavior has the logic inverted - it's adding brackets when `hasMultipleChildren` is false instead of when it's true.

### System Info
- Rollup version: latest
- JSX mode: automatic runtime

---
Repository: /testbed
