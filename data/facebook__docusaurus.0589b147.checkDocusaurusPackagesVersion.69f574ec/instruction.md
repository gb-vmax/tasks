# Bug Report

### Describe the bug

I'm experiencing an issue where Docusaurus is incorrectly validating plugin versions. The version checker seems to be throwing errors for packages that shouldn't be checked, while allowing mismatched versions for official @docusaurus packages.

### Reproduction

1. Set up a Docusaurus site with multiple official @docusaurus plugins
2. Install different versions of @docusaurus plugins (e.g., @docusaurus/plugin-content-docs at a different version than @docusaurus/core)
3. Run the build

The build completes successfully even though the official packages have mismatched versions, which should normally trigger a validation error.

Conversely, if you have third-party plugins that happen to match the Docusaurus version number, they might incorrectly trigger validation errors.

### Expected behavior

The version checker should:
- Throw an error when official @docusaurus/* packages have different versions from @docusaurus/core
- NOT validate version numbers for third-party packages (those not starting with @docusaurus/)

Currently it seems to be doing the opposite - validating third-party packages while ignoring official package version mismatches.

### System Info
- Docusaurus version: Latest
- Node version: 18.x

---
Repository: /testbed
