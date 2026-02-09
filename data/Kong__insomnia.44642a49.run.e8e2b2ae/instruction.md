# Bug Report

### Describe the bug

The UUID template tag is not working after a recent update. When trying to use the UUID tag in my requests, I'm getting JavaScript errors and the template isn't being rendered at all.

### Reproduction

I have a simple request that uses the UUID tag like this:

```
POST /api/users
{
  "id": "{% uuid 'v4' %}",
  "name": "Test User"
}
```

After the recent update, this template no longer works and breaks the request rendering. The same happens with v1 UUIDs:

```
{% uuid 'v1' %}
```

Both of these used to work fine before, but now they're causing issues when I try to send requests.

### Expected behavior

The UUID template tag should generate a valid UUID string (either v1 or v4) that gets inserted into the request. The request should be sent successfully with the generated UUID.

### System Info
- Insomnia version: Latest
- OS: macOS

This is blocking my workflow as I rely on UUID generation for testing. Any help would be appreciated!

---
Repository: /testbed
