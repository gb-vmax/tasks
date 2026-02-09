# Bug Report

### Describe the bug

I'm experiencing an issue with localized URLs in my Docusaurus site. When using the default locale, the generated URLs are incorrect - they include the locale code in the path when they shouldn't.

### Reproduction

```js
// Configuration
const config = {
  baseUrl: '/',
  defaultLocale: 'en',
  locales: ['en', 'fr', 'es']
}

// When on default locale (en):
// Expected URL: /docs/intro
// Actual URL: /en (incorrect, includes locale code)

// When on non-default locale (fr):
// Expected URL: /fr/docs/intro
// Actual URL: /fr/docs/intro (correct)
```

The problem is that the default locale is getting its locale code appended to the base URL when it shouldn't. According to Docusaurus conventions, the default locale should not have a locale prefix in the URL.

### Expected behavior

- Default locale URLs should NOT include the locale code: `/docs/intro`
- Non-default locale URLs SHOULD include the locale code: `/fr/docs/intro`, `/es/docs/intro`

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
