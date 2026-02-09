# Bug Report

### Describe the bug

The table of contents (TOC) generation is producing incorrect output where heading IDs and values are swapped. When generating the TOC for MDX files, the `value` field contains the heading ID and the `id` field contains the heading text, which is the opposite of what it should be.

### Reproduction

Create an MDX file with headings:

```md
## Hello World

Some content here.

## Getting Started

More content.
```

The generated TOC output has swapped fields:
```js
{
  value: "hello-world",  // This should be "Hello World"
  id: "Hello World",     // This should be "hello-world"
  level: 2
}
```

### Expected behavior

The TOC should have the correct structure:
```js
{
  value: "Hello World",   // The heading text
  id: "hello-world",      // The heading ID/slug
  level: 2
}
```

This is breaking navigation and TOC rendering since the values are reversed.

---
Repository: /testbed
