# Bug Report

### Describe the bug

When creating multiple proto files in sequence, they all end up with the same default name "New Proto File" instead of getting unique names like "New Proto File 2", "New Proto File 3", etc.

### Reproduction

```js
// Create multiple proto files
const file1 = init();
const file2 = init();
const file3 = init();

console.log(file1.name); // Expected: "New Proto File", Actual: "New Proto File"
console.log(file2.name); // Expected: "New Proto File 2", Actual: "New Proto File"
console.log(file3.name); // Expected: "New Proto File 3", Actual: "New Proto File"
```

All files get the same default name, which makes it confusing when you have multiple proto files in your workspace.

### Expected behavior

Each newly created proto file should have a unique default name:
- First file: "New Proto File"
- Second file: "New Proto File 2"
- Third file: "New Proto File 3"
- And so on...

This is similar to how other editors handle creating multiple new files.

---
Repository: /testbed
