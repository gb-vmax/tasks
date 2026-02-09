# Bug Report

### Describe the bug

When using locale fallback for translations, I'm getting duplicate locale codes in the fallback chain. This seems to be causing issues with translation resolution as the same locale variant is being checked twice instead of trying different variants.

### Reproduction

```js
import { codeTranslationLocalesToTry } from '@docusaurus/theme-translations';

// Example with Portuguese
const locales = codeTranslationLocalesToTry('pt');
console.log(locales);
// Expected: ['pt', 'pt-BR', 'pt-Latn', ...]
// Actual: ['pt', 'pt', 'pt-BR', 'pt-BR']

// Example with Chinese
const zhLocales = codeTranslationLocalesToTry('zh');
console.log(zhLocales);
// Getting duplicate entries instead of proper fallback chain
```

### Expected behavior

The function should return a list of unique locale codes to try in fallback order. For a locale like "pt", it should try:
1. The original locale ("pt")
2. Language + region ("pt-BR")
3. Language + script ("pt-Latn")
4. Just the language code ("pt")

Instead, I'm seeing the same locale codes appearing multiple times in the array, which breaks the fallback mechanism for finding appropriate translations.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
