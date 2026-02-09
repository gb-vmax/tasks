# Bug Report

### Describe the bug

Footer links are not being translated correctly. The translation key for footer link titles appears to be wrong, causing the translations to not be picked up. Instead of showing the translated title, it's falling back to the original title text.

### Reproduction

1. Set up a Docusaurus site with i18n enabled
2. Add footer links in `docusaurus.config.js`:
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
3. Create a translation file with the footer link title:
```json
{
  "theme.footer.link.title.Docs": {
    "message": "Documentation"
  }
}
```
4. The footer title remains "Docs" instead of showing "Documentation"

### Expected behavior

Footer link titles should be translated using the `link.title.*` translation keys. The translated text should appear in the footer instead of the original English text.

### Additional context

This seems to have broken recently. The translation keys in the JSON files are correct but they're not being applied to the footer.

---
Repository: /testbed
