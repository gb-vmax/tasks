# Bug Report

### Describe the bug

I'm experiencing an issue with the `keys()` method in the sync store. When calling `keys()` with a prefix, it's not returning nested keys even when I don't explicitly pass `recursive: false`. It seems like the method is always using non-recursive behavior regardless of what I pass in.

### Reproduction

```js
const store = new Store(driver, hooks);

// This should return all nested keys under 'myPrefix/'
const allKeys = await store.keys('myPrefix/');

// Expected: ['myPrefix/foo', 'myPrefix/bar', 'myPrefix/nested/item']
// Actual: Only returns ['myPrefix/foo', 'myPrefix/bar']
```

The nested keys are missing from the results even though they exist in the store. This is breaking my sync functionality because I need to retrieve all keys recursively.

### Expected behavior

When calling `keys(prefix)` without specifying the second parameter, it should default to recursive mode and return all nested keys. When explicitly passing `recursive: true`, it should definitely return all nested keys.

### Additional context

This seems to have started happening recently. I'm using the sync store to manage hierarchical data and rely on the recursive key retrieval to work properly.

---
Repository: /testbed
