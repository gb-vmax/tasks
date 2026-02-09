# Bug Report

### Describe the bug

I'm experiencing an issue with versioned documentation where only some versions appear to be getting their translation files loaded. It seems like every other version is being skipped during the translation file generation process.

### Reproduction

1. Set up a Docusaurus project with multiple documentation versions (e.g., version 1.0, 2.0, 3.0, 4.0)
2. Configure translations for all versions
3. Build the site
4. Notice that translation files are only generated for alternating versions (e.g., versions 2.0 and 4.0 are present, but 1.0 and 3.0 are missing)

### Expected behavior

All documentation versions should have their translation files generated and loaded, not just every other version. The translation system should process all versions in the versions array.

### System Info
- Docusaurus version: Latest
- Node version: 18.x

This is causing half of our versioned docs to appear without proper translations, which is breaking the multilingual support for those versions.

---
Repository: /testbed
