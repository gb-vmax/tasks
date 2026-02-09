# Bug Report

### Describe the bug
When creating new responses, older responses are being deleted incorrectly. Instead of keeping the most recent responses up to the `maxResponses` limit, the system is deleting the recent responses and keeping the old ones. This causes loss of important response history data.

### Reproduction
```js
// Create multiple responses for the same request
for (let i = 0; i < 25; i++) {
  await response.create({
    parentId: 'req_123',
    environmentId: 'env_abc',
    statusCode: 200,
    body: `Response ${i}`
  }, 20); // maxResponses = 20
}

// Check remaining responses
const responses = await db.find('Response', { parentId: 'req_123' });

// Expected: The 20 most recent responses should remain
// Actual: The 20 oldest responses remain, newest ones are deleted
```

### Expected behavior
When the response limit is reached, the oldest responses should be removed while keeping the most recent ones. If `maxResponses` is set to 20, the system should keep the 20 newest responses and delete any older ones.

### Current behavior
The most recent responses are being deleted instead of the oldest ones, which is the opposite of what should happen. This results in loss of the latest response data.

### System Info
- Version: Latest
- Database: NeDB

---
Repository: /testbed
