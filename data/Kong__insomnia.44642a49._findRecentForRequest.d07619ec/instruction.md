# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with response body retrieval in Insomnia. When working with larger response bodies, the application seems to hang or become unresponsive. Additionally, response data appears to be inconsistent - sometimes showing cached data from previous requests instead of the actual current response.

### Reproduction

1. Send a request that returns a response body larger than ~5MB
2. Send another request to the same endpoint
3. Notice the application becomes sluggish or unresponsive
4. Sometimes the response shown is from a previous request rather than the current one

This seems to happen more frequently when working with multiple requests in quick succession or when dealing with responses that have large JSON payloads.

### Expected behavior

Response bodies should be retrieved and displayed correctly regardless of size (within reasonable limits). Each request should show its own response data, not cached data from previous requests. The application should remain responsive when handling larger response bodies.

### Additional context

This started happening after updating to the latest version. Previously, large responses were handled without any issues. The problem is particularly noticeable when working with API endpoints that return large datasets or file downloads.

---
Repository: /testbed
