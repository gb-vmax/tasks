# Bug Report

### Describe the bug

I'm experiencing an issue with footnote back-references in MDX documents. When a footnote is referenced multiple times in the document, the generated back-reference links are incorrect.

### Reproduction

```mdx
Here is some text with a footnote[^1].

More text with the same footnote[^1].

Even more text with the same footnote[^1].

[^1]: This is the footnote content.
```

When this MDX is processed, the footnote at the bottom should have back-reference links to all three places where it's referenced in the document. However, the number of back-references generated doesn't match the actual number of references.

### Expected behavior

If a footnote is referenced 3 times in the document, there should be 3 back-reference links in the footnote section at the bottom. Each link should point back to the corresponding reference location in the main text.

### Additional context

This seems to affect documents where footnotes are reused multiple times. Single-use footnotes might work fine, but I haven't tested extensively.

---
Repository: /testbed
