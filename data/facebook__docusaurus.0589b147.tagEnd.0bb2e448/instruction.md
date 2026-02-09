# Bug Report

### Describe the bug

I'm experiencing an issue with JSX tag parsing where the closing `>` marker seems to be causing unexpected behavior. When parsing JSX elements in MDX files, the tag structure appears to be malformed internally.

### Reproduction

```jsx
<Component>
  content
</Component>
```

When processing JSX tags like the above, the internal state tracking for tag markers seems incorrect. The closing `>` character of tags doesn't get properly registered, leading to potential parsing errors or malformed AST nodes.

### Expected behavior

JSX tags should be parsed correctly with proper enter/exit events for all tag markers. The closing `>` should be properly tracked in the token stream.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

This seems to affect all JSX elements in MDX documents. Any help would be appreciated!

---
Repository: /testbed
