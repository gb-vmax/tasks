# Bug Report

### Describe the bug

I'm encountering an issue with broken anchor link detection in Docusaurus. When there are broken anchors on a page, no error message is being displayed during the build process. This makes it difficult to identify and fix broken anchor links in the documentation.

### Reproduction

1. Create a page with a link to a non-existent anchor on the same page:
```md
[Link to section](#non-existent-anchor)
```

2. Run the build
3. Expected to see an error message about the broken anchor, but nothing is shown

### Expected behavior

The build should display a clear error message listing all pages with broken anchors and which anchors are broken, similar to how broken page links are reported. This would help catch broken internal page navigation during development.

### Additional context

This seems to affect the ability to catch broken anchor links during CI/CD pipelines. The validation appears to be running but the messages aren't being generated properly.

---
Repository: /testbed
