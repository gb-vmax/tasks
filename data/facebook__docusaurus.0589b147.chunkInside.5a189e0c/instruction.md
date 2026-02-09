# Bug Report

### Describe the bug

I'm experiencing an issue with MDX content parsing where line breaks in content blocks are not being handled correctly. It seems like the parser is terminating content chunks prematurely instead of continuing to process multi-line content.

### Reproduction

```mdx
# Example

This is a paragraph
that spans multiple lines
and should be treated as continuous content.

Another paragraph here.
```

When parsing the above MDX content, the parser appears to stop processing content after encountering line endings, rather than checking if the content continues on the next line. This results in incomplete or incorrectly parsed content blocks.

### Expected behavior

The parser should properly handle multi-line content by checking for continuation patterns when it encounters line endings. Content that spans multiple lines should be parsed as a single continuous block until an actual content boundary is reached.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
