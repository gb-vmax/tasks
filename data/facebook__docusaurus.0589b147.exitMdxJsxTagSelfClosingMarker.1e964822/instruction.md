# Bug Report

### Describe the bug

Self-closing JSX tags in MDX are not being parsed correctly. When using self-closing syntax (e.g., `<Component />`), the tags are being treated as non-self-closing, which breaks the expected behavior.

### Reproduction

```mdx
<MyComponent />
```

When parsing the above MDX content, the component is not recognized as self-closing even though it uses the `/>` syntax.

### Expected behavior

Self-closing JSX tags should be properly detected and the `selfClosing` property should be set to `true` when the tag uses the `/>` syntax.

### Additional context

This appears to affect all self-closing tags in MDX documents. The parser seems to be setting `selfClosing` to the wrong value during the exit phase of tag parsing.

---
Repository: /testbed
