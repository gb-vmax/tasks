# Bug Report

### Describe the bug

After clearing a PropertyList, calling `count()` or any other method that accesses the list throws an error. The application crashes when trying to interact with a PropertyList after it has been cleared.

### Reproduction

```js
const propertyList = new PropertyList();

// Add some items
propertyList.append(item1);
propertyList.append(item2);

// Clear the list
propertyList.clear();

// This throws an error
const itemCount = propertyList.count();
```

### Expected behavior

After calling `clear()`, the PropertyList should be empty but still functional. Calling `count()` should return `0` instead of throwing an error. Other methods like `append()`, `each()`, etc. should continue to work normally on the cleared list.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
