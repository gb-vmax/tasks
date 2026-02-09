# Bug Report

### Describe the bug

I'm experiencing an issue with duplicating documents that have names. When duplicating a document multiple times, the naming pattern breaks and produces incorrect copy numbers.

### Reproduction

```js
// Start with a document named "My Request"
const original = { name: "My Request", type: "request", parentId: "workspace_1" };

// First duplicate should be "My Request (Copy)"
const firstCopy = await database.duplicate(original);
console.log(firstCopy.name); // Expected: "My Request (Copy)"

// Second duplicate should be "My Request (Copy 2)"
const secondCopy = await database.duplicate(original);
console.log(secondCopy.name); // Expected: "My Request (Copy 2)"

// But the naming seems to get confused when there are existing copies
```

Also, if I have a document named "Test (Copy)" and try to duplicate it, the new name doesn't follow the expected pattern.

### Expected behavior

- First duplicate: "Original Name (Copy)"
- Second duplicate: "Original Name (Copy 2)"
- Third duplicate: "Original Name (Copy 3)"
- And so on...

The duplicate naming should strip any existing "(Copy)" or "(Copy N)" suffix from the base name and then calculate the next available copy number correctly by looking at all siblings with the same parent.

### System Info
- Insomnia version: latest
- OS: macOS

This seems related to how the duplicate function generates names for copied documents. The regex pattern or the copy number calculation might not be working as intended.

---
Repository: /testbed
