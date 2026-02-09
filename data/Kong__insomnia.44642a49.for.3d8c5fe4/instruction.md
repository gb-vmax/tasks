# Bug Report

### Describe the bug

I'm experiencing an issue with the store deserialization logic where hook filtering isn't working as expected. When I have hooks with `supportedExtensions` defined, they're supposed to only run for specific file extensions, but it seems like the extension matching logic has some problems.

### Reproduction

```js
const store = new Store();

// Add a hook that should only process .json files
store.addHook({
  supportedExtensions: ['json'],
  read: async (ext, value) => {
    // Transform logic here
    return value;
  }
});

// Try to deserialize a .yaml file
await store._deserialize('.yaml', Buffer.from('test: data'));

// The hook runs even though it shouldn't apply to .yaml files
```

Also noticed that when using extensions without the leading dot in `supportedExtensions` (like `['json']` instead of `['.json']`), the matching doesn't work correctly.

### Expected behavior

Hooks with `supportedExtensions` should only be applied to files with matching extensions. The matching should work whether the extension in `supportedExtensions` has a leading dot or not.

### Additional context

This seems to have broken after some recent changes to the deserialization code. The hook metadata tracking also appears to be storing data in a way that might cause memory issues since it's using WeakMap on Buffer objects.

---
Repository: /testbed
