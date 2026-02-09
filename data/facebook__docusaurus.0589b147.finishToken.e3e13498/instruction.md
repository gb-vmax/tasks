# Bug Report

### Describe the bug

I'm experiencing issues with MDX parsing where tokens are being positioned incorrectly. It seems like the token end positions are off by one character, which is causing parsing errors in certain edge cases.

### Reproduction

```mdx
{/* Example MDX content that triggers the issue */}
<Component prop={value} />
```

When parsing MDX content with JSX expressions, the parser seems to be calculating token boundaries incorrectly. This leads to unexpected behavior where the parser either skips characters or includes extra characters in tokens.

### Expected behavior

Token positions should accurately reflect the actual start and end positions of parsed tokens in the source text. The `end` position should point to the character immediately after the last character of the token.

### Additional context

This appears to affect the remark-mdx parser (version 3.0.0). The issue manifests when processing JSX expressions and may cause downstream problems with syntax highlighting, error reporting, or AST transformations that rely on accurate source positions.

---
Repository: /testbed
