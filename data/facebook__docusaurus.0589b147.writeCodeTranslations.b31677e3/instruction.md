# Bug Report

### Describe the bug

The `writeCodeTranslations` function is not returning a Promise anymore, which breaks code that depends on awaiting this function. This causes issues when trying to wait for translation files to be written before proceeding with subsequent operations.

### Reproduction

```js
// This used to work but now returns undefined
const result = await writeCodeTranslations(context, content, options);

// Or when chaining operations
await writeCodeTranslations(context, content, options)
  .then(() => {
    // This callback never executes
    console.log('Translations written successfully');
  });
```

### Expected behavior

The function should return a Promise that resolves when the translation file has been written, allowing callers to await the operation or chain `.then()` handlers.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
