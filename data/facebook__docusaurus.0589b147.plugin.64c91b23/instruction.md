# Bug Report

### Describe the bug

Links in MDX files are not being transformed correctly. After a recent update, markdown links are no longer being processed and converted to the expected format. This affects both internal and external links in documentation pages.

### Reproduction

Create an MDX file with markdown links:

```md
# My Page

Check out [this link](./other-page.md) for more info.

Also see [external link](https://example.com).
```

The links are not being transformed as they should be. Internal links to `.md` files should be converted to proper routes, but they remain unchanged.

### Expected behavior

- Internal markdown links like `[text](./page.md)` should be transformed to proper Docusaurus routes
- Link transformation should process all links in the document
- Both relative and absolute links should be handled correctly

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
