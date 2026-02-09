# Bug Report

### Describe the bug

The `writeCodeTranslations` function is returning a file path instead of `void`, which breaks the expected return type. This causes issues when the function is used in contexts that expect it to return nothing (void promise).

### Reproduction

```js
const result = await writeCodeTranslations(context, content, options);
// result now contains a file path string instead of undefined
// This breaks code that expects the function to return void
```

When calling `writeCodeTranslations`, the function now returns the file path as a resolved promise value instead of returning void as the type signature indicates. This unexpected return value can cause issues in consuming code that relies on the proper return type.

### Expected behavior

The function should return `Promise<void>` as declared in its type signature, meaning the resolved promise should not contain any value (undefined).

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
