# Bug Report

### Describe the bug

I'm encountering an issue with setext-style heading parsing in markdown. When processing setext headings (headings underlined with `=` or `-`), the parser seems to be handling the underline sequence incorrectly, causing the heading to not be recognized properly.

### Reproduction

```markdown
This is a heading
=================

Another heading
---------------
```

When parsing this markdown, the setext headings are not being tokenized correctly. The underline characters should be consumed as a continuous sequence, but it appears the tokenization is breaking early or not maintaining the proper state.

### Expected behavior

Setext-style headings should be properly recognized and parsed. The underline sequence (multiple `=` or `-` characters) should be treated as a single heading indicator, and the text above it should be converted to the appropriate heading level (h1 for `=`, h2 for `-`).

### Additional context

This appears to be related to how the `setextHeadingLineSequence` token is being entered and exited during the tokenization process. The sequence of effects seems off when consuming multiple underline characters.

---
Repository: /testbed
