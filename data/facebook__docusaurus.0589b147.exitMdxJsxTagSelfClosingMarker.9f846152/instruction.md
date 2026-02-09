# Bug Report

### Describe the bug

Self-closing JSX tags in MDX are not being parsed correctly. When using self-closing syntax like `<Component />`, the parser is not recognizing them as self-closing tags.

### Reproduction

```mdx
<MyComponent />
```

When parsing the above MDX content, the component is not being treated as self-closing even though it uses the `/>` syntax.

### Expected behavior

Self-closing JSX tags should be properly identified and have their `selfClosing` property set to `true`. Components written with the self-closing syntax `<Component />` should be parsed as self-closing elements.

### Additional context

This affects any MDX content that uses self-closing JSX syntax. The parser seems to be incorrectly handling the self-closing marker, which could lead to rendering issues or incorrect AST generation.

---
Repository: /testbed
