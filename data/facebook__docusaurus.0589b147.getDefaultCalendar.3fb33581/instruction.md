# Bug Report

### Describe the bug

When using locales without an explicit calendar specified (e.g., `en-US`), the calendar detection is returning `undefined` instead of the default calendar for that locale. This affects i18n functionality where the calendar system should be automatically inferred.

### Reproduction

```js
// Using a locale without explicit calendar specification
const locale = 'en-US';
const calendar = getDefaultCalendar(locale);

console.log(calendar); // Expected: 'gregory', Actual: undefined
```

The function should return the default calendar (e.g., 'gregory' for most Western locales) when no calendar is explicitly specified in the locale string, but it's returning `undefined` instead.

### Expected behavior

The function should correctly detect and return the default calendar for a given locale. For example:
- `en-US` should return `'gregory'`
- `ja-JP` should return `'gregory'` 
- Locales with explicit calendar like `en-US-u-ca-islamic` should return `'islamic'`

This appears to have started happening recently and is breaking calendar-related i18n features.

---
Repository: /testbed
