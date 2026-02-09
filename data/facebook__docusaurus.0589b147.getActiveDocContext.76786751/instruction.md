# Bug Report

### Describe the bug

The active document context is not being identified correctly when navigating between docs. When I'm on a specific documentation page, the alternate versions sidebar is showing incorrect documents from other versions instead of the corresponding document in each version.

### Reproduction

1. Set up a multi-version docs site with at least 2 versions
2. Navigate to a specific doc page (e.g., `/docs/guides/introduction`)
3. Check the version dropdown or alternate version links
4. The alternate versions are pointing to wrong documents instead of the same doc ID across versions

For example:
- Current page: `/docs/2.0/guides/introduction`
- Expected alternate version link: `/docs/1.0/guides/introduction`
- Actual alternate version link: Shows a completely different document from version 1.0

### Expected behavior

When viewing a document in one version, the alternate version links should point to the same document (matching by doc ID) in other versions. The version switcher should allow users to view the same content across different documentation versions.

### Additional context

This seems to have broken recently. The version dropdown used to work correctly and show the right corresponding pages across versions. Now it's behaving erratically and mapping to incorrect documents.

---
Repository: /testbed
