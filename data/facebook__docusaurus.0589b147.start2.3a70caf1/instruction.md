# Bug Report

### Describe the bug

I'm experiencing an issue with whitespace handling in MDX parsing. It appears that spaces are no longer being recognized or processed correctly, which is causing unexpected behavior in my MDX documents.

### Reproduction

```mdx
# Hello World

This is a paragraph with    multiple spaces.

Another paragraph here.
```

When parsing this MDX content, the spacing between elements and within text doesn't seem to be handled properly. The parser appears to be skipping or mishandling whitespace characters where they should be processed.

### Expected behavior

Whitespace and spaces should be properly recognized and processed according to the markdown specification. The parser should correctly identify space characters and handle them appropriately when building the syntax tree.

### Additional context

This seems to have started happening recently. The spacing behavior was working fine before, but now documents that previously parsed correctly are showing issues with whitespace handling.

---
Repository: /testbed
