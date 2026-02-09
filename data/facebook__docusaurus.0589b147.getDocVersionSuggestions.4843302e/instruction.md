# Bug Report

### Describe the bug

When navigating to versioned docs, the version banner suggestion is showing the wrong document. Instead of suggesting the latest version of the current document, it appears to be suggesting the document that corresponds to the latest version's path, which may not be the same document.

### Reproduction

1. Set up a docs site with multiple versions (e.g., v1.0, v2.0)
2. Have a document that exists in both versions but at different paths or with different content
3. Navigate to an older version of a specific document
4. Observe the version banner suggestion

The banner suggests navigating to a document based on the latest version's path structure rather than finding the actual latest version of the current document you're viewing.

### Expected behavior

The version banner should suggest the latest version of the **current document** you're viewing, not a document determined by the latest version's pathname. It should look up the correct alternate version based on the document context of the page you're currently on.

### System Info
- Docusaurus version: latest
- Browser: Any

---
Repository: /testbed
