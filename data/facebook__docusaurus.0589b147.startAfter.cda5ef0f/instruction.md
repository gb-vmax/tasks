# Bug Report

### Describe the bug

I'm encountering an issue with MDX tag parsing where tags followed by whitespace or line endings are not being parsed correctly. It seems like the parser is rejecting valid MDX syntax that should be accepted.

### Reproduction

```mdx
<Component 
  prop="value"
/>
```

When I try to parse MDX content with tags that have whitespace after the opening `<`, the parser fails or behaves unexpectedly. This affects both self-closing and regular JSX tags in MDX files.

### Expected behavior

The parser should correctly handle tags with whitespace/line endings after the opening bracket. This is valid JSX/MDX syntax and should be processed without issues.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
