# Bug Report

### Describe the bug
When using `insertAfter()` on a PropertyList, the method doesn't accept string or object references to specify the position. Currently it only works with numeric indices, which makes it difficult to insert items after a specific property when you only have its ID or reference.

### Reproduction
```js
const list = new PropertyList();
list.append({ id: 'item1', name: 'First' });
list.append({ id: 'item2', name: 'Second' });

// This doesn't work - need to use string ID
list.insertAfter({ id: 'item3', name: 'Third' }, 'item1');

// This also doesn't work - need to use object reference
const firstItem = list.get('item1');
list.insertAfter({ id: 'item3', name: 'Third' }, firstItem);

// Only numeric index works currently
list.insertAfter({ id: 'item3', name: 'Third' }, 0);
```

### Expected behavior
The `insertAfter()` method should accept:
- Numeric index (current behavior)
- String ID to identify the item
- Object reference to the item

This would make it consistent with other methods in the SDK that accept multiple types of references.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
