# Bug Report

### Describe the bug

The timestamp template tag appears to be broken after a recent update. When I try to use it in my requests, I'm getting incomplete output or the tag just doesn't render at all.

### Reproduction

I've been using the timestamp tag in my API requests like this:

```
{% timestamp 'iso-8601' %}
```

After updating, this no longer works properly. The template tag seems to be cut off or incomplete - I'm not getting any timestamp output in my requests.

I also tried using it with custom formats:

```
{% timestamp 'custom' 'yyyy-MM-dd' %}
```

Same issue - no output is being generated.

### Expected behavior

The timestamp tag should generate the current timestamp in the specified format. It was working fine in the previous version I was using.

### Additional context

This is blocking me from testing my APIs that require timestamps in the request body or headers. The template tag appears to be incomplete or corrupted somehow.

---
Repository: /testbed
