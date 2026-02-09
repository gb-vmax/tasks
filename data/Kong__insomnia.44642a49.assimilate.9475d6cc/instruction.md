# Bug Report

### Describe the bug
When using `assimilate()` method on PropertyList, the behavior seems inverted - passing `prune: false` clears the list and passing `prune: true` keeps existing items. This is the opposite of what would be expected.

### Reproduction
```js
const list = new PropertyList();
list.add(item1);
list.add(item2);

// Expected: keep existing items and add new ones
// Actual: clears existing items before adding new ones
list.assimilate([item3, item4], false);

// Expected: clear existing items and add new ones  
// Actual: keeps existing items and adds new ones
list.assimilate([item3, item4], true);
```

### Expected behavior
When `prune` is `true`, the list should be cleared before assimilating new items. When `prune` is `false` (or not provided), existing items should be preserved and new items should be added to them.

### Additional context
This appears to affect how PropertyList objects merge data from different sources. The current behavior makes it difficult to properly update lists without losing existing data.

---
Repository: /testbed
