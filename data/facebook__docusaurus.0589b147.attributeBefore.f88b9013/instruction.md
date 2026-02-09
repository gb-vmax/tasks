# Bug Report

### Describe the bug

Self-closing JSX tags are not being parsed correctly in MDX. When using a self-closing tag with the `/` marker, the parser seems to fail or produce unexpected behavior.

### Reproduction

```jsx
<MyComponent />
```

When trying to parse MDX content with self-closing tags like the above, the parser doesn't handle them properly. The issue appears to be related to how the self-closing marker is processed.

### Expected behavior

Self-closing JSX tags should be parsed correctly and the MDX content should render without issues. The `/` marker should be recognized as a valid self-closing indicator.

### Additional context

This seems to have started happening recently. Regular opening/closing tag pairs like `<MyComponent></MyComponent>` work fine, but the self-closing syntax doesn't.

---
Repository: /testbed
