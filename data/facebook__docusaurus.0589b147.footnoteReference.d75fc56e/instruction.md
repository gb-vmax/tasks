# Bug Report

### Describe the bug

I'm experiencing an issue with footnote references in MDX documents. The counter for footnote references appears to be off by one, and the ID generation for footnote reference links seems incorrect.

### Reproduction

When I create a document with multiple footnotes, the numbering doesn't match what I expect:

```markdown
Here's some text with a footnote[^1].

Another paragraph with another footnote[^2].

And a reused footnote[^1].

[^1]: First footnote
[^2]: Second footnote
```

The footnote reference counter is showing incorrect values, and when a footnote is referenced multiple times, the ID attributes for the anchor tags aren't being generated correctly. The first reference should not have a suffix, but currently it seems like it's getting one.

### Expected behavior

- Footnote counters should start at 1 and increment correctly
- When a footnote is referenced for the first time, the ID should be `fnref-{id}` without any suffix
- Only subsequent references to the same footnote should get a suffix like `fnref-{id}-2`, `fnref-{id}-3`, etc.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
