# Bug Report

### Describe the bug

I'm encountering an issue with self-closing JSX tags in MDX content. When using self-closing tags like `<Component />`, they're being incorrectly parsed and the closing behavior isn't working as expected.

### Reproduction

```jsx
// MDX content with self-closing tag
<MyComponent />

// The tag is not being recognized as properly closed
```

When I parse MDX content that contains self-closing JSX tags, the parser doesn't correctly identify them as closed tags. This causes downstream issues when the AST is processed.

### Expected behavior

Self-closing JSX tags should be properly marked as closed in the AST. The `close` property should be set to `true` for tags that use the self-closing syntax (`/>`).

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest LTS

Has anyone else run into this? It seems like the closing marker detection might not be working correctly.

---
Repository: /testbed
