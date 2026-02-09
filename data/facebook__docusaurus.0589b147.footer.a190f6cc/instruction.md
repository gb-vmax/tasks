# Bug Report

### Describe the bug

I'm encountering an issue with footnote back-references in MDX. When a footnote is referenced multiple times in a document, the back-reference links are not being generated correctly. It seems like the first reference is being skipped.

### Reproduction

```mdx
Here's some text with a footnote[^1] and another reference to the same footnote[^1].

[^1]: This is the footnote content.
```

When rendered, the footnote should have back-reference links to both occurrences in the text, but only the second reference gets a back-reference link. The first reference is missing from the footnote's back-reference list.

### Expected behavior

The footnote should include back-reference links for ALL references in the document. If a footnote is referenced twice, there should be two back-reference links in the footnote itself (typically shown as ↩ symbols or similar).

### Additional context

This appears to be related to how the `rereferenceIndex` is being initialized and incremented when building the back-references array. The loop seems to be starting from the wrong index.

---
Repository: /testbed
