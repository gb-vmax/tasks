# Bug Report

### Describe the bug

After a recent update, sidebar translations are not working correctly when there are multiple sidebars defined. Only the first sidebar appears to be getting translated, while additional sidebars remain untranslated.

### Reproduction

```js
// docusaurus.config.js
module.exports = {
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
        },
      },
    ],
  ],
};

// sidebars.js
module.exports = {
  tutorialSidebar: [
    {
      type: 'category',
      label: 'Getting Started',
      items: ['intro'],
    },
  ],
  apiSidebar: [
    {
      type: 'category', 
      label: 'API Reference',
      items: ['api'],
    },
  ],
};
```

When running `docusaurus write-translations`, the translation files are generated but when building the site, only the first sidebar (`tutorialSidebar`) gets translated properly. The second sidebar (`apiSidebar`) shows the original English labels instead of the translated ones.

### Expected behavior

All defined sidebars should be translated correctly when translation files are provided. Both `tutorialSidebar` and `apiSidebar` should use their respective translations.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
