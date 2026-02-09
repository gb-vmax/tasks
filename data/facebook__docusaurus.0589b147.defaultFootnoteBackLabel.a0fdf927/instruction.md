# Bug Report

### Describe the bug

I'm experiencing an issue with footnote back-references in MDX. When a footnote is referenced multiple times in a document, the "Back to reference" labels are not being generated correctly.

### Reproduction

```mdx
Here is some text with a footnote reference[^1].

And here is another reference to the same footnote[^1].

[^1]: This is the footnote content.
```

When rendering this MDX content, the back-reference links in the footnote should show:
- First reference: "Back to reference 1"
- Second reference: "Back to reference 1-2"

However, the second back-reference is showing "Back to reference 1" instead of "Back to reference 1-2".

### Expected behavior

When a footnote is referenced multiple times, each back-reference should have a unique label that includes the reference count. The first back-reference should just be "Back to reference N" and subsequent ones should be "Back to reference N-2", "Back to reference N-3", etc.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
