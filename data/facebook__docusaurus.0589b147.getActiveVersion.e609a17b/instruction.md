# Bug Report

### Describe the bug

I'm experiencing an issue with version detection in the docs plugin. When navigating to different documentation versions, the active version is not being detected correctly. It seems like the version matching logic is inverted - pages that should match a version path are not being recognized as part of that version.

### Reproduction

1. Set up a Docusaurus site with multiple documentation versions
2. Navigate to a versioned docs page (e.g., `/docs/version-1.0/some-page`)
3. The active version detection fails and returns the wrong version or undefined

For example, with versions configured like:
- Latest version at `/docs/*`
- Version 1.0 at `/docs/version-1.0/*`

When visiting `/docs/version-1.0/introduction`, the function returns undefined or the wrong version instead of recognizing it as version 1.0.

### Expected behavior

The `getActiveVersion` function should correctly identify which version a given pathname belongs to. When I'm on a versioned docs page, it should return that version's metadata.

### Additional context

This appears to be affecting version-specific features like the version dropdown and version banners, as they rely on correctly identifying the active version from the current pathname.

---
Repository: /testbed
