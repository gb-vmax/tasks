# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where certain container structures are not being properly closed/exited. This seems to affect nested containers or specific edge cases where the offset boundaries are exactly at line start positions.

### Reproduction

```mdx
> Blockquote content
> that spans multiple lines
> and ends at a specific position

Next paragraph
```

When parsing MDX content with containers (like blockquotes, lists, etc.) that have boundaries exactly at line start offsets, the container exit logic doesn't behave as expected. The issue appears to be related to how the parser handles token boundaries during document initialization.

### Expected behavior

Containers should be properly closed regardless of whether their end offset is exactly at or just past the line start offset. The parser should correctly identify when a token needs to be processed based on its position relative to the current parsing context.

### Additional context

This seems to happen specifically when:
- A token's end offset is exactly at the line start offset (boundary case)
- Multiple containers are nested and need to be exited in sequence

The parsing logic appears to be too strict in some boundary conditions, causing containers to remain open when they should be closed.

---
Repository: /testbed
