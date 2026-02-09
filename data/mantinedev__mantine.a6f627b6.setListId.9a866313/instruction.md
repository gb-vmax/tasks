# Bug Report

### Describe the bug

When using the spotlight store's `setListId` function, it appears that the state is not being updated correctly. The list ID gets set, but other properties in the state object are being lost/reset instead of being preserved.

### Reproduction

```js
import { setListId } from '@mantine/spotlight';

// Assume store has existing state like:
// { opened: true, query: 'test', listId: 'old-id', selectedAction: 2 }

setListId('new-id', store);

// After calling setListId:
// Expected: { opened: true, query: 'test', listId: 'new-id', selectedAction: 2 }
// Actual: { listId: 'new-id' } - all other properties are lost
```

### Expected behavior

When updating the listId, all other state properties should be preserved. Only the listId should change while keeping the rest of the state intact.

### System Info
- @mantine/spotlight version: latest
- Browser: Chrome

---
Repository: /testbed
