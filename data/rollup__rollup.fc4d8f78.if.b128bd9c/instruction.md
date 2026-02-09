# Bug Report

### Describe the bug

When logging messages with either a plugin name OR location info, the log augmentation is not being applied. It seems like the logic for determining whether to augment logs has changed and now requires BOTH plugin and location to be present, which breaks cases where only one is available.

### Reproduction

```js
// Case 1: Log with only plugin info (no location)
const logWithPlugin = {
  plugin: 'my-plugin',
  message: 'Something happened'
  // no loc property
}
augmentLogMessage(logWithPlugin)
// Expected: message should be augmented with plugin prefix
// Actual: message is not augmented

// Case 2: Log with only location info (no plugin)
const logWithLocation = {
  loc: { file: 'src/main.js', line: 10 },
  message: 'Error occurred'
  // no plugin property
}
augmentLogMessage(logWithLocation)
// Expected: message should be augmented with location info
// Actual: message is not augmented
```

### Expected behavior

Log messages should be augmented when they have EITHER a plugin name OR location information. Previously this worked correctly, but now it seems to require both properties to be present simultaneously.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
