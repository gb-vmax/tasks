# Bug Report

### Describe the bug

When using certain locale strings with the i18n system, the calendar selection logic appears to be returning the wrong calendar type. Instead of getting the primary/default calendar for a locale, I'm getting what seems to be a fallback or alternative calendar.

### Reproduction

```js
// Example with a locale that has multiple calendar systems
const locale = 'ar-SA'; // Arabic (Saudi Arabia)

// The calendar being returned doesn't match what I expect
// Expected: 'gregory' (Gregorian calendar, the primary one)
// Actual: Getting a different calendar type
```

This seems to affect locales that support multiple calendar systems. The behavior changed recently and now I'm getting unexpected calendar types for certain locales.

### Expected behavior

The i18n calendar detection should return the primary/default calendar for a given locale, which in most cases should be 'gregory' (Gregorian calendar) unless explicitly specified otherwise in the locale string (e.g., with `-u-ca-` extension).

### Additional context

This is impacting date formatting across the site for certain locales. The dates are being formatted with the wrong calendar system, which is confusing for users.

---
Repository: /testbed
