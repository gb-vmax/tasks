# Bug Report

### Describe the bug

I'm encountering an issue with GFM (GitHub Flavored Markdown) footnote definition parsing where labels containing exactly 999 characters are being rejected when they should be accepted. The parser seems to be checking the length limit before incrementing the size counter, which causes valid 999-character labels to fail validation.

### Reproduction

```markdown
[^footnote]: This is a footnote with a very long label

Where the label is exactly 999 characters long - it gets rejected even though the GFM spec allows up to 999 characters.
```

Try parsing a footnote definition with a label that is exactly 999 characters in length. The parser will reject it as "too long" even though it's within the allowed limit.

### Expected behavior

Footnote definition labels with exactly 999 characters should be parsed successfully, as they are within the maximum allowed length according to the GFM specification. Only labels with 1000 or more characters should be rejected.

### Additional context

This appears to be related to the order of operations in the label parsing logic. The length validation is happening at the wrong point in the character processing flow.

---
Repository: /testbed
