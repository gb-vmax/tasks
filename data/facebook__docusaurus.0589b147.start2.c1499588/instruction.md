# Bug Report

### Describe the bug

I'm encountering an issue with MDX link parsing where inactive label markers are being processed incorrectly. When using reference-style links in MDX content, links that should be inactive are being treated as active, causing unexpected rendering behavior.

### Reproduction

```mdx
[inactive link][ref]

Some other content here

[ref]: https://example.com
```

When the label start is marked as inactive (via `_inactive` flag), the link should not be processed, but it's currently being parsed and rendered as an active reference link instead.

### Expected behavior

Links with inactive label markers should be skipped during parsing and rendered as plain text rather than being processed as reference links. The `_inactive` flag on the label start should prevent the link from being tokenized.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This seems to have started happening recently and is affecting how reference-style links are being parsed in our MDX documents.

---
Repository: /testbed
