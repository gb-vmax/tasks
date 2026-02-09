# Bug Report

### Describe the bug

When generating translation files for docs, the first sidebar is being skipped and not included in the translation output. This means that any labels, categories, or items in the first sidebar won't be translatable.

### Reproduction

1. Set up a Docusaurus site with multiple sidebars in your docs plugin configuration
2. Create at least 2 sidebars (e.g., "tutorialSidebar" and "apiSidebar")
3. Run the translation extraction command
4. Check the generated translation files

Expected: All sidebars should be included in the translation file
Actual: The first sidebar is missing from the translations

### Additional context

This affects any documentation site with multiple sidebars where the first sidebar contains content that needs to be translated. The issue seems to have appeared recently as this was working correctly before.

---
Repository: /testbed
