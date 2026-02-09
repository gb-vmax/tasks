# Bug Report

### Describe the bug

I'm experiencing an issue with the docs plugin where translation files are being generated incorrectly for versioned documentation. It seems like the translation content is being split across multiple files instead of being merged into a single file per version.

### Reproduction

1. Set up a Docusaurus project with versioned docs
2. Configure multiple versions with custom labels
3. Run the translation extraction
4. Check the generated translation files

Expected: One translation file per version containing both version label and sidebar translations
Actual: Two separate translation files are generated, splitting the version and sidebar translations

### Additional context

This appears to affect projects with multiple doc versions where the version label differs from the version name. The translation files are no longer being properly merged, which breaks the expected translation file structure.

### System Info
- Docusaurus version: latest
- Plugin: @docusaurus/plugin-content-docs

---
Repository: /testbed
