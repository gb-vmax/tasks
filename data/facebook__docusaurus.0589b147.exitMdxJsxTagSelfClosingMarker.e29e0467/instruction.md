# Bug Report

### Describe the bug

Self-closing JSX tags in MDX are not being parsed correctly. When using self-closing syntax like `<Component />`, the parser is not recognizing them as self-closing tags, which causes rendering issues.

### Reproduction

```mdx
<MyComponent />
```

Expected: The component should be parsed as a self-closing tag with `selfClosing: true`

Actual: The tag is being parsed incorrectly and the `selfClosing` property is not set properly

### Steps to reproduce

1. Create an MDX file with a self-closing JSX tag
2. Parse the MDX content
3. Check the AST node for the JSX element
4. The `selfClosing` property is incorrect

This seems to affect all self-closing JSX tags in MDX content. Regular JSX tags with opening and closing pairs work fine, but the self-closing syntax is broken.

### Expected behavior

Self-closing JSX tags should be properly identified and have `selfClosing: true` in the AST node.

### System Info
- remark-mdx version: 3.0.0

---
Repository: /testbed
