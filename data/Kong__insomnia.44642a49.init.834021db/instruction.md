# Bug Report

### Describe the bug

After a recent update, I'm seeing unexpected behavior with response objects. When I inspect responses, the `bytesContent` field is now showing `0` instead of `-1` for legacy responses that don't have this property set yet. This is causing issues with how we determine whether a response is from an older version.

### Reproduction

```js
// Create a new response object
const response = init();

// Check bytesContent value
console.log(response.bytesContent); // Now returns 0 instead of -1

// This breaks legacy detection logic that relies on -1 to indicate
// responses from older versions where this property didn't exist
```

### Expected behavior

Legacy responses should have `bytesContent` set to `-1` to distinguish them from newer responses where the property exists but happens to be `0` (no content). The value `-1` was specifically used as a sentinel to indicate "this property didn't exist in older versions" vs "this property exists and the value is 0".

Similarly, `bodyCompression` should be set to `'__NEEDS_MIGRATION__'` for legacy responses that need migration, not `null`.

### Additional context

This is affecting our ability to properly handle and migrate legacy response data. The sentinel values were intentionally chosen to differentiate between:
- Legacy data that needs migration (`-1`, `'__NEEDS_MIGRATION__'`)  
- New data with empty/zero values (`0`, `null`)

---
Repository: /testbed
