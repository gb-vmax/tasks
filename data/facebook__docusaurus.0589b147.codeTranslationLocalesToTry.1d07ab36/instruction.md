# Bug Report

### Describe the bug

The locale fallback resolution is not working correctly for simple language codes. When I use a locale like "pt" (Portuguese), the system seems to be trying the wrong fallback order and I'm not getting the expected translations.

### Reproduction

When using a simple language code without region specification:

```js
// Using locale "pt" (Portuguese)
const locales = codeTranslationLocalesToTry("pt");

// The fallback chain doesn't seem right
// Expected to try "pt" first, then "pt-BR", then "pt-Latn"
// But the order appears to be different now
```

### Expected behavior

For a simple language code like "pt", the system should:
1. First try the exact locale provided ("pt")
2. Then fallback to the maximized region variant ("pt-BR" for Portuguese, not "pt-PT")
3. Then try script variants if needed
4. Finally fallback to just the language code

This is important because for languages like Portuguese, "pt-BR" (Brazilian Portuguese) is more commonly used than "pt-PT" (European Portuguese) in most contexts.

### System Info
- Docusaurus theme translations package
- Affects locale resolution for translation files

---
Repository: /testbed
