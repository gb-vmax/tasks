# Bug Report

### Describe the bug

I'm encountering an issue with GFM (GitHub Flavored Markdown) link reference definitions where duplicate identifiers are being added to the internal tracking array. When the same reference label is defined multiple times in a document, all instances are being stored instead of just unique ones.

### Reproduction

```markdown
[foo]: https://example.com
[foo]: https://duplicate.com
[bar]: https://test.com
```

When parsing this markdown, the `defined` array ends up containing duplicate entries for `foo`, which shouldn't happen since reference definitions should only track unique identifiers.

### Expected behavior

The parser should only store unique identifiers in the `defined` array. If a reference label is already defined, it shouldn't be added again. This is important for proper reference resolution and memory efficiency when processing documents with many duplicate definitions.

### Additional context

This seems to affect how the parser tracks which link references have been defined in the document. The current behavior allows the same identifier to be pushed multiple times without checking if it already exists.

---
Repository: /testbed
