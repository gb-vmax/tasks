# Bug Report

### Describe the bug

When using a category with a linked doc in the sidebar configuration, the label and id are being swapped. The category's label is being used as the doc id, and the link's doc id is being used as the label.

### Reproduction

```js
// sidebars.js
module.exports = {
  docs: [
    {
      type: 'category',
      label: 'Getting Started',
      link: {
        type: 'doc',
        id: 'intro'
      },
      items: []
    }
  ]
}
```

When this sidebar configuration is processed, the resulting link has:
- `id: 'Getting Started'` (should be `'intro'`)
- `label: 'intro'` (should be `'Getting Started'`)

### Expected behavior

The category link should correctly map the doc id and label:
- `id` should be set to `item.link.id` (e.g., `'intro'`)
- `label` should be set to `item.label` (e.g., `'Getting Started'`)

This causes broken links in the sidebar because it's trying to find a document with id "Getting Started" instead of "intro".

---
Repository: /testbed
