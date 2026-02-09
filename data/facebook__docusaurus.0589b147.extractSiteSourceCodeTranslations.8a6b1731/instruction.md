# Bug Report

### Describe the bug

I'm experiencing an issue with translation extraction where duplicate source code file paths are being processed instead of including the extra source code file paths. This results in translations from the extra files not being extracted.

### Reproduction

```js
const sourceCodeFilePaths = ['src/pages/index.js', 'src/components/Hero.js'];
const extraSourceCodeFilePaths = ['src/theme/Footer.js'];

// When extracting translations, only sourceCodeFilePaths are processed twice
// extraSourceCodeFilePaths are ignored completely
const translations = await extractSiteSourceCodeTranslations(
  siteDir,
  plugins,
  sourceCodeFilePaths,
  babelOptions,
  extraSourceCodeFilePaths
);

// Translations from 'src/theme/Footer.js' are missing
```

### Expected behavior

The translation extractor should process both the regular source code file paths AND the extra source code file paths. Currently it seems to be duplicating the main source code paths instead of adding the extra ones.

### Additional context

This affects any workflow that relies on extracting translations from additional file paths beyond the default ones. The extra files are completely skipped during translation extraction.

---
Repository: /testbed
