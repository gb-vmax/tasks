# Bug Report

### Describe the bug

I'm experiencing an issue with locale fallback resolution in the theme translations. When using locales like "pt" or "zh", the fallback mechanism doesn't seem to be working correctly anymore. The locale codes appear to be in the wrong order or format.

### Reproduction

```js
// When using a simple locale like "pt"
const locales = codeTranslationLocalesToTry('pt');
// Expected: ['pt', 'pt-BR', 'pt-Latn', 'pt']
// Getting unexpected locale format with region-language instead of language-region
```

The function should return a list of locale codes to try in order, but the format seems incorrect. For example, with Portuguese, I'd expect to see "pt-BR" but instead I'm seeing something like "BR-pt" which is not a valid locale code format.

### Expected behavior

The function should return properly formatted locale codes in the correct order:
1. Original locale (e.g., "pt")
2. Language + Region (e.g., "pt-BR")
3. Language + Script (e.g., "pt-Latn")
4. Language only (e.g., "pt")

This is breaking translation fallback for several languages in my project.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
