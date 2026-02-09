# Bug Report

### Describe the bug

The "Max age (seconds)" field in the Response template tag is not showing up when it should be visible. I've set the trigger behavior to "when-expired" and selected a request, but the max age input field remains hidden.

### Reproduction

1. Add a Response template tag to your request
2. Select an attribute (e.g., "body" or "header")
3. Choose a request from the dropdown
4. Set the trigger behavior to "when-expired"
5. Notice that the "Max age (seconds)" field doesn't appear

The field should be visible at this point since we're using the "when-expired" trigger behavior, but it stays hidden.

### Expected behavior

When trigger behavior is set to "when-expired", the "Max age (seconds)" field should become visible so I can configure how long to cache the response before it expires.

### Additional context

This seems to affect any attribute selection except possibly "raw" and "url". The field visibility logic might not be working correctly with the current attribute/request selection state.

---
Repository: /testbed
