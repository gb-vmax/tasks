# Bug Report

### Describe the bug
When using JSX spread attributes with `jsx.mode: 'preserve'`, the spread syntax is being incorrectly removed from the output. The `{...props}` notation is stripped out even though the preserve mode should keep the JSX syntax intact.

### Reproduction
```jsx
// Input JSX
const Component = (props) => <div {...props} />;

// With jsx.mode: 'preserve'
// Expected output: <div {...props} />
// Actual output: <div  />
```

The spread attribute braces and dots are being removed when they should be preserved.

### Expected behavior
When `jsx.mode` is set to `'preserve'`, the JSX spread attributes should remain unchanged in the output, maintaining the original `{...expression}` syntax.

### Additional context
This appears to affect any JSX element using spread attributes when the preserve mode is enabled. Other JSX modes seem to work as expected, but preserve mode is stripping the spread syntax incorrectly.

---
Repository: /testbed
