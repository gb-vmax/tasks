# Bug Report

### Describe the bug

I'm encountering an issue with footnote rendering in MDX where the back-reference links are not being generated correctly. When a footnote is referenced multiple times in a document, the last reference doesn't get a proper back-link in the footnote section.

### Reproduction

```mdx
Here is some text with a footnote[^1].

More text with the same footnote[^1].

And even more text with the same footnote[^1].

[^1]: This is the footnote text.
```

When this is rendered, the footnote at the bottom should have three back-reference links (one for each usage), but only two are being generated. The third reference is missing its back-link.

### Expected behavior

All footnote references in the document should have corresponding back-links in the footnote section at the bottom of the page. If a footnote is used 3 times, there should be 3 back-reference links.

### Additional context

This seems to affect any footnote that's referenced more than once. The pattern is consistent - it's always the last reference that doesn't get its back-link generated.

---
Repository: /testbed
