# Bug Report

### Describe the bug

Footer translations are not working correctly - the translation keys seem to be swapped. When I try to translate footer link titles and item labels, the translations don't get applied properly. 

### Reproduction

Setup a footer configuration with multi-column links and try to translate them:

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

Add translations in your locale file:
```json
{
  "theme.footer.link.title.Docs": "Documentation",
  "theme.footer.link.item.label.Tutorial": "Getting Started"
}
```

### Expected behavior

The footer should display "Documentation" as the column title and "Getting Started" as the link label.

### Actual behavior

The translations are not being applied. The original text "Docs" and "Tutorial" still show up instead of the translated versions.

Also noticed that the footer logo alt text translation has the fallback order reversed - it's checking the original alt text before falling back to the translation, which seems backwards.

---
Repository: /testbed
