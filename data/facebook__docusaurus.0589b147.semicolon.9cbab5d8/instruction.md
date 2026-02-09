# Bug Report

### Describe the bug

I'm encountering unexpected syntax errors when parsing MDX files. It seems like the parser is now throwing errors for valid JavaScript/JSX code that was previously working fine.

### Reproduction

```jsx
import { Component } from 'react'

export default function MyComponent() {
  return (
    <div>
      <h1>Hello World</h1>
      <p>This is valid MDX</p>
    </div>
  )
}
```

When I try to parse this MDX content, I get an unexpected token error even though the syntax is correct and semicolons are properly placed (or omitted, which should be fine in JavaScript).

### Expected behavior

The MDX parser should successfully parse valid JSX/JavaScript code without throwing syntax errors. Semicolons should be optional in JavaScript as per the ASI (Automatic Semicolon Insertion) rules.

### Additional context

This seems to have started happening recently. The parser appears to be more strict about semicolons than it should be, or there's an issue with how it's handling ASI. Code that parsed successfully before is now failing.

---
Repository: /testbed
