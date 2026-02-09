# Bug Report

### Describe the bug

Image URLs with query parameters and hash fragments are not being handled correctly in MDX. When using images with both query strings and URL hashes, they seem to get swapped - the query string ends up in the hash position and vice versa.

### Reproduction

```md
![Alt text](./image.png?width=500#my-anchor)
```

When this markdown is processed, the query string (`?width=500`) and hash (`#my-anchor`) appear to be applied to the wrong parts of the generated code. The query parameters that should be part of the file loader path end up in the src attribute value, and the hash that should be in the src attribute ends up in the file loader path.

### Expected behavior

For an image like `./image.png?width=500#my-anchor`:
- The query string `?width=500` should be preserved with the src attribute
- The hash `#my-anchor` should be included in the require/import path for the file loader

Both parts should maintain their correct positions and not be swapped.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
