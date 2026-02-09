# Bug Report

### Describe the bug

I'm encountering an issue with the remark processor when passing `null` or `undefined` as a plugin list. The behavior seems to have changed - previously it would silently skip null/undefined plugin lists, but now it's throwing a TypeError.

### Reproduction

```js
const processor = remark();

// This now throws an error but used to work fine
processor.use(null);

// Same issue with undefined
processor.use(undefined);
```

The error message is:
```
TypeError: Expected a list of plugins, not `null`
```

### Expected behavior

When passing `null` or `undefined` to `.use()`, it should be treated as a no-op and not throw an error. This is useful when conditionally adding plugins:

```js
processor.use(someCondition ? myPlugin : null);
```

This pattern used to work in previous versions and now breaks existing code.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
