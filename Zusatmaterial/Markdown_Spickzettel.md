## Markdown-Spickzettel

Markdown ist eine einfache Markup-Sprache zur Formatierung von Text. Hier sind einige grundlegende Markdown-Elemente:

### Überschriften

Überschriften werden mit `#`, `##`, `###`, usw. erstellt.

```markdown
# Das ist eine Überschrift der Ebene 1
## Das ist eine Überschrift der Ebene 2
### Das ist eine Überschrift der Ebene 3
```

### Textformatierung

- **Fett**: Text wird fett dargestellt, indem er in doppelte Sternchen `**` eingeschlossen wird.

```markdown
**Das ist fett gedruckter Text**
```

- *Kursiv*: Text wird kursiv dargestellt, indem er in einzelne Sternchen `*` eingeschlossen wird.

```markdown
*Das ist kursiver Text*
```

- ***Fett und kursiv***: Text wird fett und kursiv dargestellt, indem er in dreifache Sternchen `***` eingeschlossen wird.

```markdown
***Das ist fett und kursiv***
```

### Listen

- Ungeordnete Liste: Verwende `*` oder `-` gefolgt von Leerzeichen.

```markdown
- Punkt 1
- Punkt 2
  - Unterpunkt 2.1
  - Unterpunkt 2.2
* Punkt 3
```

- Geordnete Liste: Verwende Zahlen gefolgt von Punkt und Leerzeichen.

```markdown
1. Erster Punkt
2. Zweiter Punkt
3. Dritter Punkt
```

### Links

Verwende `[Linktext](URL)` für Links.

```markdown
[Google](https://www.google.com)
```

### Bilder

Verwende `![Alt-Text](Bild-URL)` für Bilder.

```markdown
![Bildbeschreibung](https://www.example.com/bild.jpg)
```

### Code

- Inline-Code: Um Text als Inline-Code darzustellen, verwende Gravitationsstriche (Backticks) `.

```markdown
Das ist `Inline-Code`.
```

- Codeblock: Um einen Codeblock zu erstellen, umschließe den Code mit drei Gravitationsstrichen ``` und füge die Sprache optional hinzu.

<pre>
```python
def hallo_welt():
    print("Hallo, Welt!")
```
</pre>

### Zitate

Verwende `>` für Zitate.

```markdown
> Dies ist ein Zitat.
```

### Horizontale Linien

Füge eine horizontale Linie mit drei oder mehr Bindestrichen `---`, Asterisken `***`, oder Unterstrichen `___` ein.

```markdown
---
```

### Escapen von Markdown

Wenn du Markdown-Symbole als normalen Text anzeigen möchtest, verwende den Backslash `\` vor dem Symbol.

```markdown
\*Dies wird nicht kursiv dargestellt\*
```

Das war ein kurzer Überblick über Markdown! Du kannst diese Syntax verwenden, um Text in deinen Jupyter-Notebooks oder anderen Markdown-Dokumenten zu formatieren.