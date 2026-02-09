# Bug Report

### Describe the bug

The `count()` method on `PropertyList` is returning an incorrect value. When I have a list with items, the count is off by one - it's returning one less than the actual number of items in the list.

### Reproduction

```js
const propertyList = new PropertyList();
propertyList.add(item1);
propertyList.add(item2);
propertyList.add(item3);

console.log(propertyList.count()); // Returns 2, but should return 3
```

If I add 5 items to a PropertyList and call `count()`, I expect it to return 5, but instead it returns 4. This is causing issues in my code where I need to know the actual number of items in the list.

### Expected behavior

`count()` should return the actual number of items in the list. If there are 3 items, it should return 3, not 2.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
