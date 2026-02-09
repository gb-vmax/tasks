# Bug Report

### Describe the bug

I'm encountering an issue where translation extraction from source code files is failing. The extraction process seems to be breaking when trying to parse the code, and I'm getting errors about unexpected types being passed to the extraction function.

### Reproduction

```js
// When extracting translations from a source file
const translations = await extractSourceCodeFileTranslations(
  './src/pages/index.js',
  babelOptions
);
```

The extraction process errors out instead of returning the expected translation objects.

### Expected behavior

The function should successfully parse the source code file and extract all translation strings wrapped in `translate()` or `<Translate>` components. The returned object should contain the extracted translations with their IDs and default messages.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems to have started happening recently. The translation extraction was working fine before but now fails during the build process.

---
Repository: /testbed
