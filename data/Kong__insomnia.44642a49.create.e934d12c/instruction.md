# Bug Report

### Describe the bug

After a recent update, creating new unit test suites is taking significantly longer than before. There seems to be a performance issue when multiple test suites are created in quick succession. The UI becomes unresponsive for a few seconds when trying to add new test suites to a workspace.

### Reproduction

```js
// Create multiple test suites quickly
const workspace = { _id: 'wrk_123' };

// First suite creates fine
await createUnitTestSuite({ parentId: workspace._id, name: 'Test Suite 1' });

// Second suite takes noticeably longer
await createUnitTestSuite({ parentId: workspace._id, name: 'Test Suite 2' });

// Third and subsequent suites cause UI lag
await createUnitTestSuite({ parentId: workspace._id, name: 'Test Suite 3' });
```

### Expected behavior

Creating test suites should be instantaneous like it was before. There shouldn't be any noticeable delay or UI lag when adding multiple test suites.

### Additional context

This seems to have started happening after the latest update. I have about 20+ test suites in my workspace and the performance degradation is really noticeable. Each new suite takes progressively longer to create.

---
Repository: /testbed
