# Bug Report

### Describe the bug

When extracting translations from plugins that have a theme path, the theme path is not being included in the source code file paths. This causes translation extraction to miss translations defined in plugin themes.

### Reproduction

Steps to reproduce:
1. Create a plugin with a `getThemePath()` method that returns a valid theme directory
2. Add some translatable content in the theme files (e.g., using `<Translate>` components)
3. Run translation extraction
4. Notice that translations from the theme files are not extracted

The issue appears to affect any plugin that provides theme components with translatable strings.

### Expected behavior

Translation extraction should include files from the plugin's theme path when `getThemePath()` returns a valid path. All translatable strings in theme components should be detected and extracted.

### Additional context

This seems to have started happening recently. Previously, theme paths were being correctly included in the translation extraction process.

---
Repository: /testbed
