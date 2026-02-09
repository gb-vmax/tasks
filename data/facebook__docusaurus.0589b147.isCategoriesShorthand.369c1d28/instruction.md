# Bug Report

### Describe the bug

I'm experiencing an issue with sidebar configuration parsing. When using certain sidebar item configurations, the system is incorrectly identifying them as category shorthand syntax, which causes unexpected behavior in the sidebar rendering.

### Reproduction

```js
const sidebarConfig = {
  docs: [
    {
      type: 'category',
      label: 'My Category',
      items: ['doc1', 'doc2']
    }
  ]
}
```

When I use this configuration, items that have an explicit `type` property are being treated as if they were using the shorthand syntax. This seems to happen with any object that has a `type` field defined.

### Expected behavior

The sidebar should correctly distinguish between:
- Category shorthand syntax (objects without a `type` property)
- Explicit sidebar item configurations (objects with a `type` property)

Only items without an explicit `type` should be treated as shorthand syntax.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
