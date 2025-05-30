# Monokai Spacegray Eighties Theme Demo Files

This directory contains comprehensive test files to validate syntax highlighting across different languages and contexts.

## Test Files

### 📊 **theme_test.qmd** 
Comprehensive Quarto document testing:
- R code chunks with tidyverse patterns
- Python data science workflows  
- Observable Plot visualizations
- Markdown formatting
- YAML frontmatter
- Multiple code fence languages

### 📈 **theme_test.R**
Focused R syntax testing:
- Variable assignments (`<-` vs `=`)
- Pipe operators (`|>`, `%>%`)
- Function calls and definitions
- Namespace operators (`::`)
- Infix operators (`%in%`, `%%`)
- Statistical functions
- Data manipulation pipelines

### 🐍 **test_python.py**
Python syntax highlighting:
- Classes and inheritance
- Type hints and annotations
- Async/await patterns
- Decorators and properties
- F-strings and string formatting
- List/dict comprehensions
- Lambda functions
- Exception handling

## Expected Color Scheme

The theme uses these primary colors:

| Element | Color | Hex Code | Example |
|---------|-------|----------|---------|
| **Comments** | Gray italic | `#808080` | `# This is a comment` |
| **Keywords** | Pink | `#F92672` | `if`, `for`, `function`, `class` |
| **Operators** | Pink | `#F92672` | `|>`, `%in%`, `+`, `-`, `==`, `::` |
| **Strings** | Yellow | `#E6DB74` | `"Hello world"` |
| **Numbers** | Purple | `#AE81FF` | `42`, `3.14`, `TRUE` |
| **Function Calls** | Cyan | `#66D9EF` | `filter()`, `print()`, `mean()` |
| **Function Definitions** | Green | `#A6E22E` | `my_function <-` |
| **Variables** | White | `#F8F8F8` | `x`, `data`, `result` |
| **Parameters** | Orange italic | `#FD971F` | Function argument names |
| **Headers** | Green bold | `#A6E22E` | `# Markdown headers` |

## Testing Instructions

### In Positron (Primary Target)
1. Open any test file in Positron
2. Verify syntax highlighting matches expected colors
3. Pay special attention to:
   - R pipe operators (`|>`) should be pink
   - Function calls should be cyan
   - Variable assignments should be white
   - Namespace operators (`dplyr::filter`) should show package in green, `::` in pink, function in cyan

### In VSCode
1. Install the theme extension
2. Open test files and compare with Positron
3. Note any differences (some are expected due to different language grammars)

### In Quarto Documents
1. Open `theme_test.qmd` in Positron
2. Verify embedded R code chunks match standalone R files
3. Check that Python and Observable chunks are properly highlighted
4. Confirm markdown headers are green, not red

## Validation

Run the validation script to check theme integrity:

```bash
cd ..
uv run python validate_theme.py
```

Or use the justfile command:

```bash
just validate
```

This checks for:
- Duplicate scope definitions
- Color conflicts
- Coverage analysis

## Theme Maintenance

When modifying the theme:

1. Test changes with these demo files
2. Run validation: `just validate`
3. Update version: follows pattern in `CLAUDE.md`
4. Rebuild and reinstall: `just install`

## File Organization

```
demo/
├── README.md              # This file
├── theme_test.qmd          # Comprehensive Quarto test
├── theme_test.R            # R-specific syntax test  
└── test_python.py          # Python syntax test
```

Keep this directory updated as the theme evolves to ensure comprehensive testing coverage.