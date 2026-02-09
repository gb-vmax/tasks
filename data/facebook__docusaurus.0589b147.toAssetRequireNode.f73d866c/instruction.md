# Bug Report

### Describe the bug

When using markdown links to local assets with query parameters, the query string is being stripped from the final URL. Links that should preserve query parameters (like `?foo=bar`) are losing them after processing.

### Reproduction

Create a markdown file with a link to a local asset that includes query parameters:

```md
[Download file](./myfile.pdf?version=2)
```

After processing, the link becomes `./myfile.pdf` without the `?version=2` query parameter.

### Expected behavior

The query parameters should be preserved in the final link URL. The link should remain as `./myfile.pdf?version=2` so that the query string can be used by the server or client-side code.

### Additional context

This seems to affect only local asset links. External URLs with query parameters work fine. Also noticed that the `target="_blank"` attribute is being added to all asset links now, even when there's no hash fragment in the URL.

---
Repository: /testbed
