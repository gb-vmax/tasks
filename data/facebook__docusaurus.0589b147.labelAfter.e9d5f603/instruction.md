# Bug Report

### Describe the bug

I'm experiencing an issue with footnote definitions in GFM (GitHub Flavored Markdown) parsing. When the same footnote identifier is used multiple times in a document, all instances are being registered instead of only the first one. This causes duplicate footnote definitions to be treated as valid, which shouldn't be the case according to GFM spec.

### Reproduction

```markdown
[^1]: First definition
[^1]: Duplicate definition (should be ignored)

Some text with footnote reference[^1]
```

When parsing this markdown, both footnote definitions are being added to the `defined` array, but only the first occurrence should be recognized. Subsequent definitions with the same identifier should be ignored.

### Expected behavior

Only the first footnote definition with a given identifier should be registered. Any duplicate definitions should be treated as regular text or ignored during parsing.

### Additional context

This appears to affect how footnotes are rendered when there are multiple definitions with the same identifier in the source document. The parser should maintain a list of already-defined footnotes and skip any duplicates.

---
Repository: /testbed
