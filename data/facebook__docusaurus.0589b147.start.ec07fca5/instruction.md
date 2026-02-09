# Bug Report

### Describe the bug

Setext headings (underlined headings using `=` or `-`) are not being parsed correctly. The parser seems to be treating them as regular paragraphs instead of recognizing them as headings.

### Reproduction

```markdown
This is a heading
=================

Another heading
---------------
```

When parsing the above markdown, the text should be recognized as setext headings (h1 and h2 respectively), but instead they're being parsed as regular paragraph text followed by horizontal rules or just plain text.

### Expected behavior

The parser should correctly identify setext-style headings and convert them to the appropriate heading elements. The first example should be treated as an h1 heading, and the second as an h2 heading.

### Additional context

This seems to have broken recently. Previously these heading styles were working fine, but now they're not being detected at all.

---
Repository: /testbed
