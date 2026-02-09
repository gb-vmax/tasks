# Bug Report

### Describe the bug

I'm experiencing some really strange behavior with `PropertyList.add()`. When adding items to a PropertyList, the order of items seems completely unpredictable and doesn't match what I'd expect from a simple list append operation.

### Reproduction

```js
const list = new PropertyList();

list.add(item1);  // Gets added at the end
list.add(item2);  // Gets added at the beginning??
list.add(item3);  // Gets added at the end again
list.add(item4);  // Gets added at the beginning again
```

The items end up in a weird alternating order instead of the order they were added. Also, trying to add the same item twice doesn't work - the second add just gets silently ignored.

### Expected behavior

Items should be added to the end of the list in the order they're added, just like a normal array push. Adding the same item multiple times should either work or throw an error, not silently fail.

### Additional context

This is breaking my scripts where I need to maintain a specific order of properties. The current behavior makes it impossible to predict where items will end up in the list.

---
Repository: /testbed
