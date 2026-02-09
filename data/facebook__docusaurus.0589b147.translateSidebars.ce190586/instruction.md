# Bug Report

### Describe the bug

After a recent update, the sidebar translations are not working properly. The translated sidebars seem to be returned as an array instead of an object, which breaks the sidebar rendering.

### Reproduction

When using the docs plugin with multiple sidebars and translations enabled:

```js
// docusaurus.config.js
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

With sidebars.js containing multiple named sidebars:
```js
module.exports = {
  tutorialSidebar: [
    // items...
  ],
  apiSidebar: [
    // items...
  ],
};
```

The sidebars object structure gets corrupted and returns an array-like structure instead of maintaining the object with sidebar names as keys.

### Expected behavior

The `translateSidebars` function should return an object with the same structure as the input - sidebar names as keys mapping to their translated sidebar content. The translated sidebars should maintain the original object structure so that sidebars can be accessed by their names.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
