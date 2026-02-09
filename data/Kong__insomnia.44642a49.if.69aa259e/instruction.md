# Bug Report

### Describe the bug

After a recent update, the application appears to hang or become unresponsive when viewing responses with body content. The issue seems to occur when accessing the same response multiple times, and the application becomes progressively slower with each access.

### Reproduction

1. Send a request that returns a response with a body
2. View the response body
3. Navigate away and come back to view the same response again
4. Repeat step 3 several times

The application becomes noticeably slower each time, and eventually may freeze completely.

### Expected behavior

Viewing response bodies should consistently perform well regardless of how many times the same response is accessed. The application should not hang or become unresponsive.

### Additional context

This seems to have started happening after some recent changes. It's particularly noticeable with larger response bodies, but even small responses eventually cause issues if accessed enough times.

---
Repository: /testbed
