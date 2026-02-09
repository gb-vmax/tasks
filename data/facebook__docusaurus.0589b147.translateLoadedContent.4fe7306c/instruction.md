# Bug Report

### Describe the bug

After a recent update, the translation system for docs is broken. When trying to use translations with the docs plugin, I'm getting errors about translation files not being found or applied correctly.

It seems like the translation file mapping is not working as expected - the system can't match translation files to their corresponding content anymore.

### Reproduction

```js
// In docusaurus.config.js
module.exports = {
  plugins: [
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'docs',
        path: 'docs',
        // ... other config
      },
    ],
  ],
  i18n: {
    defaultLocale: 'en',
    locales: ['en', 'fr'],
  },
};
```

Steps:
1. Set up a docs site with i18n enabled
2. Add translation files for docs content
3. Build or start the site
4. Translation files are not being matched/loaded properly

### Expected behavior

Translation files should be correctly mapped by their file path and applied to the loaded content. The translated versions of docs should be available when switching locales.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
