# Bug Report

### Describe the bug

I'm experiencing an issue with JSX expression containers that contain literal whitespace values. It seems like the whitespace handling logic is inverted - elements that should be filtered out are being kept, and elements that should be kept are being filtered out.

### Reproduction

```jsx
const component = (
  <div>
    {' '}
    <span>Content</span>
    {'  '}
  </div>
)
```

When rendering components with JSX expression containers containing whitespace literals (like `{' '}` or `{'  '}`), these whitespace expressions are being incorrectly processed. The behavior appears to be backwards from what's expected.

### Expected behavior

JSX expression containers with whitespace-only literal values should be handled consistently with how whitespace is normally processed in JSX. Non-whitespace literal expressions should be preserved in the output.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
