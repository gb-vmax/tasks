# Bug Report

### Describe the bug

I'm experiencing an issue with the docs plugin where translation files aren't being matched correctly. The translated content isn't showing up even though the translation files are present in the i18n directory.

### Reproduction

1. Set up a Docusaurus site with the docs plugin
2. Add translation files for documentation
3. Build the site with a non-default locale
4. The content remains untranslated

It seems like the translation file lookup mechanism is broken. The translations are there but they're not being applied to the loaded content.

### Expected behavior

Translation files should be properly matched and applied to the documentation content. The site should display translated versions when built with different locales.

### Additional context

This might be related to how translation files are being indexed or keyed internally. The structure of the returned content also seems off - getting nested `loadedVersions` objects which doesn't match the expected schema.

---
Repository: /testbed
