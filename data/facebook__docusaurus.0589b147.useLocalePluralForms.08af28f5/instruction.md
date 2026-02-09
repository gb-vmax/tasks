# Bug Report

### Describe the bug

The `usePluralForm` hook is causing an infinite loop or continuous re-rendering in my Docusaurus site. The browser becomes unresponsive and I see the CPU usage spike to 100%. This seems to be happening when the locale plural forms are being initialized.

### Reproduction

I noticed this issue when:
1. Starting the Docusaurus dev server
2. Navigating to any page that uses plural forms (like blog post counts, tag counts, etc.)
3. The page becomes unresponsive and keeps re-rendering

The issue appears to be related to how the plural forms are being memoized. It seems like the dependency array might not be working correctly, causing the hook to recalculate on every render instead of only when the locale changes.

### Expected behavior

The plural form utility should only recalculate when the current locale actually changes, not on every render. The page should load normally without any performance issues.

### System Info
- Docusaurus version: latest
- Node version: 18.x
- Browser: Chrome

This is blocking my development work as the site is completely unusable in this state. Any help would be appreciated!

---
Repository: /testbed
