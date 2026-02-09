# Bug Report

### Describe the bug

Footer translations are not working correctly after a recent update. The footer link items and logo alt text are not being translated properly - they're showing the wrong fallback values.

### Reproduction

Set up a Docusaurus site with footer configuration:

```js
footer: {
  logo: {
    alt: 'My Logo Alt Text',
    src: '/img/logo.svg',
  },
  links: [
    {
      title: 'Docs',
      items: [
        {
          label: 'Getting Started',
          to: '/docs/intro',
        },
      ],
    },
  ],
}
```

Add translation files for the footer, but the translated labels are not being picked up. Instead of using the correct translation keys, it seems like the system is looking for the wrong translation key paths.

### Expected behavior

- Footer link item labels should use the translation key `link.item.label.{label}` 
- Footer logo alt text should fallback to the `alt` property when translation is missing

### Current behavior

The footer appears to be using incorrect translation key paths and wrong fallback properties, causing translations to fail silently and display unexpected values.

### System Info

- Docusaurus version: latest
- Theme: @docusaurus/theme-classic

---
Repository: /testbed
