# Bug Report

### Describe the bug

The `remove()` method in `PropertyList` is not working correctly. When trying to remove items from a property list, the method appears to have broken logic that prevents proper removal of elements.

### Reproduction

```js
const propertyList = new PropertyList();
propertyList.add({ key: 'item1', value: 'test1' });
propertyList.add({ key: 'item2', value: 'test2' });
propertyList.add({ key: 'item3', value: 'test3' });

// Try to remove an item
propertyList.remove({ key: 'item2', value: 'test2' }, {});

// The item is not removed properly
console.log(propertyList.count()); // Still shows 3 items instead of 2
```

Also having issues when using a predicate function:

```js
propertyList.remove(item => item.key === 'item2', {});
// Items are not being filtered out as expected
```

### Expected behavior

The `remove()` method should properly remove items from the list that match the predicate or the provided item object. The list should be updated to exclude the removed elements.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
