# Bug Report

### Describe the bug
I'm encountering an issue with automatic semicolon insertion (ASI) in MDX parsing. It seems like the parser is not correctly detecting when a semicolon can be inserted, particularly around closing braces.

### Reproduction
When parsing MDX content with JavaScript expressions that rely on automatic semicolon insertion, the parser fails to properly identify valid insertion points. This affects code blocks where line breaks should allow semicolon insertion.

For example:
```js
{
  const x = 1
}
// Should allow ASI here but doesn't work correctly
```

The issue appears to be related to how the parser checks for line breaks between tokens when determining if a semicolon can be automatically inserted.

### Expected behavior
The parser should correctly identify when automatic semicolon insertion is allowed based on:
1. End of file (EOF)
2. Closing brace with a line break
3. Line breaks between the last token end and current token start

Currently, it seems like the line break detection isn't working as expected in certain scenarios involving closing braces.

### System Info
- remark-mdx version: 3.0.0
- Parser: acorn-based

---
Repository: /testbed
