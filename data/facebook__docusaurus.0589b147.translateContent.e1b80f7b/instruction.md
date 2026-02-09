# Bug Report

### Describe the bug

When using custom translations for the blog sidebar title, the translation is not being applied correctly. The sidebar always shows the default title instead of the translated version, even when proper translation files are provided.

### Reproduction

1. Set up a Docusaurus site with the blog plugin
2. Configure a custom `blogSidebarTitle` in the plugin options
3. Add a translation file with `sidebar.title` message
4. Build the site with translations enabled

Expected: The translated sidebar title should be displayed
Actual: The default sidebar title from the config is always used, ignoring the translation

### Steps to reproduce

```js
// docusaurus.config.js
{
  plugins: [
    [
      '@docusaurus/plugin-content-blog',
      {
        blogSidebarTitle: 'Default Title',
        // ... other options
      },
    ],
  ],
}

// i18n/[locale]/docusaurus-plugin-content-blog/options.json
{
  "sidebar.title": {
    "message": "Translated Title"
  }
}
```

The sidebar keeps showing "Default Title" instead of "Translated Title".

### Expected behavior

The translation from the translation file should take precedence and override the default sidebar title when available.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
