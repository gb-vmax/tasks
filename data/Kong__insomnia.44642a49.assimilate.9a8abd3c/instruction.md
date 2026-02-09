# Bug Report

### Describe the bug

When using `assimilate()` method on a PropertyList with an array source, the list doesn't get populated correctly. Instead of adding the items from the source array, it appears to be duplicating its own existing items.

### Reproduction

```js
const propertyList = new PropertyList();
propertyList.add(item1);

// Try to assimilate from an array
const sourceArray = [item2, item3, item4];
propertyList.assimilate(sourceArray);

// Expected: propertyList should contain [item1, item2, item3, item4]
// Actual: propertyList contains [item1, item1]
```

### Expected behavior

When calling `assimilate()` with an array source, the method should add all items from the source array to the PropertyList. The list should grow with the new items from the source.

### Additional context

This seems to work fine when the source is another PropertyList object, but breaks when passing a plain array. The issue appeared recently and is blocking our ability to populate PropertyLists from array data.

---
Repository: /testbed
