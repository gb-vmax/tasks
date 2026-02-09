# Bug Report

### Describe the bug

When using custom scoped packages that contain `@docusaurus/` in their name (like `@mycompany/@docusaurus/plugin-custom`), the build fails with an error claiming that the package version doesn't match the core Docusaurus version, even though it's not an official Docusaurus package.

### Reproduction

1. Create a custom plugin with a scoped package name that includes `@docusaurus/` somewhere in it (e.g., `@myorg/@docusaurus/custom-plugin`)
2. Install it in your Docusaurus project
3. Try to build the project

The build will fail with an error message like:
```
Invalid name=@myorg/@docusaurus/custom-plugin version number=1.0.0.
All official @docusaurus/* packages should have the exact same version as @docusaurus/core (number=3.0.0).
```

### Expected behavior

Only official Docusaurus packages (those that actually start with `@docusaurus/`) should be subject to version checking. Custom scoped packages that happen to contain the string `@docusaurus/` elsewhere in their name should not trigger this validation error.

### System Info
- Docusaurus version: 3.x
- Node version: 18.x

---
Repository: /testbed
