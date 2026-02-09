# Bug Report

### Describe the bug

I'm encountering an issue with markdown line ending detection in the remark-directive parser. It seems like certain line endings are not being recognized correctly, which causes parsing to fail or behave unexpectedly for directives that span multiple lines.

### Reproduction

When parsing markdown with directives that have line breaks, the parser doesn't correctly identify line endings. This affects both container and leaf directives.

```markdown
:::note
This is a note
with multiple lines
:::
```

The directive content isn't being parsed properly when there are newlines involved. It appears that the line ending detection logic is not working as expected.

### Expected behavior

The parser should correctly identify markdown line endings (newlines, carriage returns, etc.) and properly parse directives that span multiple lines. Line breaks within directive content should be handled correctly.

### Additional context

This seems to be related to how character codes are being checked for line endings. The issue manifests when processing directives with multi-line content or when directives are separated by newlines.

---
Repository: /testbed
