# Bug Report

### Describe the bug

The default locale configuration seems to have incorrect values assigned to `direction` and `calendar` fields. When using locales with region codes (like `en-US`), the `htmlLang` attribute is being set to just the language code without the region, and the `direction` and `calendar` fields appear to be swapped.

### Reproduction

```js
const localeConfig = getDefaultLocaleConfig('en-US');

console.log(localeConfig.direction); // Expected: 'ltr', but getting calendar value
console.log(localeConfig.calendar); // Expected: 'gregory', but getting direction value
console.log(localeConfig.htmlLang); // Expected: 'en-US', but getting 'en'
```

### Expected behavior

- `direction` should contain the text direction (e.g., 'ltr' or 'rtl')
- `calendar` should contain the calendar system (e.g., 'gregory')
- `htmlLang` should preserve the full locale string including region code (e.g., 'en-US')

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
