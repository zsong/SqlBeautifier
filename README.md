SqlBeautifier
============================

This is a SQL formatter plugin using [python-sqlparse](https://code.google.com/p/python-sqlparse/) for both Sublime 2 and 3. 

Enjoy!

### Installation
Please install Sublime [Package Control](https://sublime.wbond.net/installation) first. Then inside *Package Control: Install Package*, type *SqlBeautifier* and then click to confirm.


###Settings
#### The default key binding for Mac is

```
{ "keys": ["super+k", "super+f"], "command": "sql_beautifier" }
```

#### The default key binding for Windows / Linux is

```
{ "keys": ["ctrl+k", "ctrl+f"], "command": "sql_beautifier" }
```

#### Options for formatter

To change the options, click through *Package Settings -> Sql Beautifier -> Settings User* and add the overrided options in JSON like this

```
{
	"indent_tabs": true,
	"indent_width": 1
}
```

This overrides the default option at *Package Settings -> Sql Beautifier -> Settings Default*.

Here is the list of options the formatter supports:

- **keyword_case**: Changes how keywords are formatted. Allowed values are “upper”, “lower” and “capitalize” and null (leaves case intact).

- **identifier_case**: Changes how identifiers are formatted. Allowed values are “upper”, “lower”, and “capitalize” and null (leaves case intact).

- **strip_comments**: If True comments are removed from the statements.

- **reindent**: If True the indentations of the statements are changed.

- **indent_tabs**: If True tabs instead of spaces are used for indentation.

- **indent_width**: The width of the indentation, defaults to 2.
