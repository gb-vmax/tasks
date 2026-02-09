# Bug Report

### Describe the bug

When using the alternate page utils in a multi-locale setup, the localized base URLs are being generated incorrectly. The default locale is getting the locale code appended to it when it shouldn't, and non-default locales are missing the locale code in their base URLs.

### Reproduction

```js
// Assume we have:
// - defaultLocale: 'en'
// - baseUrlUnlocalized: 'https://example.com/'
// - alternate locale: 'fr'

const utils = useAlternatePageUtils();

// For default locale 'en':
const enBaseUrl = getLocalizedBaseUrl('en');
// Returns: 'https://example.com/en' 
// Expected: 'https://example.com/'

// For alternate locale 'fr':
const frBaseUrl = getLocalizedBaseUrl('fr');
// Returns: 'https://example.com/'
// Expected: 'https://example.com/fr/'
```

### Expected behavior

- Default locale should return the base URL without any locale suffix
- Non-default locales should return the base URL with the locale code appended

The URLs are completely backwards from what they should be. This affects alternate page links and probably breaks i18n navigation.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
