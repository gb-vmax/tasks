# Bug Report

### Describe the bug

I'm experiencing an issue with the docs plugin where translation files are not being properly matched to their corresponding content. After updating, the translation system seems to be broken - translations are not being applied to the documentation pages.

### Reproduction

1. Set up a Docusaurus site with the docs plugin
2. Configure i18n with translation files for documentation
3. Add translation JSON files in the expected directory structure
4. Build or serve the site
5. Navigate to a translated version of the docs

**Expected:** The translated content should be displayed based on the translation files.

**Actual:** The original content is shown instead, translations are ignored.

### Additional context

This appears to affect how translation files are being looked up and applied to the loaded content. The translation file mapping doesn't seem to be working correctly, causing the system to fail to find the appropriate translations even when they exist.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
