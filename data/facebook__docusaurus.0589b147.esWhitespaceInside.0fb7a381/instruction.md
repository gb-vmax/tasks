# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where whitespace handling in JSX tags seems to be broken. When I have JSX expressions with whitespace, the parser enters an infinite loop or doesn't properly exit the whitespace state.

### Reproduction

```mdx
<Component
  prop={
    value
  }
/>
```

When parsing JSX tags with whitespace inside expressions, the parser gets stuck and doesn't properly handle the whitespace tokens. This seems to happen specifically when there are spaces or line breaks within JSX attribute expressions.

### Expected behavior

The parser should properly consume and exit whitespace tokens in JSX expressions without getting stuck in an infinite recursion. Whitespace inside JSX tags should be handled gracefully and the document should parse successfully.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This is blocking our ability to format MDX files with prettier since the parser hangs on properly formatted JSX.

---
Repository: /testbed
