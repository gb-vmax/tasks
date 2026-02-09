# Bug Report

### Describe the bug

The response template tag is not working correctly after a recent change. When trying to use the `{% response %}` tag to reference data from another request, it appears the functionality has been broken or incomplete.

### Reproduction

```js
// In a request body or header, use the response tag:
{% response 'body', 'req_123abc', 'jsonpath', 'never' %}
```

When trying to send a request with this template tag, the tag doesn't resolve properly and the request fails or returns unexpected results.

### Expected behavior

The response tag should:
1. Look up the specified request by ID
2. Retrieve the latest response for that request
3. Extract the requested field (body, header, url, or raw)
4. Apply any filters if specified
5. Return the extracted value to be used in the current request

### Additional context

This seems to have started happening recently. The response tag is a critical feature for chaining requests together, so this is blocking our workflow. Not sure if this is a regression or if something changed in how the tag is supposed to be used.

---
Repository: /testbed
