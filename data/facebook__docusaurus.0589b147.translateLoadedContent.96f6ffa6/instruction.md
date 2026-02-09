# Bug Report

### Describe the bug

After a recent update, documentation translations are not being applied correctly. The translated content is not showing up on the site even though translation files are present and properly configured.

### Reproduction

1. Set up a Docusaurus project with the docs plugin
2. Add translation files for documentation content
3. Configure i18n with a non-default locale (e.g., `fr`, `es`, etc.)
4. Build the site and navigate to the translated version
5. Observe that the documentation still shows the original content instead of the translated version

Expected: The documentation should display the translated content from the translation files.

Actual: The documentation shows the original untranslated content, as if the translation files are being ignored.

### Additional context

This appears to affect all documentation pages. The translation files are being loaded but the content is not being replaced with the translated versions. Other parts of the site (like theme translations) seem to work fine, it's specifically the docs plugin content that's not translating.

---
Repository: /testbed
