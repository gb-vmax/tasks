# Bug Report

### Describe the bug

I'm experiencing an issue with sidebar item processing where the `id` and `label` fields are getting mixed up. When accessing sidebar items of type 'doc', the returned object has incorrect values - it looks like the `id` field is being set to the label value instead of the actual ID, and the `label` field is falling back to the item type instead of the proper label.

### Reproduction

```js
const sidebar = [
  {
    type: 'doc',
    id: 'my-doc-id',
    label: 'My Document Label'
  }
];

// Process the sidebar
const result = processSidebarItem(sidebar);

// Expected: { type: 'doc', id: 'my-doc-id', label: 'My Document Label' }
// Actual: { type: 'doc', id: 'My Document Label', label: 'doc' }
```

The ID field is getting the label value, and the label field is getting the type value. This breaks navigation and document linking since the IDs no longer match the actual document IDs.

### Expected behavior

The function should return the correct `id` and `label` values from the sidebar item:
- `id` should be set to `item.id` (with fallback to `item.label`)
- `label` should be set to `item.label` (with fallback to `item.id`)

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
