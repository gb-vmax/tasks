# Bug Report

### Describe the bug

I'm experiencing an issue where MDX content that doesn't start with JSX elements (like plain text or markdown) is not being rendered in the output. The generated AST seems to be missing the content when the root node is not a JSX fragment or element.

### Reproduction

```mdx
This is plain text content.

Some **markdown** here.
```

When processing this MDX content, the output appears to be empty or missing the actual content. It seems like only content that starts with JSX elements gets properly included in the final result.

### Expected behavior

All MDX content should be rendered, regardless of whether it starts with JSX elements or plain markdown/text. The content should be wrapped in a JSX fragment if necessary and included in the output.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
