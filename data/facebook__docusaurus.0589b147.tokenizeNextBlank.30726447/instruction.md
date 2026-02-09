# Bug Report

### Describe the bug

I'm experiencing an issue with blank line handling in MDX parsing. It seems like the parser is incorrectly identifying or processing blank lines in certain contexts, which is causing unexpected behavior when parsing MDX content.

### Reproduction

```js
const mdxContent = `
Some content here

Another line after blank
`;

// Parse the MDX content
const result = parseMDX(mdxContent);

// The blank line is not being handled correctly
// Expected the parser to recognize the blank line properly
// but it seems to be failing in the wrong direction
```

### Expected behavior

The parser should correctly identify and handle blank lines in MDX content. When there's a blank line between content blocks, it should be properly recognized and the parsing should succeed without issues.

### Additional context

This might be related to how the tokenizer processes line endings and blank lines. The issue appears to affect content that has blank lines separating different sections.

---
Repository: /testbed
