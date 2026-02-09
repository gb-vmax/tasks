# Bug Report

### Describe the bug

I'm encountering an issue with export default statements in MDX files. It seems like semicolons are being added or removed incorrectly when exporting default declarations, which is causing syntax errors in the generated JavaScript output.

### Reproduction

When I have an MDX file with a default export like this:

```mdx
export default function MyComponent() {
  return <div>Hello</div>
}
```

The generated output has incorrect semicolon placement. It looks like the logic for determining when to add semicolons after export default statements isn't working as expected.

Similarly, when exporting default objects or other expressions:

```mdx
export default {
  title: 'My Page',
  description: 'Description'
}
```

The semicolon handling seems inconsistent and produces invalid JavaScript in some cases.

### Expected behavior

Export default declarations should have proper semicolon placement based on the type of declaration being exported. Function declarations shouldn't have semicolons added, while expression-based exports should have them when appropriate.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This is breaking my build process since the generated code has syntax errors. Any help would be appreciated!

---
Repository: /testbed
