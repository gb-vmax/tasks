# Bug Report

### Describe the bug

I'm encountering an issue with footnote back-references in MDX documents. When a footnote is referenced multiple times in the document, the generated back-reference links in the footer are incorrect - it seems like one back-reference is missing.

### Reproduction

```mdx
Here is some text with a footnote[^1] and another reference to the same footnote[^1].

[^1]: This is the footnote content.
```

When this is rendered, the footnote in the footer should have back-reference links to both locations where it's referenced in the document. However, only one back-reference link appears instead of two.

### Expected behavior

The footnote footer should include back-reference links for all instances where the footnote is referenced in the document. If a footnote is referenced twice, there should be two back-reference links in the footer.

### Additional context

This appears to affect any footnote that's referenced more than once. The first reference seems to be missing from the back-references list in the generated output.

---
Repository: /testbed
