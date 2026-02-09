# Bug Report

### Describe the bug
When using the response template tag with nested request dependencies, the application becomes unresponsive or hangs indefinitely. This seems to happen when a request references another request's response, and that second request also references a response.

### Reproduction
```js
// Request A references Request B's response
GET /api/endpoint1
Body: {{ response 'body', 'request-b-id' }}

// Request B references Request C's response  
GET /api/endpoint2
Body: {{ response 'body', 'request-c-id' }}

// Request C
GET /api/endpoint3
```

When trying to send Request A, the app hangs and never completes. Looking at the console, I can see `[response tag] Preventing recursive render` being logged, but the request still doesn't finish.

### Expected behavior
The requests should be sent in the correct order (C → B → A) and complete successfully, or at minimum, fail with a clear error message instead of hanging.

### System Info
- Insomnia version: Latest
- OS: macOS

This is blocking our workflow since we have several chained requests that depend on each other's responses. Any help would be appreciated!

---
Repository: /testbed
