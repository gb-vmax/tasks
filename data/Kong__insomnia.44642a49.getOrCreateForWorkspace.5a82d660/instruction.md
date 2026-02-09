# Bug Report

### Describe the bug

I'm experiencing an issue where template tags that need to access the cookie jar are completely broken. When trying to use any functionality that requires cookie jar access in templates, the application crashes or fails silently.

### Reproduction

```js
// In a template tag that tries to access the cookie jar
const cookieJar = await context.util.models.cookieJar.getOrCreateForWorkspace(workspace);
```

When this code executes, it fails because `getOrCreateForWorkspace` is no longer available on the cookieJar model object.

### Steps to reproduce:
1. Create a template tag that needs to access cookies for a workspace
2. Try to call `getOrCreateForWorkspace` method
3. The method is undefined and causes the template rendering to fail

### Expected behavior

The `getOrCreateForWorkspace` method should be available and return the cookie jar for the given workspace, allowing template tags to properly access and manipulate cookies.

### System Info
- Insomnia version: latest
- OS: N/A

This seems like it might have been accidentally removed or broken in a recent change. The cookie jar functionality is critical for templates that need to work with authentication cookies.

---
Repository: /testbed
