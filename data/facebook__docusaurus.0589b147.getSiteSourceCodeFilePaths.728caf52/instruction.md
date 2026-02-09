# Bug Report

### Describe the bug

After a recent update, the translation extraction is no longer picking up any translatable strings from the `src/` directory. The i18n workflow seems to be broken - when I run the translation extraction, it generates empty translation files even though I have `<Translate>` components and other translatable content in my source code.

### Reproduction

1. Create a Docusaurus site with translatable content in the `src/` directory
2. Add some `<Translate>` components or use the translation APIs in your custom React components
3. Run the translation extraction command
4. Check the generated translation files

Expected: Translation files should contain entries for all translatable strings found in `src/`

Actual: Translation files are empty or missing entries from the `src/` directory

### Additional context

This was working fine before, and all my translatable strings in the `src/` folder were being extracted correctly. Now it seems like the extractor is completely ignoring the source directory. Plugin translations still seem to work, but anything in my custom components under `src/` is not being picked up.

---
Repository: /testbed
