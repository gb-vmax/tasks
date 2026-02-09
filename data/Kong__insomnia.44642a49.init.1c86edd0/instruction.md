# Bug Report

### Describe the bug

After a recent update, the default timeout value for requests has changed unexpectedly. Instead of the expected 30 seconds (30,000 milliseconds), requests are now timing out at 29 seconds (29,000 milliseconds). This is causing issues with API endpoints that typically respond within 29-30 seconds.

### Reproduction

1. Create a new workspace or reset settings to defaults
2. Check the timeout setting value
3. Make a request to an endpoint that takes approximately 29.5 seconds to respond

**Expected behavior:** The default timeout should be 30,000 milliseconds (30 seconds) and requests should wait the full 30 seconds before timing out.

**Actual behavior:** The default timeout is 29,000 milliseconds (29 seconds) and requests that take longer than 29 seconds are being terminated prematurely.

### Additional context

This seems to have started happening after the latest changes. Our API tests that were previously passing with endpoints responding in ~29.5 seconds are now failing with timeout errors. The 1 second difference is significant for our use case.

---
Repository: /testbed
