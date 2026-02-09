# Bug Report

### Describe the bug

I'm experiencing an issue with version detection in the docs plugin. When I have multiple documentation versions, the active version is not being correctly identified based on the current pathname.

### Reproduction

Setup:
- Multiple doc versions configured (e.g., current, 1.0, 2.0)
- Latest version path: `/docs/`
- Older version paths: `/docs/1.0/`, `/docs/2.0/`

When navigating to an older version like `/docs/1.0/introduction`, the system incorrectly identifies the active version as the latest version instead of version 1.0.

Expected: Active version should be `1.0`
Actual: Active version is detected as `current` (latest)

This seems to affect the version dropdown and potentially other version-related UI elements. The version matching logic appears to be prioritizing the wrong version when multiple paths could match.

### Expected behavior

The active version should be correctly identified based on the pathname. When visiting `/docs/1.0/some-page`, version 1.0 should be detected as active, not the latest version.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
