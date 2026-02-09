# Bug Report

### Describe the bug

I'm encountering an issue with ATX heading parsing where headings without whitespace after the `#` symbols are not being parsed correctly. The content of the heading is not being extracted properly when there's no space between the heading markers and the text.

### Reproduction

```markdown
#Heading without space
##Another heading
###Third level
```

When parsing these headings, the heading text content is not being resolved correctly. It seems like the parser is expecting whitespace after the `#` symbols and fails to handle cases where the whitespace is missing.

### Expected behavior

The parser should handle headings both with and without whitespace after the `#` markers:
- `# Heading` (with space) - should work
- `#Heading` (without space) - should also work and extract "Heading" as the content

Both formats are commonly used in markdown files and should be supported.

### Additional context

This appears to affect the heading resolution logic specifically. The issue manifests when trying to extract the actual text content from ATX-style headings.

---
Repository: /testbed
