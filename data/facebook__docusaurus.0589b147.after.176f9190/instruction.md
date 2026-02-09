# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where whitespace handling after JSX flow tags appears to be incorrect. When there's no whitespace following a JSX tag in flow context, the parser seems to enter an infinite loop or behaves unexpectedly.

### Reproduction

```mdx
<Component/>Text immediately after with no space
```

Or:

```mdx
<div>
  content
</div>NextLine
```

When parsing MDX content where JSX flow tags are immediately followed by non-whitespace characters (no space between the closing tag and the next content), the parser doesn't handle it correctly.

### Expected behavior

The parser should correctly handle cases where JSX flow tags are followed immediately by non-whitespace content, either by properly parsing the subsequent content or providing a clear error message if this is invalid syntax.

Currently, it seems like the whitespace check logic is inverted - it's trying to consume whitespace when there isn't any, instead of moving on to the next token.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
