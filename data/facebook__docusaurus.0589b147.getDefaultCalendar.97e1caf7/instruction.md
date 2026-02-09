# Bug Report

### Describe the bug

The calendar detection for locales is returning incorrect results. When I check the calendar for a locale, it's returning `undefined` instead of the expected default calendar value.

### Reproduction

```js
import { getDefaultLocaleConfig } from '@docusaurus/core/lib/server/i18n';

// Try getting locale config for a standard locale
const config = getDefaultLocaleConfig('en-US');
console.log(config.calendar); // Expected: 'gregory', Actual: undefined

// Same issue with other locales
const frConfig = getDefaultLocaleConfig('fr-FR');
console.log(frConfig.calendar); // Expected: 'gregory', Actual: undefined
```

### Expected behavior

The function should return `'gregory'` as the default calendar for standard locales that don't explicitly specify a calendar. Currently it seems to be returning `undefined` or an unexpected value.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This is breaking our i18n setup where we rely on proper calendar detection for date formatting. Any help would be appreciated!

---
Repository: /testbed
