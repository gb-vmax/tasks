# Bug Report

### Describe the bug

When creating multiple new environments, they all get assigned the same name "New Environment" instead of being numbered sequentially. This makes it confusing to distinguish between different environments in the UI.

### Reproduction

```js
// Create first environment
const env1 = models.environment.init();
console.log(env1.name); // Expected: "New Environment", Actual: "New Environment"

// Create second environment
const env2 = models.environment.init();
console.log(env2.name); // Expected: "New Environment 2", Actual: "New Environment"

// Create third environment
const env3 = models.environment.init();
console.log(env3.name); // Expected: "New Environment 3", Actual: "New Environment"
```

All environments end up with the same name, which causes issues when trying to identify them in dropdowns or lists.

### Expected behavior

Each new environment should automatically get a unique name with an incrementing number suffix:
- First: "New Environment"
- Second: "New Environment 2"
- Third: "New Environment 3"
- etc.

This is similar to how other apps handle duplicate names (e.g., "Copy of Document", "Copy of Document 2", etc.)

### Additional context

Also noticed that all new environments have `color: null` which makes them harder to visually distinguish. It would be nice if they got assigned different colors automatically from a palette.

---
Repository: /testbed
