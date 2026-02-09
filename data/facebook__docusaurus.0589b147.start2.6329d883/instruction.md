# Bug Report

### Describe the bug

I'm experiencing an issue with blank line parsing in MDX content. When there are spaces before a blank line, the parser seems to be handling them incorrectly, which causes unexpected behavior in the output.

### Reproduction

```mdx
Some content here

    
Another line after blank line with leading spaces
```

When parsing MDX content that has blank lines with leading whitespace (spaces or tabs), the tokenizer doesn't process them correctly. The `linePrefix` token appears to be applied in the wrong order or skipped entirely.

### Expected behavior

Blank lines with leading whitespace should be tokenized properly, with the `linePrefix` token correctly identifying and handling the spaces before the line ending. The parser should consistently handle both blank lines with and without leading whitespace.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have started happening recently. The blank line tokenizer logic might have a regression in how it handles the `factorySpace` call for line prefixes.

---
Repository: /testbed
