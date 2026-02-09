# Bug Report

### Describe the bug

When exporting requests data, the export format seems to be incorrect. If I specify 'json' as the format, I'm getting YAML output instead of JSON. Also, it appears that ancestor documents are being skipped during export when they should be included.

### Reproduction

```js
// Try to export with JSON format
const exported = await exportRequestsData(
  requests,
  false,
  'json'
);

// Expected: JSON string
// Actual: YAML formatted output
```

Also noticed that when exporting requests with their ancestors (like parent folders), some ancestor documents are missing from the export even though they exist in the database.

### Expected behavior

1. When format is set to 'json', the output should be a JSON string
2. When format is set to 'yaml', the output should be YAML formatted
3. All ancestor documents should be included in the export

### System Info
- Using the latest version from main branch

---
Repository: /testbed
