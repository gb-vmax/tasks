# Bug Report

### Describe the bug

I'm experiencing an issue where localized pages are not being loaded correctly. When I have both a default page and a localized version of the same page, only the default version appears to be processed, and the localized content is ignored.

### Reproduction

1. Set up a Docusaurus site with i18n enabled
2. Create a page in the default locale (e.g., `src/pages/mypage.md`)
3. Create a localized version (e.g., `i18n/fr/docusaurus-plugin-content-pages/mypage.md`)
4. Build or start the dev server
5. Navigate to the French locale version

### Expected behavior

Both the default and localized versions of the page should be available. When viewing the site in French, the localized content from `i18n/fr/docusaurus-plugin-content-pages/mypage.md` should be displayed instead of the default content.

### Actual behavior

The localized page content is not being picked up. Only the default locale content is shown regardless of which locale is selected.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
