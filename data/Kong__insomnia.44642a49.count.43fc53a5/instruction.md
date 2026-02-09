# Bug Report

### Describe the bug

The `count()` method on `PropertyList` is returning incorrect values. When I have a list with items, the count is always one less than the actual number of items in the list.

### Reproduction

```js
const list = new PropertyList();
list.add({ key: 'item1', value: 'value1' });
list.add({ key: 'item2', value: 'value2' });
list.add({ key: 'item3', value: 'value3' });

console.log(list.count()); // Returns 2, but should return 3
```

When I add 3 items to a PropertyList, calling `count()` returns 2 instead of 3. Similarly, if I add 5 items, it returns 4.

### Expected behavior

The `count()` method should return the actual number of items in the list. If there are 3 items, it should return 3, not 2.

### Additional context

This seems to have started happening recently. The count is consistently off by one for any non-empty list.

---
Repository: /testbed
