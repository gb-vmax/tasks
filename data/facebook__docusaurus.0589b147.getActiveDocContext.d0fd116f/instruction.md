# Bug Report

### Describe the bug

I'm experiencing an issue with the active document detection in the docs plugin. When navigating between different documentation pages, the wrong document is being identified as "active", and the version switcher seems to be completely broken - it's not showing alternate versions of the current document anymore.

### Reproduction

1. Set up a docs site with multiple versions (e.g., "1.0.0", "2.0.0", "current")
2. Create a document that exists across all versions (e.g., "intro.md" with id "intro")
3. Navigate to that document in any version
4. Check which document is marked as active
5. Try to use the version switcher to see alternate versions

### Expected behavior

- The current document should be correctly identified based on the URL pathname
- The version switcher should display all available versions of the current document
- Switching between versions should work properly

### Actual behavior

- The active document detection appears to be matching against the document ID instead of the path
- The alternate document versions are not being populated correctly (seems like an additional incorrect condition was added)
- Navigation and version switching is broken

### System Info

- Docusaurus version: latest
- Node version: 18.x

This seems like a regression that was recently introduced. The docs plugin was working fine before.

---
Repository: /testbed
