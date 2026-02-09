# Bug Report

### Bug with footer translation extraction

I'm experiencing an issue with the footer translations in the classic theme. It seems like the translation file generation is not working correctly for footer content.

### Reproduction

When I have a footer configuration like this:

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
        {
          label: 'API',
          to: '/docs/api',
        },
      ],
    },
  ],
  copyright: 'Copyright © 2024 My Project',
}
```

The translation extraction seems to be inverted - links without labels are being extracted instead of links with labels. Also, the copyright message is not being included in the translation file when it should be.

### Expected behavior

- Footer links with labels should be extracted for translation
- Copyright text should be included in the translation file when present
- Links without labels should be ignored

### System Info

- Docusaurus version: latest
- Theme: @docusaurus/theme-classic

This is blocking our i18n setup as the footer translations are not being generated correctly. Any help would be appreciated!

---
Repository: /testbed
