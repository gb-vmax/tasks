# Bug Report

### Describe the bug

I'm experiencing an issue with the default locale configuration generation. When using the i18n system, the `htmlLang` and `path` properties in the locale config are being set to incorrect values instead of the actual locale code.

### Reproduction

```js
const locale = 'fr';
const config = getDefaultLocaleConfig(locale);

console.log(config.htmlLang); // Expected: 'fr', but getting the locale label instead
console.log(config.path); // Expected: 'fr', but getting the language direction instead
```

When I create a locale config for a language like French ('fr') or Arabic ('ar'), the resulting configuration object has:
- `htmlLang` set to the locale label (e.g., 'Français' or 'العربية') instead of the locale code
- `path` set to the language direction ('ltr' or 'rtl') instead of the locale code

### Expected behavior

The `htmlLang` property should be set to the locale code (e.g., 'fr', 'ar', 'en') for proper HTML lang attribute values.

The `path` property should be set to the locale code for correct URL path generation.

Both should use the original `locale` parameter, not derived values from other functions.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
