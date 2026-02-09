# Bug Report

### Describe the bug

I'm experiencing an issue with JSX parsing in MDX content. It seems like JSX elements are being treated incorrectly depending on whether they appear in flow content vs text content. Specifically, JSX that should work in regular flow context is being parsed as if it's inline text, and vice versa.

### Reproduction

When I try to use JSX components in my MDX files, they're not being parsed correctly:

```mdx
# My Document

<MyComponent>
  This should be block-level JSX
</MyComponent>

Some paragraph with <InlineComponent /> inside it.
```

The block-level component gets treated as inline text, and the inline component gets treated as block-level flow content. This causes rendering issues and unexpected behavior.

### Expected behavior

- JSX elements in flow context (block-level) should be parsed as flow content
- JSX elements in text context (inline) should be parsed as text content
- The parser should correctly distinguish between these two contexts

### System Info

- @mdx-js/mdx version: 3.0.0
- Node version: 20.x

This seems to have broken recently - the same MDX files were working fine before. Any help would be appreciated!

---
Repository: /testbed
