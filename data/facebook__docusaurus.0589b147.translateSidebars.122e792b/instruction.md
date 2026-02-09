# Bug Report

### Describe the bug

I'm experiencing an issue with sidebar translations in the docs plugin. When I try to build my site with multiple sidebars, the translation system seems to be passing incorrect data to the translation function. Instead of translating individual sidebar items, it appears to be receiving the entire sidebars object where it should only get a single sidebar.

### Reproduction

```js
// docusaurus.config.js
module.exports = {
  plugins: [
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'docs',
        // ... other config
      },
    ],
  ],
  i18n: {
    defaultLocale: 'en',
    locales: ['en', 'fr'],
  },
};

// sidebars.js
module.exports = {
  tutorialSidebar: [
    {
      type: 'category',
      label: 'Tutorial',
      items: ['intro'],
    },
  ],
  apiSidebar: [
    {
      type: 'category', 
      label: 'API',
      items: ['api-intro'],
    },
  ],
};
```

When building with translations enabled, the sidebar names and sidebar content seem to be swapped during the translation process. This causes the translation system to fail or produce unexpected results.

### Expected behavior

Each sidebar should be translated independently with its correct name and items. The `translateSidebar` function should receive the individual sidebar array and its corresponding name, not the entire sidebars object.

### System Info

- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
