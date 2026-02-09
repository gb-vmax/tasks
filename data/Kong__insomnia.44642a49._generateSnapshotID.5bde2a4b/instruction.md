# Bug Report

### Describe the bug

I'm experiencing an issue with snapshot ID generation in the VCS module. When creating snapshots with identical content (same blobs and parent/project IDs), the system generates different snapshot IDs each time instead of producing consistent, deterministic IDs.

This is causing problems with duplicate snapshot detection - snapshots that should be considered identical are being treated as different snapshots, leading to unnecessary storage and sync issues.

### Reproduction

```js
// Create two snapshots with identical state
const state = [
  { blob: 'abc123', key: 'doc1', name: 'Document 1' },
  { blob: 'def456', key: 'doc2', name: 'Document 2' }
];

const parentId = 'parent-123';
const projectId = 'project-456';

// Generate snapshot ID twice with the same inputs
const snapshotId1 = _generateSnapshotID(parentId, projectId, state);
const snapshotId2 = _generateSnapshotID(parentId, projectId, state);

// Expected: snapshotId1 === snapshotId2
// Actual: snapshotId1 !== snapshotId2
```

### Expected behavior

Snapshot IDs should be deterministic - generating a snapshot ID with the same parent, project, and state should always produce the same ID. This is essential for detecting duplicate snapshots and avoiding unnecessary storage.

### Additional context

This seems to have started happening recently. The snapshot deduplication that was working before is now broken, and I'm seeing multiple snapshots with identical content being created.

---
Repository: /testbed
