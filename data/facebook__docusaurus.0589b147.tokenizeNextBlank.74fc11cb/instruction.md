# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where blank lines after certain elements are not being handled correctly. It seems like the parser is consuming line endings in the wrong order, which causes unexpected behavior when processing content with blank lines.

### Reproduction

```mdx
# Heading

Some text here

<Component />

More text after blank line
```

When parsing MDX content like above, the blank lines between elements aren't being recognized properly. The parser seems to be exiting the "lineEndingBlank" state before actually consuming the code, which leads to incorrect parsing results.

### Expected behavior

Blank lines should be properly tokenized and the parser should correctly handle transitions between different content blocks. The line ending should be consumed before exiting the blank line state.

### Additional context

This appears to affect MDX documents that rely on blank lines for proper separation between markdown elements and JSX components. The issue manifests when there are multiple blank lines or when blank lines appear in specific positions within the document.

---
Repository: /testbed
