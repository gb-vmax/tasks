# Bug Report

### Describe the bug

After a recent update, I'm experiencing intermittent failures when plugins try to load React/ReactDOM modules. The plugin renderer context seems to be caching modules and retrying failed imports, but this is causing issues in my plugin development workflow.

When I reload my plugin multiple times in quick succession, sometimes the modules fail to load properly even though they're available. The behavior is inconsistent - sometimes it works fine, other times the plugin just doesn't render anything.

### Reproduction

1. Create a custom plugin that uses the app context's renderer modules
2. Call `context.app.__private.loadRendererModules()` multiple times rapidly
3. Observe that subsequent calls may return cached modules even if the initial load had issues
4. The plugin UI fails to render correctly in some cases

Example plugin code:
```js
module.exports.requestHooks = [
  async context => {
    const modules = await context.app.__private.loadRendererModules();
    // modules might be an empty object {} even when React/ReactDOM are available
    console.log(modules); // Sometimes empty, sometimes populated
  }
];
```

### Expected behavior

The module loading should be consistent and reliable. If modules are available, they should always be loaded successfully without needing retry logic or caching that might mask underlying issues.

### System Info
- Insomnia version: latest
- OS: macOS
- Plugin development environment

---
Repository: /testbed
