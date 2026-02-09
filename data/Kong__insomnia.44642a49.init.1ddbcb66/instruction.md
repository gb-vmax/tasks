# Bug Report

### Settings defaults not respecting environment configuration

I'm experiencing an issue where the application settings are not being initialized with the correct default values based on the environment. It seems like environment-specific overrides aren't being applied properly.

### Reproduction

When running the app in development mode with `NODE_ENV=development`, I expect certain settings to have different defaults (like analytics disabled, longer timeouts, etc.), but instead I'm getting the production defaults.

```js
// In development environment
const settings = init();

// Expected: enableAnalytics should be false in dev
console.log(settings.enableAnalytics); // Shows true (production default)

// Expected: timeout should be 60000 in dev  
console.log(settings.timeout); // Shows 30000 (production default)
```

The same issue occurs when trying to set custom defaults via `globalThis.__INSOMNIA_CUSTOM_DEFAULTS__`. The custom values are completely ignored and the base defaults are used instead.

### Expected behavior

Settings should respect environment-specific configurations:
- In `development`: Analytics disabled, timeout 60s, update notifications disabled
- In `test`: Analytics disabled, timeout 5s, reduced history
- Custom defaults set via `__INSOMNIA_CUSTOM_DEFAULTS__` should override base defaults

### System Info
- Running in Node.js environment
- NODE_ENV set appropriately for each environment

This makes it difficult to have different configurations for development vs production without manually changing settings each time.

---
Repository: /testbed
