# Bug Report

### Describe the bug

I'm encountering an issue with link reference definitions in GFM (GitHub Flavored Markdown). When I define the same link reference multiple times in a document, all definitions are being added to the list instead of only keeping the first one. This causes incorrect behavior when resolving link references.

### Reproduction

```markdown
[foo]: https://example.com
[foo]: https://different.com

[foo]
```

In the above example, both definitions for `[foo]` are being tracked, when according to the CommonMark spec, only the first definition should be used and subsequent ones should be ignored.

### Expected behavior

When a link reference is defined multiple times, only the first definition should be stored and used. Subsequent definitions with the same identifier should be ignored, not added to the definitions list.

### Additional context

This affects how links are resolved in the final output. The current behavior doesn't match the expected GFM/CommonMark specification for handling duplicate link reference definitions.

---
Repository: /testbed
