# Bug Report

### Describe the bug

I'm experiencing an issue with route context initialization in Docusaurus. When navigating between pages, I'm getting an error "Unexpected: no Docusaurus route context found" even though the route context should be properly set up.

### Reproduction

This happens when:
1. Starting the dev server
2. Navigating to any page in the site
3. The app crashes with the error mentioned above

The error appears to be thrown incorrectly - it seems like the route context validation logic is backwards. When there IS a parent context, it's throwing an error saying there's NO context found.

### Expected behavior

The app should navigate normally between pages without throwing route context errors. The route context should be properly merged from parent to child routes.

### System Info
- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
