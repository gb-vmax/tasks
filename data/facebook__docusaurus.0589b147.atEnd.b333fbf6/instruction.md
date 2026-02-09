# Bug Report

### Describe the bug

I'm encountering a parsing error when using import/export statements in MDX files. The error message is truncated and appears to be related to acorn parsing, but the actual error details are incomplete or malformed.

### Reproduction

When trying to parse MDX content with import statements, I get an error that seems to be cut off mid-processing. The error object appears to be incomplete - specifically the `offset` field in the error's `place` property.

Example MDX content that triggers this:
```mdx
import { Component } from './component'

# Hello World

<Component />
```

### Expected behavior

The parser should provide complete error information when import/export parsing fails. Error objects should have all required fields properly populated, including the full `offset` value in the error location details.

### Additional context

This seems to affect error reporting when acorn encounters parsing issues with import/export statements. The error construction appears to be incomplete, which makes debugging MDX parsing issues very difficult since you can't get the full error details.

---
Repository: /testbed
