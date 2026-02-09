# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with plugin renderer modules not loading correctly. The application seems to be caching React and ReactDOM modules indefinitely, and when the app version changes or when I try to force a reload, the old cached modules are still being used instead of fresh ones.

### Reproduction

This happens when:
1. A plugin tries to load renderer modules through `app.__private.loadRendererModules()`
2. The app version gets updated
3. The modules should be invalidated and reloaded, but the stale cached versions are still returned

I noticed this particularly affects plugins that rely on getting fresh React/ReactDOM instances after updates.

### Expected behavior

When the app version changes or when `__INSOMNIA_INVALIDATE_MODULE_CACHE__` is set to true, the module cache should be cleared and fresh modules should be loaded on the next call to `loadRendererModules()`. Currently, it seems like the cache invalidation logic isn't working as intended.

### System Info
- Insomnia version: latest
- OS: macOS

Has anyone else run into this? It's causing some weird behavior with plugins after app updates.

---
Repository: /testbed
