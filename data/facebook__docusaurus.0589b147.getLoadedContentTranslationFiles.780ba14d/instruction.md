# Bug Report

### Describe the bug

After a recent update, translation files are not being loaded correctly in the docs plugin. The translations simply disappear and don't get applied to the documentation pages.

### Reproduction

Set up a Docusaurus site with the docs plugin and add translation files for your documentation versions. The translation files are created and exist in the correct location, but they're not being picked up and applied.

Steps to reproduce:
1. Configure docs plugin with multiple versions
2. Add translation files for those versions
3. Build or start the dev server
4. Notice that translations are missing/not applied

### Expected behavior

Translation files should be loaded and applied to the documentation content. All translation files that exist should be processed and made available to the docs plugin.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems to have started happening recently. The translation files are there but something in the loading process is filtering them out incorrectly.

---
Repository: /testbed
