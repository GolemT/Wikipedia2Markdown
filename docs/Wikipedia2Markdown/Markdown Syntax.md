---
sidebar_position: 5
---

# Markdown Syntax

Hier is eine kurze Ansammlung an Markdown Syntax und schreibweisen.

# Heading 1
```markdown
# Heading 1
```

## Heading 2
```markdown
Heading 2
```

### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6

:::warning Überschrift
Warning Message 
(Nur sichtbar in Browser, nicht in VS Code Preview)
:::
```markdown
:::warning Überschrift
Warning Message 
(Nur sichtbar in Browser, nicht in VS Code Preview)
:::
```

:::danger Überschrift
Danger Message 
(Nur sichtbar in Browser, nicht in VS Code Preview)
:::

```markdown
:::danger Überschrift
Danger Message
(Nur sichtbar in Browser, nicht in VS Code Preview)
:::
```

:::info Überschrift
Info Message
(Nur sichtbar in Browser, nicht in VS Code Preview)
:::

```markdown
:::info Überschrift
Info Message
(Nur sichtbar in Browser, nicht in VS Code Preview)
:::
```

* Aufzählung
  * Eingerückte Aufzählung
  * Eingerückte Aufzählung
* Aufzählung
  1. Eingerückte Nummerierung
  2. Eingerückte Nummerierung
* Aufzählung

```markdown
* Aufzählung
  * Eingerückte Aufzählung
  * Eingerückte Aufzählung
* Aufzählung
  1. Eingerückte Nummerierung
  2. Eingerückte Nummerierung
* Aufzählung
```

1. Nummerierte Aufzählung
    1. Eingerückte Nummerierung
    2. Eingerückte Nummerierung
2. Nummerierte Aufzählung
   * Eingerückte Aufzählung
   * Eingerückte Aufzählung
3. Nummerierte Aufzählung

```markdown
1. Nummerierte Aufzählung
    1. Eingerückte Nummerierung
    2. Eingerückte Nummerierung
2. Nummerierte Aufzählung
   * Eingerückte Aufzählung
   * Eingerückte Aufzählung
3. Nummerierte Aufzählung
```

## Code Snippet

```python
// Code Block
main():
print("Hello, World")
```

```markdown
    ```python
    // Code Block
    main():
    print("Hello, World")
    ```
```


## Zitat:
>> Lorem ipsum dolor sit amet,
>>
>> consectetur adipisici elit
>
> — Docusaurus

```markdown
> Zitat:
>> Lorem ipsum dolor sit amet,
>>
>> consectetur adipisici elit
>
> — Docusaurus
```

| Table Header 1                 | Table Header 2                              |
| ----------------------- | ---------------------------------------- |
| Table Cell 1        | Table Cell 2  |
| X        | X  |

```markdown

| Table Header 1                 | Table Header 2                              |
| ----------------------- | ---------------------------------------- |
| Table Cell 1        | Table Cell 2  |
| X        | X  |

```

**Bold Text**

```markdown
**Bold Text**
```

[Link](https://git.tech.rz.db.de/TimKosleck/Wikipedia2markdown)

```markdown
[Link](https://git.tech.rz.db.de/TimKosleck/Wikipedia2markdown)
```

## Image

![Image](../../static/img/docusaurus.png)

```markdown
![Image](./static/img/DB_rgb.png)
```

## Separator line

---

```markdown
---
```
