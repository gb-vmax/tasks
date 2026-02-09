# Bug Report

### Describe the bug

I'm experiencing an issue with footer link translations in the classic theme. When I configure multi-column footer links with titles, the translation files are not being generated correctly. It seems like links with titles are being excluded from the translation extraction process.

### Reproduction

```js
// docusaurus.config.js
module.exports = {
  themeConfig: {
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
        {
          title: 'Community',
          items: [
            {
              label: 'Discord',
              href: 'https://discord.gg/example',
            },
          ],
        },
      ],
    },
  },
};
```

After running the translation extraction, the footer link titles ('Docs', 'Community') are missing from the generated translation files. Only links WITHOUT titles seem to be included, which is the opposite of what should happen.

### Expected behavior

Footer links that have a `title` property should be included in the translation file generation so that the titles can be properly translated. Currently it appears that only links without titles are being processed.

### System Info

- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

This is blocking our internationalization efforts as we can't translate the footer section titles properly.

---
Repository: /testbed
