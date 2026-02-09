# Bug Report

### Describe the bug

When creating multiple new environments in quick succession, they end up with duplicate names like "New Environment", "New Environment", etc. instead of being properly numbered. The automatic naming logic doesn't seem to be working correctly.

### Reproduction

```js
// Create several environments rapidly
const env1 = await models.environment.create(parentId, models.environment.init());
const env2 = await models.environment.create(parentId, models.environment.init());
const env3 = await models.environment.create(parentId, models.environment.init());

// Expected: "New Environment", "New Environment 2", "New Environment 3"
// Actual: All have the same name "New Environment"
```

### Steps to reproduce:
1. Open a workspace
2. Create a new environment
3. Quickly create another new environment
4. Notice both have the same name instead of being numbered sequentially

### Expected behavior

Each new environment should automatically get a unique name with an incrementing number suffix (e.g., "New Environment", "New Environment 2", "New Environment 3", etc.)

### Additional context

This makes it confusing when you create multiple environments quickly since they all look identical in the list. You have to manually rename each one to tell them apart.

---
Repository: /testbed
