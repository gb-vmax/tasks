# Bug Report

### Describe the bug

I'm encountering an issue with locale configuration where the `direction` and `path` properties seem to be swapped or incorrectly assigned. When setting up i18n locales, the text direction is being set to the locale string itself (like "en" or "ar") instead of the actual direction value ("ltr" or "rtl"), and the path is being set to what appears to be the direction value.

### Reproduction

```js
const localeConfig = getDefaultLocaleConfig('ar');

console.log(localeConfig.direction); // Expected: 'rtl', Got: 'ar'
console.log(localeConfig.path);      // Expected: 'ar', Got: 'rtl'
```

When configuring an RTL language like Arabic:
1. The `direction` property contains the locale code ('ar') instead of 'rtl'
2. The `path` property contains the direction ('rtl') instead of the locale code

This causes issues with:
- CSS direction styles not being applied correctly
- Locale paths being incorrect in the URL structure

### Expected behavior

For a locale like 'ar' (Arabic):
- `direction` should be 'rtl' 
- `path` should be 'ar'

For a locale like 'en' (English):
- `direction` should be 'ltr'
- `path` should be 'en'

The locale config should properly assign text direction based on the language's writing direction, and the path should use the locale identifier.

---
Repository: /testbed
