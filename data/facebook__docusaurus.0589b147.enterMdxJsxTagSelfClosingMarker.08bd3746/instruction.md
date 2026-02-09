# Bug Report

### Describe the bug

Self-closing JSX tags in MDX are not being validated correctly. When I use a self-closing tag with the `/` syntax, it's throwing an error even though the syntax is valid.

### Reproduction

```mdx
<MyComponent />
```

This throws an error:
```
Unexpected self-closing slash `/` in closing tag, expected the end of the tag
```

But this is a valid self-closing tag syntax and should be allowed.

### Expected behavior

Self-closing tags like `<MyComponent />` should be parsed without errors. The error message should only appear when there's an actual issue like trying to use `</MyComponent />` (a closing tag with a self-closing slash).

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
