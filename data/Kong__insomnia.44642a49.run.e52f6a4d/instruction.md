# Bug Report

### Describe the bug

I'm experiencing an issue with the `cookie` attribute in template tags where the functionality appears to be incomplete or broken. When trying to reference a cookie value in a request template, the operation doesn't complete properly and seems to cut off mid-execution.

### Reproduction

```js
// In a request template, trying to use:
{% cookie 'session_id' %}

// Or when accessing cookie attributes:
const cookieValue = await templateTag.run(context, 'cookie', 'session_id');
```

The cookie retrieval process starts but doesn't return a value. It seems like the code execution is getting interrupted before it can resolve the cookie value.

### Expected behavior

The template tag should successfully retrieve the cookie value from the cookie jar and return it for use in the request. The promise should resolve with the cookie value matching the specified name.

### Additional context

This affects any workflow that relies on dynamically inserting cookie values into requests using template tags. The URL attribute seems to work fine, but the cookie attribute specifically has this issue.

---
Repository: /testbed
