# Bug Report

### Describe the bug

I'm experiencing an issue with the cookie jar functionality in templating extensions. When accessing `getOrCreateForWorkspace`, there seems to be a problem with the scope of the cache variable. The code appears to have a `_cookieJarCache` WeakMap declared outside of the proper scope, which is causing unexpected behavior.

### Reproduction

```js
// In a template extension context
const workspace = {
  _id: 'wrk_123',
  name: 'My Workspace'
};

// Try to get or create cookie jar for workspace
const cookieJar = await context.store.cookieJar.getOrCreateForWorkspace(workspace);

// The cache variable seems to be in the wrong scope
// causing issues with the function execution
```

### Expected behavior

The `getOrCreateForWorkspace` function should properly cache cookie jars per workspace and return the correct cookie jar instance. The cache should be scoped correctly within the cookieJar object definition.

### System Info
- Insomnia version: latest
- Platform: N/A

The indentation and structure of the code looks off - it seems like the `_cookieJarCache` declaration got placed outside the object structure where it should be. This is breaking the cookieJar functionality.

---
Repository: /testbed
