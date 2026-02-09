# Bug Report

### Describe the bug

I'm encountering an issue with footnote definition parsing in markdown. When processing footnotes, the marker token structure appears to be incorrect, causing the content type to be set on the wrong token level.

### Reproduction

```markdown
Here's some text with a footnote reference[^1].

[^1]: This is the footnote content.
```

When parsing this markdown with footnote definitions, the token tree structure for the footnote definition label is not being built correctly. The `contentType` property seems to be applied at an unexpected level in the token hierarchy.

### Expected behavior

The footnote definition should be parsed with the correct token structure where:
1. The marker token (`^`) is properly entered and exited
2. The label string container is created with the appropriate content type
3. The chunk string token is nested correctly within the label string

Instead, it appears the token exit for the marker is missing and the content type assignment happens on a different token than intended.

### System Info
- Using remark-gfm 4.0.0
- This affects footnote definition parsing specifically

---
Repository: /testbed
