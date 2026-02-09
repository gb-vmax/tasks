# Bug Report

### Describe the bug

The response template tag seems to be broken after a recent change. When trying to reference a response from another request using the `{% response %}` tag, I'm getting unexpected behavior or errors.

### Reproduction

```js
// In a request, try using the response tag:
{% response 'body', req_123abc, 'filter' %}
```

When sending the request, the template tag doesn't seem to process correctly. The response data is not being extracted as expected.

### Expected behavior

The response tag should extract the specified field (body, header, url, or raw) from the referenced request's response and inject it into the current request.

### Additional context

This was working fine before, but something seems to have changed with how the response tag processes requests. The tag should support:
- Different field types (body, header, raw, url)
- Filtering response data
- Resend behaviors (never, no-history, when-expired, always)
- Max age for cached responses

The functionality appears to be incomplete or cut off somehow.

---
Repository: /testbed
