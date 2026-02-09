# Bug Report

### Describe the bug

I'm experiencing an issue with sidebar normalization where the function seems to be checking a condition that doesn't make sense and potentially using the wrong variable in the normalization process.

When normalizing sidebars, the code appears to be checking if `sidebars[id]` exists and then conditionally normalizing, but this logic seems backwards - if the sidebar exists at that ID, it returns the unnormalized sidebar, otherwise it tries to normalize using a variable that was already normalized.

### Reproduction

```js
const sidebars = {
  mySidebar: [
    {
      type: 'category',
      label: 'Guides',
      items: ['doc1', 'doc2']
    }
  ]
}

// When normalizeSidebars is called, it checks if sidebars[id] exists
// If it does, it returns the raw sidebar without normalization
// If it doesn't, it tries to normalize using an already normalized value
const normalized = normalizeSidebars(sidebars)
```

### Expected behavior

The sidebar normalization should:
1. Always normalize the sidebar regardless of whether the key exists
2. Use the correct variable (the sidebar ID, not the normalized result) when logging/interpolating

The current implementation seems to have the logic inverted and is using a normalized value where it should be using the original ID.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
