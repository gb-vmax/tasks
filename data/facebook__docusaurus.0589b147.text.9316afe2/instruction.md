# Bug Report

### Describe the bug

I'm experiencing an issue with HTML serialization where text content inside `<style>` tags is being escaped when it shouldn't be. Special characters like `<` and `&` are being converted to HTML entities (`&lt;` and `&amp;`) within style blocks, which breaks the CSS.

### Reproduction

```js
const tree = {
  type: 'element',
  tagName: 'style',
  children: [
    {
      type: 'text',
      value: 'div > span { content: "A & B"; }'
    }
  ]
}

// The output incorrectly escapes characters:
// <style>div &gt; span { content: "A &amp; B"; }</style>
```

### Expected behavior

Text content inside `<style>` tags (and `<script>` tags) should be rendered as-is without escaping special characters. The CSS should remain valid:

```html
<style>div > span { content: "A & B"; }</style>
```

This is critical because escaping characters inside style blocks makes the CSS invalid and breaks styling.

### Additional context

This appears to affect both `<style>` and `<script>` tags. Raw text content in these elements should never be entity-encoded since they have special parsing rules in HTML.

---
Repository: /testbed
