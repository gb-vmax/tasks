# Bug Report

### Describe the bug

Footnote references are not being numbered correctly when the same footnote is referenced multiple times in a document. The counter seems to be using the wrong value for subsequent references to the same footnote ID.

### Reproduction

```mdx
Here is some text with a footnote[^1].

More content here with another reference to the same footnote[^1].

And yet another reference[^1].

[^1]: This is the footnote content.
```

When rendering this, the footnote reference numbers don't match what you'd expect. Instead of all references to `[^1]` pointing to the same footnote number, they seem to be getting different counter values.

### Expected behavior

All references to the same footnote ID should use the same footnote number. For example, if `[^1]` is the first footnote defined, all instances of `[^1]` in the document should be numbered as footnote 1, not incrementing with each reference.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
