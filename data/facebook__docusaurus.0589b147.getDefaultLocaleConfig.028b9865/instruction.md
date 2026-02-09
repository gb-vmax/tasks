# Bug Report

### Describe the bug

I'm experiencing an issue with the i18n locale configuration where the `htmlLang` and `calendar` properties appear to have incorrect values. When I inspect the generated locale config, the `htmlLang` field contains what looks like calendar information, and the `calendar` field contains direction information instead of the expected values.

### Reproduction

```js
import { getDefaultLocaleConfig } from '@docusaurus/core';

const config = getDefaultLocaleConfig('en');
console.log(config.htmlLang); // Expected: 'en', but getting calendar value
console.log(config.calendar); // Expected: calendar value, but getting direction (ltr/rtl)
```

### Expected behavior

The locale config should have:
- `htmlLang` set to the locale string (e.g., 'en', 'fr', 'ar')
- `calendar` set to the appropriate calendar system for that locale

Instead, these two properties seem to be swapped or assigned incorrect values.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This is causing issues with HTML lang attributes and calendar-related functionality in my site. Any help would be appreciated!

---
Repository: /testbed
