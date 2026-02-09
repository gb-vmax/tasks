# Bug Report

### Describe the bug

I'm having an issue with versioned sidebars in the docs plugin. After updating, the plugin can't find my versioned sidebar files anymore and is throwing errors about missing sidebar configuration.

### Reproduction

1. Set up a docs plugin with versioning enabled
2. Create a versioned sidebar file at the standard location: `versioned_sidebars/version-1.0.0-sidebars.json`
3. Build the site

The plugin fails to locate the sidebar file even though it exists at the expected path.

### Expected behavior

The plugin should correctly locate and load versioned sidebar files from `versioned_sidebars/version-{versionName}-sidebars.json` as it did before.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
