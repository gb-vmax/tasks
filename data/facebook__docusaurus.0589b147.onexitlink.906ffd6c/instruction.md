# Bug Report

### Describe the bug

I'm experiencing an issue with MDX link parsing where regular links are being incorrectly treated as reference-style links. When I use standard markdown links with inline URLs, they're being converted to reference links instead of staying as regular links.

### Reproduction

```mdx
[Click here](https://example.com)
```

When this is parsed, it seems to be treated as a reference-style link instead of a regular inline link. The URL is being deleted and the link is being converted to a reference type.

### Expected behavior

Regular markdown links with inline URLs should remain as regular links with the `url` property intact. Only actual reference-style links (like `[text][ref]` or `[ref][]`) should be converted to reference link types.

The parser should distinguish between:
- Regular links: `[text](url)` - should keep the URL
- Reference links: `[text][ref]` - should be marked as references

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have broken standard link functionality in MDX documents. Any help would be appreciated!

---
Repository: /testbed
