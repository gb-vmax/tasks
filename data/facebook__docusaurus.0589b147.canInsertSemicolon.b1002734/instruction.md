# Bug Report

### Describe the bug

I'm experiencing an issue with automatic semicolon insertion (ASI) in MDX parsing. It seems like semicolons are not being inserted correctly in certain situations, causing parsing errors where they shouldn't occur.

### Reproduction

```jsx
// This should parse correctly but throws an error
const MyComponent = () => {
  return (
    <div>
      {someValue}
    </div>
  )
}

export default MyComponent
```

When parsing MDX content with JavaScript/JSX blocks, the parser fails to recognize valid positions for automatic semicolon insertion. This happens specifically when there's a closing brace `}` or at end-of-file positions where a semicolon should be auto-inserted.

### Expected behavior

The parser should correctly identify locations where semicolons can be automatically inserted according to JavaScript ASI rules. Code that is valid JavaScript/JSX should parse without errors in MDX files.

### Additional context

This seems to affect MDX files with:
- Function declarations/expressions followed by closing braces
- Component exports at the end of files
- Any code relying on ASI at brace boundaries

The parsing worked fine in previous versions, so this might be a regression.

---
Repository: /testbed
