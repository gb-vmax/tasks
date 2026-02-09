# Bug Report

### Describe the bug

I'm experiencing an issue with the docs plugin where translations are not being applied to the loaded content. The documentation pages are showing up in the original language instead of the translated versions, even though translation files are present and configured correctly.

### Reproduction

1. Set up a Docusaurus project with the docs plugin
2. Add translation files for a specific locale (e.g., `i18n/fr/docusaurus-plugin-content-docs/current/**/*.json`)
3. Build or run the site with the translated locale
4. Navigate to the documentation pages

**Expected:** Documentation should display in the translated language
**Actual:** Documentation remains in the original language

### Additional context

This seems to affect all versions of the documentation. The translation files are being loaded but the actual content isn't getting updated with the translations. The issue appears to be in how the loaded content is being processed.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
