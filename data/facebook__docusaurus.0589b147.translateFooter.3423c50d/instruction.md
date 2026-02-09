# Bug Report

### Describe the bug

Footer link titles are not being translated correctly. The translation keys appear to be wrong - instead of using `link.title.*` keys, the code is looking for `link.item.label.*` keys which don't match the expected translation file structure.

### Reproduction

1. Set up a Docusaurus site with the classic theme
2. Configure footer links in `docusaurus.config.js`:
```js
footer: {
  links: [
    {
      title: 'Docs',
      items: [
        {
          label: 'Tutorial',
          to: '/docs/intro',
        },
      ],
    },
  ],
}
```
3. Create translation files with the expected key format:
```json
{
  "theme.footer.link.title.Docs": {
    "message": "Documentation"
  }
}
```
4. The footer title still shows "Docs" instead of "Documentation"

### Expected behavior

Footer link titles should be translated using the `link.title.*` translation keys as defined in the translation files. The title should display the translated message when available.

### System Info
- Docusaurus version: latest
- Theme: @docusaurus/theme-classic

---
Repository: /testbed
