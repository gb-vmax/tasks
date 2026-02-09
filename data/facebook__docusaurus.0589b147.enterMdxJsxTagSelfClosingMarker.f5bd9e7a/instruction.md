# Bug Report

### Describe the bug

Self-closing JSX tags in MDX are not being validated correctly. The parser is allowing self-closing syntax on closing tags (e.g., `</Component />`) when it should throw an error.

### Reproduction

```mdx
<MyComponent>
  content here
</MyComponent />
```

The above MDX should fail to parse because `</MyComponent />` is invalid syntax - closing tags cannot have a self-closing slash. However, the parser is currently accepting this without raising an error.

### Expected behavior

The parser should throw a `VFileMessage` error with the message:
```
Unexpected self-closing slash `/` in closing tag, expected the end of the tag
```

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

This seems like a regression as the validation logic appears to be inverted - it's checking for the wrong condition before throwing the error.

---
Repository: /testbed
