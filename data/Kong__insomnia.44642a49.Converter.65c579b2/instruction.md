# Bug Report

### Describe the bug

I'm experiencing an issue with the Swagger 2.0 importer where the generated base URL environment variable is malformed. The scheme and host components appear to be in the wrong order, resulting in invalid URLs like `example.com://https/api/v1` instead of `https://example.com/api/v1`.

### Reproduction

1. Import a Swagger 2.0 specification file
2. Check the generated base environment variables
3. Notice that `base_url` is constructed as `{{ _.host }}://{{ _.scheme }}{{ _.base_path }}`

The generated URL ends up being something like:
```
example.com://https/api/v1
```

Instead of the expected:
```
https://example.com/api/v1
```

### Expected behavior

The `base_url` environment variable should be constructed with the scheme (protocol) first, followed by the host, like: `{{ _.scheme }}://{{ _.host }}{{ _.base_path }}` to produce valid URLs such as `https://example.com/api/v1`.

### Additional context

This affects all imported Swagger 2.0 files and makes the generated requests fail since the base URL is invalid. The requests can't be executed until the environment variables are manually corrected.

---
Repository: /testbed
