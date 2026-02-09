# Bug Report

### Describe the bug

I'm experiencing an issue with plugin logging where logs are being duplicated or appearing in the wrong plugins. When multiple plugins use the `onLog` hook, it seems like the log messages are being passed to plugins that should have been skipped.

### Reproduction

```js
const plugin1 = {
  name: 'plugin-1',
  onLog(level, log) {
    console.log('Plugin 1 received:', log.message);
  }
};

const plugin2 = {
  name: 'plugin-2',
  onLog(level, log) {
    console.log('Plugin 2 received:', log.message);
    // This triggers a new log
    this.warn('Secondary log from plugin 2');
  }
};

// When plugin2 logs, plugin1 also receives the message
// even though it should be skipped
```

### Expected behavior

When a plugin triggers a log from within its own `onLog` handler, that log should only be sent to other plugins, not back to itself or to plugins that have already processed the original log. The skipped plugins set should be properly maintained across the chain.

### System Info

- Rollup version: latest
- Node version: 18.x

This seems like it might be related to how the skipped plugins are being tracked when logs are forwarded between plugins.

---
Repository: /testbed
