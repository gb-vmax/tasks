# Bug Report

### Describe the bug

I'm experiencing an issue with setext-style headings in markdown parsing. The heading levels appear to be inverted - headings that should be level 1 (using `=` underlines) are being parsed as level 2, and headings that should be level 2 (using `-` underlines) are being parsed as level 1.

### Reproduction

```markdown
This should be H1
=================

This should be H2
-----------------
```

When parsing the above markdown:
- The first heading (with `=` underline) is incorrectly parsed as depth 2 instead of depth 1
- The second heading (with `-` underline) is incorrectly parsed as depth 1 instead of depth 2

### Expected behavior

According to markdown spec:
- Headings underlined with `=` should be level 1 (depth 1)
- Headings underlined with `-` should be level 2 (depth 2)

The parser should correctly assign depth values based on the underline character used.

### Additional context

This seems to have started recently. The heading levels are completely reversed from what they should be, which breaks any documentation or content that relies on proper heading hierarchy.

---
Repository: /testbed
