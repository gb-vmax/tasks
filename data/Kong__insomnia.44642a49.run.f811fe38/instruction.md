# Bug Report

### Describe the bug

The UUID template tag is not generating UUIDs correctly after a recent update. When trying to use the basic UUID functionality, I'm getting errors about missing name parameters even though I'm just trying to generate a standard v4 UUID.

### Reproduction

Using the UUID template tag with default settings:
```
{% uuid %}
```

Or explicitly specifying v4:
```
{% uuid 'v4' %}
```

Both of these now throw an error:
```
UUID v5 requires a name parameter (format: "v5:namespace:name")
```

This is confusing because I'm not trying to use v5 at all - just the standard v4 random UUID generation.

### Expected behavior

The template tag should generate a random v4 UUID by default without requiring any additional parameters. This used to work fine before.

### Additional context

This seems to have started happening recently. The error message mentions v5 UUIDs which I'm not even trying to use. It looks like something might be incorrectly parsing the UUID type parameter.

---
Repository: /testbed
