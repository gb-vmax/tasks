# Bug Report

### Describe the bug

I'm experiencing issues with unit test suite ordering after recent changes. When I create multiple test suites under the same parent, they don't appear in the correct order based on their `metaSortKey` values. The ordering seems inconsistent and sometimes shows suites in a completely different sequence than expected.

### Reproduction

```js
// Create multiple test suites with specific sort keys
const suite1 = await create({
  parentId: 'workspace_1',
  metaSortKey: 100,
  name: 'First Suite'
});

const suite2 = await create({
  parentId: 'workspace_1',
  metaSortKey: 50,
  name: 'Second Suite'
});

const suite3 = await create({
  parentId: 'workspace_1',
  metaSortKey: 75,
  name: 'Third Suite'
});

// Retrieve suites
const suites = getByParentId('workspace_1');

// Expected order: suite2 (50), suite3 (75), suite1 (100)
// But the order is wrong or inconsistent
```

### Expected behavior

Test suites should be returned in ascending order based on their `metaSortKey` values. Suite with key 50 should come before suite with key 75, which should come before suite with key 100.

### Additional context

This seems to have started happening recently. The suites are being created correctly with the right sort keys, but when I fetch them they're not in the expected order. Sometimes refreshing or waiting a bit changes the order, which is really confusing.

---
Repository: /testbed
