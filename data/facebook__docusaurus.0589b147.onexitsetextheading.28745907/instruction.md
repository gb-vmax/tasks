# Bug Report

### Describe the bug

I'm encountering an issue with setext heading parsing in MDX where the parser seems to be failing when processing certain heading formats. After a recent update, documents with setext-style headings (underlined with `=` or `-`) are not being parsed correctly.

### Reproduction

```mdx
My Heading
==========

Some content here.

Another Heading
---------------

More content.
```

When trying to parse this MDX content, the headings are not being recognized properly and the document structure appears broken.

### Expected behavior

Setext headings should be parsed correctly:
- Headings underlined with `=` should be treated as level 1 headings
- Headings underlined with `-` should be treated as level 2 headings
- The parser should properly exit the heading state and continue parsing subsequent content

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This appears to have started after a recent change to the heading parser. The issue seems related to how the parser handles the exit state for setext headings.

---
Repository: /testbed
