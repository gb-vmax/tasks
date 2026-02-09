# Bug Report

### Describe the bug

I'm experiencing incorrect token positioning when parsing MDX content. It appears that tokens are being created with invalid end positions, which causes the parser to fail or produce incorrect results when processing certain MDX syntax.

### Reproduction

When parsing MDX content with various token types, the token positions seem to be wrong. For example:

```js
// Parsing simple MDX content
const mdxContent = `
# Hello

<Component prop="value" />
`;

// The parser creates tokens with incorrect end positions
// Expected: token.end should be at the actual end of the token
// Actual: token.end equals token.start, making the token have zero length
```

This causes issues when trying to extract source code ranges or when other tools rely on accurate token positions for syntax highlighting, error reporting, or code transformation.

### Expected behavior

Tokens should have correct `start` and `end` positions that accurately reflect their actual position in the source code. The `end` position should point to the character after the last character of the token, not to the same position as `start`.

### Additional context

This seems to affect all token types being parsed. The issue makes it impossible to accurately map tokens back to their source positions, which breaks features that depend on this information.

---
Repository: /testbed
