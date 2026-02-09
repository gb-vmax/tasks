# Bug Report

### Describe the bug

I'm experiencing an issue where plugin timing labels are not being captured correctly. When I enable timing for plugins, the timer labels appear to be undefined or incorrect, making it impossible to properly identify which plugin hook is being timed.

### Reproduction

```js
// Create a plugin with a named hook
const myPlugin = {
  name: 'my-custom-plugin',
  buildStart() {
    // some logic here
  }
}

// When timing is enabled, the timer label should be:
// "plugin 0 (my-custom-plugin) - buildStart"
// But it seems to be undefined or not set correctly
```

### Expected behavior

The timer labels should be properly set before the handler function is called, showing the correct plugin index, name, and hook name. This worked fine in previous versions.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
