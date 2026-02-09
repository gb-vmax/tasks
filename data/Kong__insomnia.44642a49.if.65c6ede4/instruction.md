# Bug Report

### Describe the bug

After a recent update, I'm noticing that the request update operation is behaving strangely. When I try to update a request, it seems like the function is being defined twice or there's some kind of duplication issue happening. The code appears to execute but the behavior is inconsistent.

### Reproduction

```js
import { update } from './request-operations';

const myRequest = {
  _id: 'req_123',
  type: 'Request',
  name: 'Test Request',
  url: 'https://api.example.com'
};

// Try to update the request
await update(myRequest, { 
  name: 'Updated Request',
  url: 'https://new-api.example.com'
});
```

When running this code, the update doesn't seem to work as expected. Sometimes it works, sometimes it doesn't. Looking at the code, it seems like there might be a syntax issue or something with how the function is structured.

### Expected behavior

The update function should consistently update the request object with the provided patch data and return the updated request.

### System Info
- Insomnia version: Latest
- Platform: macOS

Has anyone else run into this? The update operation was working fine before but now it's acting weird.

---
Repository: /testbed
