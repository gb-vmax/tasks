# Bug Report

### Describe the bug

The logging system is not respecting the configured log levels properly. Messages that should be suppressed based on the log level are still being logged, and position validation seems to be inverted.

### Reproduction

```js
// Set log level to 'warn'
const logHandler = getLogHandler('info', 'myPlugin', 'warn');

// This info message gets logged even though log level is 'warn'
logHandler({ message: 'This is an info message' }, { line: 10, column: 5 });

// Also, when providing a valid position, I get warnings about invalid position
// But when I don't provide a position, no warning appears
```

### Expected behavior

1. When the log level is set to 'warn', only 'warn' and 'error' level messages should be logged. 'info' and 'debug' messages should be suppressed.
2. When a valid position is provided, no warning about invalid position should appear.
3. When position is missing (null/undefined), a warning about invalid position should be shown.

### System Info
- Version: Latest from main branch
- Node: v18.x

This seems like the filtering logic might be backwards? The position validation also appears to be inverted.

---
Repository: /testbed
