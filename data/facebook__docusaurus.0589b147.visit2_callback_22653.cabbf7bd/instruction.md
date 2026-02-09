# Bug Report

### Describe the bug

I'm experiencing an issue with MDX where definitions and footnote definitions aren't being recognized properly. It seems like the identifier matching has become case-sensitive or something changed with how duplicate definitions are handled.

### Reproduction

```mdx
[link]: https://example.com

This is a [link] reference.
```

When I try to use reference-style links or footnotes, they're not resolving correctly. The references appear as plain text instead of being converted to the appropriate elements.

Also noticed that if I have multiple definitions with the same identifier (in different cases), only some of them seem to work now, and it's inconsistent which ones get picked up.

### Expected behavior

Reference-style links and footnotes should work regardless of the case used in the identifier. The first definition with a given identifier should be used, and subsequent duplicates should be ignored (as per CommonMark spec).

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
