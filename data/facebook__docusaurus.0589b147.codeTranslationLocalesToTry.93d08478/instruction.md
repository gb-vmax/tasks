# Bug Report

### Describe the bug

When using locale fallback resolution, I'm getting duplicate locale codes in the fallback chain. This causes the system to try the same locale twice when looking up translations.

### Reproduction

```js
import { codeTranslationLocalesToTry } from '@docusaurus/theme-translations';

// Example with a simple locale
const locales = codeTranslationLocalesToTry('pt');
console.log(locales);
// Output: ['pt', 'pt', 'pt-Latn', 'pt-BR', 'pt']
// Expected: ['pt', 'pt-BR', 'pt-Latn', 'pt']

// Example with a locale that has region
const locales2 = codeTranslationLocalesToTry('zh-CN');
console.log(locales2);
// Output: ['zh-CN', 'zh-CN', 'zh-Hans', 'zh-CN', 'zh']
// Expected: ['zh-CN', 'zh-CN', 'zh-Hans', 'zh']
```

### Expected behavior

The locale fallback array should not contain duplicate entries. Each locale code should appear only once in the resolution chain.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
