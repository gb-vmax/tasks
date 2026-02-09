# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with the plugin system when multiple plugins try to load renderer modules simultaneously. The `loadRendererModules()` function seems to have broken concurrent access patterns, causing race conditions or unexpected behavior when plugins attempt to initialize at the same time.

### Reproduction

```js
// Simulate multiple plugins loading concurrently
const plugin1 = app.__private.loadRendererModules();
const plugin2 = app.__private.loadRendererModules();

await Promise.all([plugin1, plugin2]);
```

When multiple plugins call `loadRendererModules()` at nearly the same time, they seem to interfere with each other. Sometimes one of the calls returns incomplete data or the modules aren't properly loaded.

### Expected behavior

Multiple concurrent calls to `loadRendererModules()` should work correctly without race conditions. Each call should either wait for the modules to load or return the already-loaded modules if they're cached.

### Additional context

This wasn't an issue in previous versions. It seems like something changed in how the module loading is handled. The problem is intermittent and seems to depend on timing - sometimes it works fine, other times the modules aren't available when the plugin tries to use them.

---
Repository: /testbed
