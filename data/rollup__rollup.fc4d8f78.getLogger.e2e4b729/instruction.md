# Bug Report

### Describe the bug

I'm experiencing an issue with the logger where log messages are not being output at the expected log levels. It seems like the logger is filtering out messages that should be displayed based on the configured minimum log level.

### Reproduction

```js
const logger = getLogger(
  plugins,
  { level: 'warn' },  // Set minimum level to 'warn'
  onLog
);

// This warning should be logged but isn't appearing
logger('warn', { message: 'This is a warning' });

// Only errors seem to be getting through
logger('error', { message: 'This is an error' });
```

### Expected behavior

When the minimum log level is set to `'warn'`, both warnings and errors should be logged. Currently it appears that only messages with a higher priority than the minimum are being output, when it should include messages at the minimum level and above.

### Additional context

This might be related to how log level priorities are being compared. The filtering logic seems inverted - messages that should be shown are being suppressed and vice versa.

---
Repository: /testbed
