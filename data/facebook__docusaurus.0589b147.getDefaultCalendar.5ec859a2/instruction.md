# Bug Report

### Describe the bug

When using locales with explicit calendar systems specified in the locale string (e.g., `en-US-u-ca-islamic`), the calendar detection is not working correctly. The system is returning the wrong calendar or falling back to 'gregory' unexpectedly.

### Reproduction

```js
// Example locale strings that should return their specified calendar
const locale1 = 'en-US-u-ca-islamic';
const locale2 = 'ar-SA-u-ca-islamic-umalqura';
const locale3 = 'ja-JP-u-ca-japanese';

// The calendar should be extracted from the locale string
// But it's not being detected properly
```

When a locale string explicitly includes a calendar identifier using the Unicode extension (`-u-ca-xxx`), the calendar should be correctly identified and returned. However, the current behavior seems to ignore or incorrectly handle these explicit calendar specifications.

### Expected behavior

When a locale string contains an explicit calendar identifier (e.g., `-u-ca-islamic`), that calendar should be detected and returned. The function should prioritize the explicitly specified calendar from the locale string before falling back to other detection methods.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
