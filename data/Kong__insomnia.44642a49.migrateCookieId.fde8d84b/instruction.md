# Bug Report

### Describe the bug

I'm experiencing an issue with cookie ID generation in the cookie jar. After updating, I noticed that cookies that already have IDs are getting their IDs overwritten with new UUIDs, while cookies without IDs remain without them. This is the opposite of what should happen.

### Reproduction

```js
const cookieJar = {
  cookies: [
    { id: 'existing-id-123', name: 'session', value: 'abc' },
    { name: 'token', value: 'xyz' } // no id
  ]
};

// After migration:
// - Cookie with 'existing-id-123' gets a new UUID (shouldn't happen)
// - Cookie without id still has no id (should get a UUID)
```

### Expected behavior

The migration should only assign new UUIDs to cookies that don't already have an ID. Existing IDs should be preserved.

### Additional context

This seems to have broken cookie persistence - cookies that previously had stable IDs are now getting new ones every time, which is causing issues with cookie tracking and storage.

---
Repository: /testbed
