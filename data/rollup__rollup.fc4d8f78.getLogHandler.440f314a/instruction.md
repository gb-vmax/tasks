# Bug Report

### Describe the bug

The logging system is not working as expected. When I set a log level, messages that should be filtered out are still appearing, and messages that should be logged are being suppressed. Additionally, I'm getting unexpected warnings about invalid log positions even when I provide valid position information.

### Reproduction

```js
const logger = getLogHandler('info', 'myPlugin', 'warn');

// This should be logged (info < warn priority) but nothing happens
logger({ message: 'Important info message' }, { line: 10, column: 5 });

// Also getting warnings about invalid positions even though I'm passing position data
logger({ message: 'Debug info' }, { line: 20, column: 10 });
// Output: Warning about invalid log position
```

### Expected behavior

1. Log messages with priority level lower than the configured log level should be suppressed
2. Log messages with priority level equal to or higher than the configured log level should be displayed
3. When position information is provided, it should be used without triggering invalid position warnings
4. Invalid position warnings should only appear when position is NOT provided

### System Info
- Version: latest
- Node: 18.x

---
Repository: /testbed
