# Bug Report

### Describe the bug

I'm experiencing an issue with nested curly braces in MDX expressions. When using multiple levels of braces (like objects inside JSX expressions), the parser seems to close the expression prematurely or incorrectly handle the brace matching.

### Reproduction

```mdx
{
  {
    nested: 'value'
  }
}
```

The expression gets terminated at the wrong closing brace, causing parsing errors or unexpected behavior. It seems like the brace counting logic is inverted - opening braces are being counted as closing and vice versa.

### Expected behavior

Nested braces should be properly balanced and the expression should only close when all opening braces have matching closing braces. The parser should correctly track the nesting level and only exit the expression context when the outermost closing brace is encountered.

### System Info
- remark-mdx version: 3.0.0

---
Repository: /testbed
