# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where the parser seems to be accessing the wrong context in the context stack. This is causing incorrect parsing behavior, particularly around brace handling and block detection.

### Reproduction

When parsing MDX content with nested structures, the parser appears to be looking at the wrong element in the context stack. This affects how braces are interpreted - whether they're treated as block delimiters or object literals.

Example MDX content that triggers the issue:
```mdx
export const config = {
  nested: {
    value: true
  }
}

# Heading

Some content here
```

The parser seems to be checking the wrong context level when determining if a brace should be treated as a block, which can lead to syntax errors or incorrect parsing of valid MDX.

### Expected behavior

The parser should correctly identify the current context from the context stack (the most recent/last element) when making decisions about how to parse braces and other syntax elements.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

This appears to be a regression as the same MDX files were parsing correctly in earlier versions.

---
Repository: /testbed
