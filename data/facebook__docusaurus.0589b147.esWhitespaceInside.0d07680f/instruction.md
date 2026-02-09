# Bug Report

### Describe the bug

I'm encountering an issue with MDX JSX parsing where whitespace handling inside JSX tags appears to be broken. When there are spaces or other whitespace characters within JSX expressions, the parser seems to exit the whitespace state prematurely or in the wrong order, causing unexpected parsing behavior.

### Reproduction

```mdx
<Component
  prop={  value  }
/>
```

or

```mdx
<div>
  {  someExpression  }
</div>
```

When parsing MDX content with whitespace inside JSX expressions (between braces), the content is not being parsed correctly. The whitespace tokens seem to be getting mishandled.

### Expected behavior

The parser should correctly handle whitespace characters (including spaces and unicode whitespace) inside JSX expressions and exit the whitespace state at the appropriate time. The whitespace should be consumed before exiting the state, not after.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
