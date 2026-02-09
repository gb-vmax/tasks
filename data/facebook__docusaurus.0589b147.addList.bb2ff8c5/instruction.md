# Bug Report

### Describe the bug

When passing `undefined` as a plugin list to the processor, an error is thrown instead of being treated as a no-op. This breaks backward compatibility with code that conditionally passes plugin configurations.

### Reproduction

```js
const processor = unified()

// This should work but throws an error
processor.use(undefined)

// Also fails when undefined is in a plugin array
const plugins = someCondition ? [remarkPlugin] : undefined
processor.use(plugins) // throws TypeError
```

The error message is:
```
TypeError: Expected a list of plugins, not `undefined`
```

### Expected behavior

Passing `undefined` (or `null`) as the plugin list should be handled gracefully and treated as a no-op, similar to how it was handled before. This is useful when conditionally loading plugins based on configuration.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
