# Bug Report

### Describe the bug

I'm experiencing an issue with route context initialization in Docusaurus. When navigating to pages, I'm getting an error about the route context not having the expected structure. The error message says "Unexpected: Docusaurus topmost route context has no `plugin` attribute" even though the route context should be properly initialized.

### Reproduction

This happens when:
1. Starting a fresh Docusaurus site
2. Navigating to any page
3. The route context should be initialized at the topmost level with a `plugin` attribute

The error appears to be thrown incorrectly - it seems like the validation logic for checking whether a route context is at the topmost level (should have `plugin` attribute) is inverted or checking the wrong condition.

### Expected behavior

The route context should be properly validated and merged without throwing errors. The topmost route context should have a `plugin` attribute and this should be accepted without errors.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems like a regression in the route context merging logic. The validation conditions might have been accidentally flipped.

---
Repository: /testbed
