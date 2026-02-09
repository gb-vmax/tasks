# Bug Report

### Describe the bug

I'm experiencing an issue with MDX definitions and footnotes where identifiers are not being properly registered. It seems like definitions and footnotes with unique identifiers are not being stored correctly, causing them to be unavailable when referenced later in the document.

### Reproduction

```mdx
[link]: https://example.com "Example"
[another-link]: https://example.org "Another Example"

This is a [link] and this is [another-link].
```

When processing this MDX content, the definitions don't seem to be registered properly. The references remain unresolved even though the definitions are clearly present in the document.

Same issue occurs with footnotes:

```mdx
Here's a footnote reference[^1] and another one[^2].

[^1]: First footnote
[^2]: Second footnote
```

### Expected behavior

All definitions and footnotes should be properly registered and available for reference throughout the document. Each unique identifier should be stored in the internal map so that references can be resolved correctly.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have broken recently. Previously all my definition links and footnotes were working fine.

---
Repository: /testbed
