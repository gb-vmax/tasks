# Bug Report

### Describe the bug

I'm encountering an issue with setext heading parsing where the underline characters are not being recognized correctly. It appears that setext headings (using `=` or `-` underlines) are no longer working as expected.

### Reproduction

```markdown
This is a heading
=================

Another heading
---------------
```

When parsing the above markdown, the setext headings are not being detected properly. The underline sequence seems to be consuming incorrect characters.

### Expected behavior

The parser should correctly identify setext headings by:
1. Matching the underline marker character (`=` or `-`)
2. Consuming all consecutive instances of that marker
3. Properly exiting the sequence when a different character is encountered

The headings should be parsed as valid setext headings with the text on the first line becoming the heading content.

### Additional context

This seems to affect both `=` (level 1) and `-` (level 2) setext headings. The tokenizer appears to be processing the underline sequence incorrectly, which prevents proper heading detection.

---
Repository: /testbed
