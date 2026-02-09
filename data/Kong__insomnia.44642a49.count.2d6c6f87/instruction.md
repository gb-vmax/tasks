# Bug Report

### Describe the bug

I'm experiencing an issue with the `PropertyList` class where the `count()` method is returning incorrect values. When I have a list with items, the count is off by one - it's returning one less than the actual number of items in the list.

### Reproduction

```js
const propertyList = new PropertyList();
propertyList.add(item1);
propertyList.add(item2);
propertyList.add(item3);

console.log(propertyList.count()); // Expected: 3, but getting: 2
```

### Expected behavior

The `count()` method should return the exact number of items in the list. If I add 3 items, it should return 3, not 2.

### Additional context

This seems to have started recently. The count is consistently one less than expected for any non-empty list. For empty lists it correctly returns 0, but for any list with items the count is wrong.

---
Repository: /testbed
