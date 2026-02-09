# Bug Report

### Describe the bug

When navigating to versioned documentation routes, the active version detection is not working correctly. Instead of matching the correct version based on the URL path, it seems to only match the last version regardless of which version's path I'm actually on.

### Reproduction

1. Set up a docs site with multiple versions (e.g., 1.0, 2.0, and current)
2. Navigate to a specific version like `/docs/2.0/some-page`
3. Check which version is detected as active

Expected: Version 2.0 should be detected as active
Actual: The last version is always detected as active, even when on a different version's route

### Additional context

This affects version-specific features like version dropdowns and version banners, which now show incorrect information when browsing older documentation versions. The issue appears to be with how the path matching logic determines which version corresponds to the current route.

---
Repository: /testbed
