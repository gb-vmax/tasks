# Bug Report

### Describe the bug

I'm encountering an issue with footnote definitions in GFM (GitHub Flavored Markdown) where duplicate footnote identifiers are being added to the `defined` array. When a footnote definition is parsed, it seems like the identifier is being registered even when it already exists.

### Reproduction

```markdown
[^1]: First footnote
[^1]: Duplicate footnote with same identifier
```

When parsing this markdown, both footnote definitions with identifier `^1` get added to the internal tracking array, even though the second one should be ignored or handled differently since the identifier already exists.

### Expected behavior

The parser should check if a footnote identifier already exists before adding it to the `defined` array. Only the first occurrence should be registered, or duplicate identifiers should be handled appropriately to avoid conflicts.

### Additional context

This appears to affect how footnote definitions are tracked internally during parsing. The logic for checking whether an identifier has already been defined seems to be inverted or not working as intended.

---
Repository: /testbed
