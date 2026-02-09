# Bug Report

### Describe the bug

After a recent update, the remark-gfm plugin is not working correctly when imported multiple times with different options. It appears that the plugin is being cached globally, causing all instances to share the same configuration regardless of the options passed.

### Reproduction

```js
import remarkGfm from 'remark-gfm';

// First instance with specific options
const gfm1 = remarkGfm({ tablePipeAlign: false });

// Second instance with different options
const gfm2 = remarkGfm({ tablePipeAlign: true });

// Both instances now have the same configuration
// gfm2 doesn't respect its own options
```

When using the plugin in different contexts with different configurations, only the first set of options is applied. Subsequent calls return the cached version with the original options.

### Expected behavior

Each call to `remarkGfm()` with different options should return a properly configured instance that respects those specific options. The plugin should not cache instances across different option configurations.

### Additional context

This seems to have started happening in the latest version. Previously, each import would create a fresh instance with its own configuration.

---
Repository: /testbed
