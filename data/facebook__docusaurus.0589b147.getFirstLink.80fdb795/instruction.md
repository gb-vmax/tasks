# Bug Report

### Describe the bug

I'm encountering an issue with the sidebar utility functions where `getFirstLink` is not working correctly. When trying to get the first link from a sidebar by its ID, the function appears to be receiving incorrect arguments.

### Reproduction

```js
const sidebarUtils = createSidebarsUtils(sidebars);

// Trying to get the first link for a sidebar
const firstLink = sidebarUtils.getFirstLink('docs');
```

The function call fails because it seems like the arguments being passed to the underlying `getFirstLink` function are wrong. Instead of receiving the expected parameters, it's only getting a single sidebar object.

### Expected behavior

The `getFirstLink` function should properly receive both the sidebars collection and the sidebar ID to correctly retrieve the first link from the specified sidebar.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
