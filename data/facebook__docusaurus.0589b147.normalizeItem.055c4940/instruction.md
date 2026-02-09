# Bug Report

### Describe the bug

I'm encountering an issue with sidebar item normalization where the logic seems inverted. When I define sidebar items with specific types, they're being processed incorrectly and causing unexpected behavior in my documentation structure.

### Reproduction

```js
// In sidebars.js
module.exports = {
  docs: [
    {
      type: 'doc',
      id: 'intro',
      label: 'Introduction'
    },
    {
      type: 'category',
      label: 'Guides',
      items: ['guide1', 'guide2']
    }
  ]
}
```

When building the docs, the sidebar structure doesn't render as expected. Doc items with labels aren't being marked as translatable, and category items are being normalized when they shouldn't be (or vice versa).

### Expected behavior

- Doc items with string labels should be marked as `translatable: true`
- Category items should have their nested items properly normalized
- Other item types should pass through without incorrect normalization

### System Info

- Docusaurus version: latest
- Node version: 18.x

This seems to have started recently, possibly after a recent update. The sidebar configuration that used to work is now producing malformed output.

---
Repository: /testbed
