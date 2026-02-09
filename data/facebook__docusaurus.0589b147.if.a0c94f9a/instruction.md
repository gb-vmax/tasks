# Bug Report

### Describe the bug

When using a category with a `link` of type `doc` in the sidebar configuration, the generated breadcrumb is showing the wrong document. Instead of linking to the correct document ID, it appears to be using the label property instead.

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
      items: ['tutorial']
    }
  ]
}
```

With this configuration, the breadcrumb link for the category is broken. It tries to find a document with an ID matching the label instead of using the actual document ID specified in `link.id`.

### Expected behavior

The breadcrumb should correctly link to the document specified by `link.id` (in this case, 'intro'), not try to use the label as the document ID.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
