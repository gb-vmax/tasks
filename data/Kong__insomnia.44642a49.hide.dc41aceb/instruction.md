# Bug Report

### Describe the bug

I'm experiencing an issue with the request template tag where certain header attributes are not being properly hidden in the UI. Specifically, when trying to access sensitive headers like `Authorization` or `Cookie` through the `header` attribute, they should be hidden from the dropdown/autocomplete but they're still showing up.

### Reproduction

```js
// When using the request template tag with header attribute
// These sensitive headers should be hidden but are still visible:

{% request 'header', 'Authorization' %}
{% request 'header', 'Cookie' %}
{% request 'header', 'authorization' %}  // lowercase variant
{% request 'header', 'cookie' %}         // lowercase variant
```

The issue seems to be that the `hide` logic isn't checking for the combination of `attribute === 'header'` with restricted header names. It only checks if the attribute itself is in the hide list (like 'url', 'oauth2', etc.), but doesn't validate the second argument when the attribute is 'header'.

### Expected behavior

When the attribute is set to `'header'` and the header name is either `'Authorization'` or `'Cookie'` (case-insensitive), these options should be hidden from the UI to prevent accidental exposure of sensitive authentication data.

### System Info
- Insomnia version: latest
- OS: macOS

This could be a security concern as it might lead users to accidentally expose sensitive authentication headers in their templates.

---
Repository: /testbed
