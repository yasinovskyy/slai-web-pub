# Day 7. Using JavaScript

JavaScript is a powerful language that can be used both client-side and server-side.

## Syntax

### Variable definition

```javascript
let a = 10;
let zoo = ["aardvark", "beaver", "cheetah"];
let zoo = {"aardvark": "Alice", "beaver": "Bob", "cheetah": "Charlie"};
```

### Conditions

```javascript
let zoo = ["aardvark", "beaver", "cheetah"];
if (zoo.includes("beaver")) {...}
let zoo = {"aardvark": "Alice", "beaver": "Bob", "cheetah": "Charlie"};
if ("beaver" in zoo) {...}
```

### Loops

```javascript
for (let animal in zoo) {console.log(animal);}
for (let animal of zoo) {console.log(animal);}
```

### Function definition

```javascript
function greet(name) {
    console.log(`Hello, ${name}`);
}

greet("Student");
```

## XPath

XML Path Language (XPath) uses a non-XML syntax to provide a way of addressing (finding) different parts of an XML (HTML) document.

```javascript
document.querySelector(elementId);
document.querySelectorAll(elementClass);
```

## DOM

JavaScript can be used to manipulate Document Object Model.

```javascript
let bodyElement = document.querySelector("body");
let footer = document.createElement("footer");
footer.innerHTML = "<strong>Hello</strong>";
bodyElement.appendChild(footer);
```

## References

- [JavaScript — Dynamic client-side scripting - Learn web development | MDN](https://developer.mozilla.org/en-US/docs/Learn/JavaScript)
- [Fetch API - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
- [JSON - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON)
- [XPath | MDN](https://developer.mozilla.org/en-US/docs/Web/XPath)
- [Selectors Level 4](https://drafts.csswg.org/selectors/)
- [Open Trivia DB: Free to use, user-contributed trivia question database.](https://opentdb.com/api_config.php)
