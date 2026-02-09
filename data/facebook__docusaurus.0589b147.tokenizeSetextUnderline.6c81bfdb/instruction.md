# Bug Report

### Describe the bug

I'm encountering an issue with setext heading parsing in markdown. When I try to use setext-style headings (underlined with `=` or `-`), they're not being recognized correctly. The parser seems to be treating them as regular paragraphs instead of headings.

### Reproduction

```markdown
This is a heading
=================

This should be an h2
--------------------
```

When parsing the above markdown, the headings are not being converted properly. They just show up as plain text followed by lines of equals signs or dashes.

I tried with both single-line and multi-line content above the underline, but neither works as expected.

### Expected behavior

The parser should recognize setext-style headings and convert them to proper heading elements:
- Lines underlined with `===` should become h1 headings
- Lines underlined with `---` should become h2 headings

This is standard markdown syntax and was working in previous versions.

### Additional context

This seems to have broken recently. Regular ATX-style headings (with `#`) still work fine, but setext headings are completely broken now.

---
Repository: /testbed
