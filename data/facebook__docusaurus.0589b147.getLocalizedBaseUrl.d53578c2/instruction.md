# Bug Report

### Describe the bug

I'm experiencing an issue with localized URLs in my Docusaurus site. The alternate page URLs are being generated incorrectly - the default locale is getting a locale prefix when it shouldn't, and non-default locales are missing their locale prefix entirely.

### Reproduction

```js
// Setup: defaultLocale = 'en', other locale = 'fr'
// baseUrlUnlocalized = '/docs/'

// Current behavior:
// For default locale 'en': generates '/docs/en' (should be '/docs/')
// For other locale 'fr': generates '/docs/' (should be '/docs/fr/')
```

Steps to reproduce:
1. Set up a multi-locale Docusaurus site with a default locale (e.g., 'en')
2. Add at least one additional locale (e.g., 'fr')
3. Navigate to any page and check the alternate language links
4. The URLs are swapped - default locale has the prefix, non-default locales don't

### Expected behavior

- Default locale pages should NOT have a locale prefix in the URL
- Non-default locale pages SHOULD have their locale prefix in the URL

For example, with default locale 'en' and alternate locale 'fr':
- English page: `/docs/page` (no 'en' prefix)
- French page: `/docs/fr/page` (with 'fr' prefix)

This is breaking language switching functionality on my site.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
