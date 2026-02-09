# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where content after certain constructs is not being processed correctly. It seems like the parser is terminating early or skipping content when it encounters specific patterns.

### Reproduction

```mdx
# Heading

Some content here

More content that should be parsed
```

When parsing the above MDX, the content after the initial construct is not being recognized. The parser appears to be handling null/non-null checks incorrectly, causing it to exit prematurely or continue when it shouldn't.

### Expected behavior

The parser should correctly process all content in the MDX file, including content that comes after headings and other constructs. Line endings should be properly consumed and the parser should continue to the next construct.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
