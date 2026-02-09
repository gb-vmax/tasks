# Bug Report

### Describe the bug

JSX elements with self-closing tags are not rendering correctly. When I use a self-closing JSX element like `<Component />`, the output is malformed - it seems like the closing logic is inverted.

### Reproduction

```jsx
// Input JSX
const element = <MyComponent prop="value" />;

// Expected output (classic mode):
// React.createElement(MyComponent, { prop: "value" })

// Actual output:
// The closing parenthesis and logic appears to be wrong
```

Also happens with regular elements:

```jsx
const div = <div className="test">content</div>;
```

The self-closing vs non-self-closing element handling seems backwards.

### Expected behavior

- Self-closing elements like `<Component />` should render with proper closing parenthesis
- Elements with closing tags like `<div>...</div>` should properly render the closing element

### System Info
- Rollup version: latest
- JSX transform: classic mode

---
Repository: /testbed
