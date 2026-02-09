# Bug Report

### Describe the bug

Footnote references are generating incorrect href links. When using footnotes in MDX documents, the generated anchor links don't point to the correct footnote definitions, causing broken navigation.

### Reproduction

```mdx
Here is some text with a footnote[^1].

And another reference to the same footnote[^1].

[^1]: This is the footnote content.
```

When rendered, clicking on the footnote reference links doesn't jump to the footnote definition at the bottom of the page. The href attribute seems to be pointing to the wrong ID.

### Expected behavior

Clicking on a footnote reference (the superscript number) should scroll the page to the corresponding footnote definition. Multiple references to the same footnote should all link to the same definition, and the counter should increment correctly for the first occurrence vs. reused footnotes.

### Additional context

This appears to affect how footnote IDs and counters are being assigned. The first occurrence of a footnote should get one counter value, and subsequent reuses should get a different counter, but something seems reversed in the logic.

---
Repository: /testbed
