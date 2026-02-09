# Bug Report

### Describe the bug

When using a slug in the front matter that starts with `/`, the slug is being incorrectly processed. Instead of treating it as an absolute path (starting from the root), it appears to be removing the leading slash and treating it as a relative path.

### Reproduction

Create a markdown file with the following front matter:

```md
---
slug: /my-custom-slug
---

# My Document
```

The expected behavior is that the document should be accessible at `/my-custom-slug`, but instead it's being processed as if the slug was `my-custom-slug` (without the leading slash).

### Expected behavior

When a slug starts with `/`, it should be treated as an absolute path and used as-is without modification. The leading slash should be preserved to indicate that this is a root-level path.

### System Info
- Docusaurus version: latest
- Plugin: @docusaurus/plugin-content-docs

This seems to have started happening recently. Previously, absolute slugs with leading slashes worked correctly.

---
Repository: /testbed
