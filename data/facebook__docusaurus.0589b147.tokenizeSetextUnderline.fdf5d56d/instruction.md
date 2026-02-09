# Bug Report

### Describe the bug
I'm encountering an issue with setext heading parsing in markdown. It seems like the parser is not correctly recognizing setext-style headings (headings underlined with `=` or `-` characters).

### Reproduction
```markdown
This is a heading
=================

Another heading
---------------
```

When I try to parse this markdown, the setext headings are not being recognized properly. The underlines aren't being matched to their corresponding text, and the headings aren't being converted as expected.

### Expected behavior
The parser should correctly identify setext-style headings where:
1. A line of text is followed by a line of `=` characters (for h1)
2. A line of text is followed by a line of `-` characters (for h2)

The underline characters should all match (all `=` or all `-`) and the heading should be properly parsed.

### Additional context
This appears to have started happening recently. The setext heading detection logic seems to be broken - either the underline matching isn't working correctly or the paragraph detection is failing.

---
Repository: /testbed
