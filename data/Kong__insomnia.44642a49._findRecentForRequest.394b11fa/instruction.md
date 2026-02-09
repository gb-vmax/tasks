# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with response body handling in Insomnia. The application seems to hang or crash when trying to view response bodies, particularly for larger responses. It looks like the code for retrieving and caching response bodies was modified but the implementation appears incomplete.

### Reproduction

1. Send a request that returns a response body
2. Try to view the response in the UI
3. The response viewer either hangs indefinitely or the application becomes unresponsive

This is blocking my ability to inspect API responses. The issue started appearing after pulling the latest changes.

### Expected behavior

Response bodies should load and display correctly in the UI without hanging or crashing. The caching mechanism should work properly to improve performance for repeated views of the same response.

### Additional context

Looking at the code, it seems like there's an incomplete refactoring around response body streaming and caching. The `_findRecentForRequest` and `getLatestForRequest` functions appear to have been removed or replaced with caching logic, but the new implementation looks cut off mid-function. The `_applyRangeToStream` function seems to be missing its complete implementation.

This is affecting basic functionality of viewing request/response data in the app.

---
Repository: /testbed
