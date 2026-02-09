# Bug Report

### Describe the bug

I'm experiencing an issue with MDX link parsing where reference-style links are not being recognized correctly. Links that should work with reference definitions are being treated as regular text instead of being parsed as valid links.

### Reproduction

```md
This is a [reference link][ref-id] that should work.

[ref-id]: https://example.com
```

When parsing the above MDX content, the reference link is not being resolved. It appears that the link reference is being skipped or not properly detected during tokenization.

### Expected behavior

The reference-style link should be properly parsed and the link reference should be resolved to the defined URL. The output should treat `[reference link][ref-id]` as a valid link pointing to `https://example.com`.

### Additional context

This seems to affect all reference-style links in MDX documents. Direct links with inline URLs (like `[text](url)`) still work fine, but any link that uses a reference definition is broken.

---
Repository: /testbed
