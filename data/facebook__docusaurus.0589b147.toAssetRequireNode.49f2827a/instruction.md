# Bug Report

### Describe the bug

When using links in MDX files, the hash and search parameters in URLs are being swapped. Links that should have a hash fragment (like `#section`) are getting it treated as a search parameter, and vice versa.

### Reproduction

Create an MDX file with a link to a static asset that includes both hash and query parameters:

```md
[Download PDF](./assets/document.pdf?version=1#page=5)
```

After processing, the URL parameters are reversed - the hash becomes the search and the search becomes the hash.

### Expected behavior

The hash and search parameters should remain in their correct positions:
- Hash fragments (starting with `#`) should be preserved as hash
- Query strings (starting with `?`) should be preserved as search parameters

### System Info
- Docusaurus version: latest
- Node version: 18.x

This is causing issues with links that rely on proper URL fragment handling, especially for PDFs with page anchors or documents with section links.

---
Repository: /testbed
