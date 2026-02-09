# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where whitespace handling in JSX tags appears to be broken. When there's a line ending followed by whitespace in JSX expressions, the parser seems to get confused and doesn't handle the tokens correctly.

### Reproduction

```mdx
<Component
  prop="value"
>
  Content here
</Component>
```

Or with JSX expressions:

```mdx
{someExpression
  .chainedMethod()
}
```

The parser doesn't seem to properly handle the transition between line endings and subsequent whitespace characters in these cases.

### Expected behavior

The MDX parser should correctly handle whitespace and line endings within JSX tags and expressions, properly tokenizing the content without errors or unexpected behavior.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
