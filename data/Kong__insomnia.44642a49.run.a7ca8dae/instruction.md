# Bug Report

### Timestamp template tag stopped working after recent changes

I'm experiencing an issue with the timestamp template tag where it's no longer functioning properly. The tag appears to be broken and I'm getting errors when trying to use it in my requests.

### Reproduction

When trying to use the timestamp tag in a request (for example, in headers or body), I get an error. The tag was working fine before but seems to have broken recently.

Example usage that's failing:
```
{% timestamp 'iso-8601' %}
{% timestamp 'unix' %}
{% timestamp 'custom', 'yyyy-MM-dd' %}
```

### Expected behavior

The timestamp tag should generate the current timestamp in the specified format:
- `iso-8601` should return ISO 8601 formatted date
- `unix` should return Unix timestamp in seconds
- `custom` with a format string should return a custom formatted date

### Additional context

This seems to have started happening after a recent update. The timestamp functionality is critical for my API testing workflow as many endpoints require timestamps in headers.

---
Repository: /testbed
