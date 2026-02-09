# Bug Report

### Describe the bug

When plugin warnings are displayed in the CLI, URLs are not showing up correctly in some cases. It seems like the URL is being skipped or reset when it should be displayed, particularly when warnings don't have location information or frames.

### Reproduction

Create a plugin that emits warnings with URLs but without frames or location data:

```js
{
  plugins: [
    {
      name: 'test-plugin',
      buildStart() {
        this.warn({
          message: 'Test warning without frame',
          url: 'https://example.com/docs'
        });
      }
    }
  ]
}
```

The URL should be displayed in the output, but it's being skipped in certain scenarios.

### Expected behavior

Plugin warning URLs should consistently appear in the CLI output when provided, regardless of whether the warning has location information or a frame. The URL should be shown once per unique URL for each warning message group.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
