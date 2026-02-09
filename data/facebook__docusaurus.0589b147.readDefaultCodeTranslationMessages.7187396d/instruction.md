# Bug Report

### Describe the bug

When trying to load translation files, the function doesn't return the translation content anymore. It seems like the translation loading mechanism is broken - the function always returns `undefined` even when valid translation files exist.

### Reproduction

```js
const translations = await readDefaultCodeTranslationMessages({
  dirPath: '/path/to/translations',
  locale: 'fr_FR',
  name: 'common'
});

console.log(translations); // undefined - expected: translation object
```

### Expected behavior

The function should return the content of the first matching translation file. For example:
- If `fr_FR.json` exists, return its content
- Otherwise, try `fr.json` and return its content if it exists
- Return undefined only if no matching files are found

Currently it's returning `undefined` in all cases, even when the translation files are present and valid.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
