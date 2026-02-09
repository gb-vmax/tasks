# Bug Report

### Describe the bug

I'm encountering an issue with setext heading parsing in markdown. When I have a paragraph followed by underline characters (`=` or `-`), the parser is not correctly recognizing them as setext headings in certain cases.

### Reproduction

```markdown
This is a paragraph
===================

Another paragraph
-----------------
```

When parsing the above markdown, the setext headings are not being properly detected. The underlines should convert the preceding paragraphs into headings (h1 for `=` and h2 for `-`), but they're being treated as regular text or ignored.

### Expected behavior

The parser should recognize setext-style headings where a line of `=` characters creates an H1 heading and a line of `-` characters creates an H2 heading from the preceding paragraph text.

Expected output:
- "This is a paragraph" should be rendered as an H1 heading
- "Another paragraph" should be rendered as an H2 heading

### Additional context

This seems to affect the tokenization logic for setext underlines. The issue appears when the parser is checking for valid setext heading patterns in the event stream.

---
Repository: /testbed
