# Bug Report

### Describe the bug

Footnote references with exactly 999 characters are being rejected when they should be valid. The parser incorrectly treats the 999-character limit as exclusive rather than inclusive.

### Reproduction

```markdown
[^footnote-with-999-chars]

[^footnote-with-999-chars]: This is a footnote with exactly 999 characters in the reference label...
```

When parsing markdown with a footnote reference that has exactly 999 characters, it fails to parse even though the GFM spec allows footnote labels up to and including 999 characters.

### Expected behavior

Footnote references with exactly 999 characters should be parsed successfully. Only references with 1000+ characters should be rejected.

### Additional context

This appears to be an off-by-one error in the length validation. References with 998 characters work fine, but 999 characters are incorrectly rejected.

---
Repository: /testbed
