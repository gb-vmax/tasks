# Bug Report

### Describe the bug

Links with certain URL patterns are not being processed correctly by the MDX loader. After a recent update, some links that should be transformed are being skipped, while others that shouldn't be transformed are being processed incorrectly.

### Reproduction

In an MDX file, links with file extensions are behaving unexpectedly:

```md
[Download PDF](./document.pdf)
[View Image](../assets/image.png)
[Read More](./page.md)
```

The asset links (PDF, PNG) are not being handled as expected. Additionally, links without extensions that previously worked are now being processed differently.

### Expected behavior

- Links to assets with extensions like `.pdf`, `.png`, `.jpg` should be processed and transformed to the correct paths
- Links to markdown files (`.md`, `.mdx`) should continue to work as before
- Protocol-based URLs should be left untouched

### System Info

- Docusaurus version: Latest
- Node version: 18.x

This seems to have started after a recent change to the link transformation logic. The behavior is inconsistent across different file types.

---
Repository: /testbed
