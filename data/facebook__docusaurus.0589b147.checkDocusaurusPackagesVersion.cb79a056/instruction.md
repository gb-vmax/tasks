# Bug Report

### Describe the bug

I'm experiencing an issue where Docusaurus is not properly validating the versions of official `@docusaurus/*` packages. It seems like packages with mismatched versions are not being caught during the build process, which should normally throw an error to ensure all official packages use the same version.

### Reproduction

1. Set up a Docusaurus project with `@docusaurus/core` at a specific version (e.g., 2.4.0)
2. Install another official Docusaurus package (like `@docusaurus/plugin-content-docs`) at a different version (e.g., 2.3.0)
3. Run the build

### Expected behavior

The build should fail with an error message indicating that all official `@docusaurus/*` packages must have the exact same version as `@docusaurus/core`. This version mismatch check is important to prevent compatibility issues.

### Actual behavior

The build proceeds without throwing the expected version mismatch error, even when official Docusaurus packages have different versions installed.

### System Info

- Docusaurus version: 2.x
- Node version: 18.x

This validation is critical for catching version mismatches early before they cause runtime issues. Would appreciate if this could be looked into!

---
Repository: /testbed
