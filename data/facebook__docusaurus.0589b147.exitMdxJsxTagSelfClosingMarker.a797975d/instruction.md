# Bug Report

### Describe the bug

Self-closing JSX tags in MDX are not being recognized correctly. When I use self-closing syntax like `<Component />`, the component is being treated as if it's not self-closing, which causes rendering issues.

### Reproduction

```jsx
// This MDX content doesn't work as expected
<MyComponent />

// The component is treated as non-self-closing
// Expected: { selfClosing: true }
// Actual: { selfClosing: false }
```

When parsing MDX with self-closing tags, the parser incorrectly marks them as non-self-closing tags. This affects how the components are processed and rendered.

### Expected behavior

Self-closing JSX tags should be properly identified with `selfClosing: true` so they render correctly without requiring a closing tag.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
