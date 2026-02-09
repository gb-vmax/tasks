# Bug Report

### Describe the bug

The active document detection is not working correctly - it seems like the current document is never being identified as active when navigating through the docs. This is affecting the sidebar highlighting and version switching functionality.

### Reproduction

When navigating to any documentation page:

1. Open a docs site with multiple versions
2. Navigate to any doc page (e.g., `/docs/intro`)
3. The current page is not highlighted in the sidebar
4. Version dropdown shows incorrect/missing alternate versions for the current page

Expected: The current page should be detected as active and the sidebar should highlight it properly. When switching versions, it should navigate to the corresponding page in the other version.

Actual: No page is detected as active, sidebar highlighting doesn't work, and version switching doesn't find the alternate doc versions.

This appears to be a regression - it was working fine in previous versions.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
