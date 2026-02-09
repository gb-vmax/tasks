# Bug Report

### Describe the bug

I'm experiencing an issue with JSX rendering where single-child elements are being treated incorrectly. When a JSX element has exactly one child, it seems to be using the wrong factory function in automatic mode, which causes rendering problems.

### Reproduction

```jsx
// This JSX element with a single child
const element = <div>Hello</div>;

// Gets transformed incorrectly - should use 'jsx' but uses 'jsxs' instead
```

The issue appears when:
1. Using JSX in automatic mode
2. Creating an element with exactly one child element
3. The factory function selection logic seems backwards

### Expected behavior

Elements with a single child should use the `jsx` factory function, while elements with multiple children should use `jsxs`. Currently it seems like the logic is inverted.

### Additional context

This affects JSX transpilation in automatic mode. The rendered output doesn't match what's expected for single-child vs multi-child elements.

---
Repository: /testbed
