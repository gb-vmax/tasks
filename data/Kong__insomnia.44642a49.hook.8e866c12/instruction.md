# Bug Report

### Describe the bug

After a recent update, the default headers plugin appears to be broken. When I try to send requests, they fail immediately and nothing happens. The plugin code seems to be incomplete or cut off - requests just don't get sent anymore.

### Reproduction

1. Set up DEFAULT_HEADERS environment variable with some headers
2. Try to send any request
3. Request fails to execute

Example setup:
```js
{
  "DEFAULT_HEADERS": {
    "X-API-Key": "my-key",
    "Content-Type": "application/json"
  }
}
```

When I try to send a request with this configuration, nothing happens. The request doesn't get sent at all.

### Expected behavior

The default headers should be applied to the request and the request should be sent normally, just like it worked before.

### System Info
- Insomnia version: latest
- OS: macOS

This was working fine before the recent changes. Not sure what happened but it seems like something got corrupted in the plugin code.

---
Repository: /testbed
