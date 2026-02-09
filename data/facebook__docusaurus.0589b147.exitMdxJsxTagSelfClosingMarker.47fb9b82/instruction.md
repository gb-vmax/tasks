# Bug Report

### Describe the bug

Self-closing JSX tags in MDX are not being parsed correctly. When using self-closing syntax like `<Component />`, the parser doesn't properly set the `selfClosing` property, which causes the tag to be treated as a regular opening tag instead.

### Reproduction

```mdx
# My Document

<MyComponent />

Some text here
```

When parsing this MDX content, the `<MyComponent />` tag should be recognized as self-closing, but instead it's being parsed as if it were `<MyComponent>` (without the self-closing flag set).

### Expected behavior

Self-closing JSX tags should have their `selfClosing` property set to `true` in the AST. The parser should correctly identify the `/>` syntax and mark the tag appropriately.

### System Info
- remark-mdx version: 3.0.0

---
Repository: /testbed
