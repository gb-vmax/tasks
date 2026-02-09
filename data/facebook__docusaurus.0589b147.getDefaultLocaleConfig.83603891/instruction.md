# Bug Report

### Describe the bug

When using locale configurations with region-specific codes (e.g., `en-US`, `zh-CN`), the default locale label is being generated incorrectly. Instead of using the full locale string to determine the appropriate label, only the base language code is being used.

### Reproduction

```js
// Example with Chinese locales
const config = {
  i18n: {
    defaultLocale: 'zh-CN',
    locales: ['en', 'zh-CN', 'zh-TW']
  }
}

// The label for zh-CN and zh-TW will be the same
// Both will use 'zh' instead of the full locale code
```

### Expected behavior

Each locale variant should get its own appropriate label based on the full locale string (e.g., `zh-CN` vs `zh-TW`), not just the base language code. For example:
- `zh-CN` should get a label for Simplified Chinese
- `zh-TW` should get a label for Traditional Chinese

Currently both would receive the same label since they both start with `zh`.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
