# Bug Report

### Describe the bug

Broken markdown links are not being reported when processing documentation files. The validation that should catch and report broken links appears to have stopped working.

### Reproduction

1. Create a markdown file with a broken internal link:
```md
Check out [this page](./non-existent-page.md) for more info.
```

2. Build the documentation

3. Expected: A warning/error about the broken link
   Actual: No warning is shown, broken link goes undetected

### Expected behavior

The `onBrokenMarkdownLink` callback should be invoked for each broken markdown link found during the build process, allowing users to be notified about broken references in their documentation.

### System Info
- Docusaurus version: Latest
- Node version: 18.x

This seems like a regression as broken link detection was working in previous builds. The links are being identified but the notification mechanism isn't being triggered.

---
Repository: /testbed
