# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with response body reading in Insomnia. When making multiple requests to the same endpoint, the application seems to be returning cached/stale response bodies instead of the fresh data from the server.

### Reproduction

1. Make a request to an API endpoint that returns dynamic data (e.g., current timestamp)
2. Note the response body content
3. Make the same request again
4. The response body shows the same data as the first request, even though the server is returning different data

This is particularly problematic when:
- Testing APIs that return time-sensitive data
- Debugging endpoints that should return different responses on each call
- Working with endpoints that have side effects

### Expected behavior

Each request should return the actual response body from the server, not a cached version from a previous request. Response bodies should only be cached if explicitly configured to do so.

### Additional context

This seems to have started happening recently. I'm working with REST APIs that return JSON responses, and the issue occurs consistently across different endpoints. The response headers and status codes update correctly, but the body content remains stale.

---
Repository: /testbed
