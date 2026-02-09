# Bug Report

### Describe the bug

I'm experiencing an issue with footnote and definition handling in MDX documents. When I have multiple definitions or footnotes with the same identifier (case-insensitive), only the last one is being recognized instead of the first one. This seems like a regression as the expected behavior should be to use the first occurrence and ignore duplicates.

### Reproduction

```mdx
[link1][ref]
[link2][ref]

[ref]: https://first-definition.com
[ref]: https://second-definition.com
```

In this case, both links are resolving to `https://second-definition.com` when they should both resolve to `https://first-definition.com` (the first definition should take precedence).

The same issue occurs with footnotes:

```mdx
Some text[^1] and more text[^1]

[^1]: First footnote
[^1]: Second footnote
```

Both footnote references are showing "Second footnote" instead of "First footnote".

### Expected behavior

According to Markdown spec, when there are duplicate reference definitions, the first one should be used and subsequent ones with the same identifier should be ignored. The current behavior appears to be using the last definition instead of the first.

### Additional context

This might be related to how definitions are being stored in the internal map. It seems like duplicate identifiers are overwriting previous entries instead of being ignored.

---
Repository: /testbed
