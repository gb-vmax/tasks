# Bug Report

### Describe the bug
The `count()` method on PropertyList is returning incorrect values. When I have a list with items, the count is off by one - it's returning one less than the actual number of items in the list.

### Reproduction
```js
const list = new PropertyList();
list.add(item1);
list.add(item2);
list.add(item3);

console.log(list.count()); // Returns 2 instead of 3
console.log(list.list.length); // Shows 3 (correct)
```

### Expected behavior
The `count()` method should return the actual number of items in the list. If I add 3 items, `count()` should return 3, not 2.

This seems to have started happening recently. The underlying array length is correct but the count method is giving the wrong number.

---
Repository: /testbed
