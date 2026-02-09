# Bug Report

### Describe the bug

I'm experiencing an issue with footnote back-references in MDX. When a footnote is referenced multiple times in the document, the last back-reference link is missing from the footnote section at the bottom of the page.

### Reproduction

```mdx
Here is some text with a footnote[^1].

More text with the same footnote again[^1].

And one more reference to it[^1].

[^1]: This is the footnote content.
```

When rendering this MDX content, the footnote at the bottom should have three back-reference links (to jump back to each place where `[^1]` appears), but only two are being generated.

### Expected behavior

All footnote references in the document should have corresponding back-reference links in the footnote section. If a footnote is referenced 3 times, there should be 3 back-reference links.

### Additional context

This seems to affect documents where footnotes are referenced multiple times. Single-use footnotes appear to work correctly. The issue is specifically with the back-reference count/links generation.

---
Repository: /testbed
