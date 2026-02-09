# Bug Report

### Describe the bug

I'm encountering an issue with `getFirstLink` function when trying to get the first link from a sidebar. It seems like the function is receiving the wrong argument and returns unexpected results.

When calling `getFirstLink(id)` where `id` is a sidebar identifier, the function doesn't work as expected. Instead of getting the first link from the specific sidebar, it appears to be processing the entire sidebars object incorrectly.

### Reproduction

```js
const sidebars = {
  docs: [
    { type: 'doc', id: 'intro' },
    { type: 'doc', id: 'tutorial' }
  ],
  api: [
    { type: 'doc', id: 'api-reference' }
  ]
};

// Trying to get the first link from 'docs' sidebar
const firstLink = getFirstLink('docs');
// Returns unexpected result or throws an error
```

### Expected behavior

`getFirstLink('docs')` should return the first link from the 'docs' sidebar (e.g., 'intro'), not process the entire sidebars object.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
