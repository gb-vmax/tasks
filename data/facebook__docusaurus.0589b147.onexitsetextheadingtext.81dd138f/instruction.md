# Bug Report

### Describe the bug

I'm encountering an issue with setext-style headings (underlined headings) in markdown parsing. When parsing markdown with setext headings, the line ending handling appears to be broken. The heading text is not being processed correctly when there are line endings involved.

### Reproduction

```markdown
Heading text
============

Some paragraph after the heading.
```

When parsing this markdown, the heading and subsequent content don't render as expected. It seems like the line ending after the heading text is not being handled properly, which affects how the rest of the document is parsed.

### Expected behavior

Setext-style headings should be parsed correctly with proper line ending handling. The heading should be recognized as a separate block element, and the content following it should be parsed independently.

Example of what should work:
```markdown
Level 1 Heading
===============

Level 2 Heading
---------------
```

Both heading styles should parse correctly and maintain proper separation from surrounding content.

### Additional context

This seems to affect specifically setext headings (those using `=` or `-` underlines), while ATX-style headings (using `#`) work fine. The issue appears to be related to how line endings are tracked during the parsing process.

---
Repository: /testbed
