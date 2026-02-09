# Bug Report

### Describe the bug

Translation files are only being generated for the default version instead of all versions. After a recent change, non-default versions are missing their translation files, which breaks i18n support for versioned documentation.

### Reproduction

1. Set up a Docusaurus site with multiple doc versions (e.g., version 1.0, 2.0, and current)
2. Enable i18n with multiple locales
3. Run the translation file generation
4. Check the generated translation files

**Expected:** Translation files should be generated for all versions

**Actual:** Only the default version gets translation files, other versions are missing their translations

### System Info
- Docusaurus version: latest
- Plugin: @docusaurus/plugin-content-docs

This is causing issues in multi-version documentation sites where users need to access translated content for older versions. The translations are completely missing for non-default versions.

---
Repository: /testbed
