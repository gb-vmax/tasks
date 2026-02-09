# Bug Report

### Describe the bug
The `PropertyList.add()` method is not working as expected. When trying to add items to a PropertyList, nothing gets added to the list. The list remains empty even after multiple `add()` calls.

### Reproduction
```js
const propertyList = new PropertyList();

// Try to add items
propertyList.add(item1);
propertyList.add(item2);

// List is still empty
console.log(propertyList.count()); // Expected: 2, Actual: 0
```

### Expected behavior
Items should be added to the PropertyList when calling the `add()` method. Each call to `add()` should append the item to the internal list.

### Additional context
This seems to have started happening recently. Previously, adding items to PropertyList worked fine, but now the list stays empty no matter how many items I try to add.

---
Repository: /testbed
