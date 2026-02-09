# Bug Report

### Describe the bug

I'm encountering an issue with `PropertyList.clear()` method. After calling `clear()` on a PropertyList instance, subsequent operations like `count()` or iterating over the list throw errors because the internal list becomes undefined instead of an empty array.

### Reproduction

```js
const propertyList = new PropertyList();

// Add some properties
propertyList.add({ key: 'test1', value: 'value1' });
propertyList.add({ key: 'test2', value: 'value2' });

// Clear the list
propertyList.clear();

// This throws an error: Cannot read property 'length' of undefined
const count = propertyList.count();
```

### Expected behavior

After calling `clear()`, the PropertyList should be empty but still functional. Methods like `count()` should return 0, and the list should be ready to accept new items without errors.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
