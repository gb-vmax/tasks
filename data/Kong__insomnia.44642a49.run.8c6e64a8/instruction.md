# Bug Report

### Describe the bug

I'm experiencing an issue with the JSONPath template tag where it seems to be cutting off or truncating the output. When I try to use JSONPath queries, I'm getting incomplete results or the function doesn't seem to be working at all.

### Reproduction

```js
// Using JSONPath template tag
const jsonData = '{"users": [{"name": "Alice"}, {"name": "Bob"}]}';
const filter = '$.users[0].name';

// Expected: "Alice"
// Actual: Incomplete or no output
```

I've also tried using format directives like `|format:first` and `|default:fallback` but the behavior is inconsistent.

### Expected behavior

The JSONPath query should return the first matching result properly. When using format directives like:
- `|format:first` - should return the first result
- `|format:last` - should return the last result  
- `|format:all` - should return all results as JSON array
- `|format:join` or `|format:join:;` - should join results with delimiter
- `|default:value` - should return default value when no results found

The template tag should parse these directives correctly and return complete, properly formatted output.

### System Info
- Insomnia version: latest
- OS: macOS

This might have been introduced in a recent update to the template tag handling code. The JSONPath functionality was working fine before.

---
Repository: /testbed
