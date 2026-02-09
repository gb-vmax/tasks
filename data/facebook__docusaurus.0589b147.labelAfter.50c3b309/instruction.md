# Bug Report

### Describe the bug

I'm encountering an issue with footnote definitions in GFM (GitHub Flavored Markdown) where duplicate footnote identifiers are being added to the `defined` array. When I use the same footnote reference multiple times in a document, it seems like the identifier gets registered multiple times instead of being skipped when it already exists.

### Reproduction

```markdown
Here's some text with a footnote[^1].

[^1]: First definition

More text with the same footnote[^1].

[^1]: Duplicate definition (should be ignored or handled differently)
```

When parsing this markdown, the identifier `^1` appears to be added to the internal `defined` array multiple times, which could cause issues with footnote resolution or rendering.

### Expected behavior

Duplicate footnote definitions should be handled properly - either by:
- Only registering the first occurrence of a footnote identifier
- Preventing duplicate identifiers from being added to the tracking array

The current behavior seems to allow the same identifier to be registered multiple times in the `defined` array.

### System Info
- remark-gfm version: 4.0.0
- Node version: Latest

---
Repository: /testbed
