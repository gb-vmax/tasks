# Bug Report

### Describe the bug

I'm experiencing an issue with localized base URLs in my Docusaurus site. The URLs being generated for alternate language versions are malformed - specifically, the trailing slashes are appearing in the wrong places.

For the default locale, the base URL is missing a trailing slash, while for non-default locales, there's an extra trailing slash being added after the locale code.

### Reproduction

When I have a multi-language site configured with:
- Default locale: `en`
- Other locales: `fr`, `es`
- Base URL: `/docs/`

The generated alternate URLs look like:
- English (default): `/docs` (missing trailing slash)
- French: `/docsfr` (locale code concatenated directly)
- Spanish: `/docses` (locale code concatenated directly)

### Expected behavior

The URLs should be properly formatted as:
- English (default): `/docs/`
- French: `/docs/fr/`
- Spanish: `/docs/es/`

This is affecting the `<link rel="alternate">` tags in the HTML head, which impacts SEO and language switching functionality.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
