# Bug Report

### Describe the bug

I'm encountering an infinite loop issue when parsing MDX content that contains certain whitespace patterns in JSX expressions. The parser seems to get stuck and never completes, causing the process to hang indefinitely.

### Reproduction

```jsx
<Component
  prop={
    value
  }
/>
```

When trying to parse MDX content with JSX tags that have whitespace inside attribute expressions (like spaces or tabs between the braces and the value), the parser enters an infinite loop and never returns.

This also happens with similar patterns:
```jsx
<div className={ "test" } />
```

### Expected behavior

The parser should handle whitespace inside JSX attribute expressions correctly and complete the parsing without hanging. Whitespace should be consumed and the parser should move forward to the next token.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
