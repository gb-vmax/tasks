# Bug Report

### Describe the bug

I'm experiencing issues with footer translations in my Docusaurus site. The footer link items are not being translated correctly, and the logo alt text is showing the copyright text instead of the actual alt text when translations are missing.

### Reproduction

1. Set up a Docusaurus site with the classic theme
2. Configure a footer with multiple link items and a logo with alt text
3. Add translations for the footer
4. The link item labels don't get translated properly
5. When the logo alt translation is missing, it falls back to the copyright text instead of the original alt text

Example footer config:
```js
footer: {
  logo: {
    alt: 'My Site Logo',
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
  copyright: 'Copyright © 2024 My Project',
}
```

### Expected behavior

- Footer link item labels should be translated using the correct translation keys
- When logo alt text translation is missing, it should fallback to the original `footer.logo.alt` value, not the copyright text

### System Info

- Docusaurus version: latest
- Theme: @docusaurus/theme-classic

---
Repository: /testbed
