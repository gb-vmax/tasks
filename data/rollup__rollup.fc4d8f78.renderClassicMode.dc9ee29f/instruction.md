# Bug Report

### Describe the bug

Self-closing JSX elements are not being rendered correctly. When I use a self-closing JSX tag like `<Component />`, the output is malformed and includes an extra closing parenthesis instead of properly closing the element.

### Reproduction

```jsx
// Input JSX
const element = <MyComponent prop="value" />;

// Expected output
React.createElement(MyComponent, { prop: "value" })

// Actual output
React.createElement(MyComponent, { prop: "value" }))
```

The same issue occurs with any self-closing element:

```jsx
<div className="test" />
<img src="image.png" />
<input type="text" />
```

All of these produce output with an extra closing parenthesis at the end.

### Expected behavior

Self-closing JSX elements should be transformed into proper `createElement` calls without extra parentheses. Non-self-closing elements with opening and closing tags work fine, but self-closing syntax is broken.

### System Info
- Rollup version: Latest
- Node version: 18.x

---
Repository: /testbed
