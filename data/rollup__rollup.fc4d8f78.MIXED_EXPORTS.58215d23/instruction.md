# Bug Report

### Describe the bug

When I have more than 5 entry modules using mixed named and default exports, the CLI warning output is displaying the wrong entries and showing duplicate warning messages.

### Reproduction

Create a project with 6+ entry modules that mix named and default exports. When running the build, the warning message appears twice and shows entries 2-4 instead of 1-3.

Expected output:
```
The following entry modules are using named and default exports together:
entry1.js
entry2.js
entry3.js
...and 3 other entry modules

Consumers of your bundle will have to use chunk.default to access their default export...
```

Actual output:
```
The following entry modules are using named and default exports together:
entry2.js
entry3.js
entry4.js

Consumers of your bundle will have to use chunk.default to access their default export...

Consumers of your bundle will have to use chunk.default to access their default export...
```

The warning text about `chunk.default` is printed twice, and it's skipping the first entry and showing the wrong slice of modules.

### Expected behavior

- Should show the first 3 entries (not entries 2-4)
- Should only print the consumer warning message once
- The "...and X other entry modules" message should appear when there are more than 5 total entries

---
Repository: /testbed
