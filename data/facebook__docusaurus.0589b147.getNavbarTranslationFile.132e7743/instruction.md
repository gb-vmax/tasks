# Bug Report

### Describe the bug

Navbar item labels are not being extracted for translation. When building a Docusaurus site with internationalization enabled, the navbar items don't appear in the translation files, making it impossible to translate navigation menu labels.

### Reproduction

```js
// docusaurus.config.js
module.exports = {
  themeConfig: {
    navbar: {
      items: [
        {
          type: 'doc',
          docId: 'intro',
          label: 'Docs',
        },
        {
          label: 'Blog',
          to: '/blog',
        },
        {
          label: 'About',
          items: [
            {
              label: 'Team',
              to: '/team',
            },
            {
              label: 'Contact',
              to: '/contact',
            },
          ],
        },
      ],
    },
  },
};
```

After running the translation extraction, the navbar labels like "Docs", "Blog", "About", "Team", and "Contact" are missing from the generated translation files. This means these labels cannot be translated to other languages.

### Expected behavior

All navbar item labels (including nested items in dropdown menus) should be included in the translation files so they can be translated. The translation keys should be generated for both top-level and nested navbar items.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
