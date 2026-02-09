# Bug Report

### Describe the bug

When using self-closing JSX tags in MDX content, the closing marker is not being properly set on the tag object. The tag's `close` property remains undefined even after processing self-closing tags like `<Component />`.

### Reproduction

```jsx
// MDX content with self-closing tag
<MyComponent />

// After parsing, the tag object doesn't have close property set correctly
// Expected: tag.close === true
// Actual: tag.close === undefined
```

The issue appears to affect any self-closing JSX syntax in MDX documents. Regular closing tags with explicit closing markers (e.g., `<Component></Component>`) might work, but the shorthand self-closing syntax doesn't properly mark the tag as closed.

### Expected behavior

Self-closing JSX tags should have their `close` property set to `true` after parsing, allowing proper handling of the tag structure downstream.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
