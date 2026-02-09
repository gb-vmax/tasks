# Bug Report

### Describe the bug

Translation extraction is not working - no translations are being detected from source files. After updating, the translation extraction process completes without errors but doesn't find any translatable content in the `src/` directory.

### Reproduction

1. Set up a Docusaurus site with translatable content in the `src/` directory
2. Add some translatable strings using `<Translate>` components or `translate()` calls
3. Run the translation extraction command
4. Check the generated translation files - they're empty or missing expected translations

Example structure:
```
my-site/
  src/
    pages/
      index.js  // Contains <Translate> components
    components/
      MyComponent.js  // Contains translate() calls
```

### Expected behavior

The translation extractor should scan all files in the `src/` directory and extract translatable strings into the translation JSON files. All `<Translate>` components and `translate()` function calls should be detected and added to the translation catalog.

### System Info
- Docusaurus version: Latest
- Node version: 18.x

---
Repository: /testbed
