# Bug Report

### Describe the bug

When parsing MDX tags, whitespace after the opening tag marker is being incorrectly rejected. This causes valid MDX syntax with spaces or line breaks after the `<` character to fail parsing.

### Reproduction

```jsx
// This should be valid MDX but fails to parse
<
  Component
  prop="value"
/>

// Also fails
< Component />
```

The parser is rejecting these cases even though they should be valid according to MDX/JSX syntax rules where whitespace after the opening bracket is allowed.

### Expected behavior

MDX should allow whitespace (spaces, tabs, newlines) immediately after the opening `<` tag marker, similar to how JSX handles it. The parser should continue processing the tag name after consuming the whitespace rather than rejecting it outright.

### System Info
- remark-mdx version: 3.0.0

---
Repository: /testbed
