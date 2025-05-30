# ============================================================================
# Monokai Spacegray Eighties Theme Test File
# Test all syntax highlighting elements for consistency between VSCode/Positron
# ============================================================================

# Comments should be italic gray (#808080)
#! Alert comments (if Better Comments extension is used)
# TODO: Fix this issue
#* Important note
#' Roxygen documentation comment
#' @param x A parameter description
#' @return Some return value
#' @examples
#' my_function(x = 5)

# ============================================================================
# OPERATORS - All should be pink (#F92672)
# ============================================================================

# Arithmetic operators
x <- 10 + 5 - 2 * 3 / 4^2
y <- 10 %% 3 # modulo
z <- 10 %/% 3 # integer division

# Assignment operators (should be pink)
a <- 5 # preferred in R
b = 10 # also valid
c <<- 15 # global assignment
d ->> e # rightward assignment

# Comparison operators
x == y # equality
x != y # inequality
x < y & x > z # less than, greater than with logical AND
x <= y | x >= z # less/greater equal with logical OR
x %in% c(1, 2, 3) # membership operator (should be pink!)

# Pipe operators (should be pink!)
data |> # native pipe (R 4.1+)
  filter() %>% # magrittr pipe
  select()

# Logical operators
!TRUE # negation
TRUE && FALSE # short-circuit AND
TRUE || FALSE # short-circuit OR

# ============================================================================
# NUMBERS AND CONSTANTS - Should be purple (#AE81FF)
# ============================================================================

# Numbers
integer_num <- 42L
decimal_num <- 3.14159
scientific <- 1.23e-4
negative <- -99.9

# Built-in constants
pi # mathematical constant
TRUE # boolean true
FALSE # boolean false
NULL # null value
NA # missing value
Inf # infinity
NaN # not a number

# ============================================================================
# STRINGS - Should be yellow (#E6DB74)
# ============================================================================

# Basic strings
single_quote <- 'Hello world'
double_quote <- "Hello world"
multiline <- "This is a
multiline string"

# String with escapes (escapes should be purple)
escaped <- "Line 1\nLine 2\tTabbed"
quoted <- "She said \"Hello\""

# Raw strings
raw_string <- r"(Raw string with \n no escapes)"

# ============================================================================
# FUNCTIONS - User functions green (#A6E22E), Built-ins cyan (#66D9EF)
# ============================================================================

# User-defined function (name should be green)
my_function <- function(x, y = 10, ...) {
  # parameters should be orange italic
  # Function body
  result <- x + y
  return(result)
}

# Function calls
my_result <- my_function(5, 20) # my_function should be green

# Built-in functions (should be cyan)
length(c(1, 2, 3))
mean(c(1, 2, 3, 4, 5))
sum(1:10)
print("Hello")
paste("Hello", "world", sep = " ")

# Base R functions
data.frame(x = 1:5, y = letters[1:5])
list(a = 1, b = 2, c = 3)
matrix(1:12, nrow = 3, ncol = 4)

# Statistical functions
rnorm(100, mean = 0, sd = 1)
lm(mpg ~ wt, data = mtcars)
summary(mtcars)

# ============================================================================
# CONTROL STRUCTURES - Keywords should be pink (#F92672)
# ============================================================================

# Conditional statements
if (x > 0) {
  print("Positive")
} else if (x < 0) {
  print("Negative")
} else {
  print("Zero")
}

# Loops
for (i in 1:10) {
  if (i %% 2 == 0) next # next/break should be pink
  print(i)
  if (i > 5) break
}

while (x > 0) {
  x <- x - 1
}

repeat {
  if (runif(1) > 0.9) break
}

# Switch statement
switch(x, "1" = "one", "2" = "two", "default")

# ============================================================================
# PACKAGES AND NAMESPACING
# ============================================================================

# Library calls
library(dplyr) # dplyr should be green (module name)
require(ggplot2) # ggplot2 should be green

# Namespace operators
dplyr::filter # :: should be pink, dplyr green, filter cyan
base:::print # ::: for internal functions

# ============================================================================
# DATA MANIPULATION PIPELINE (Real-world example)
# ============================================================================

library(gapminder)
library(dplyr)
library(ggplot2)

# This should show the theme in action with a realistic data pipeline
result <- gapminder |> # |> should be pink
  filter(year >= 1990) |> # filter should be cyan (built-in)
  mutate(
    # mutate should be cyan
    life_expectancy = lifeExp, # = should be pink
    gdp_billions = gdpPercap * pop / 1e9 # * / should be pink
  ) |>
  group_by(continent, year) |> # group_by should be cyan
  summarise(
    # summarise should be cyan
    avg_life_exp = mean(life_expectancy), # mean should be cyan
    total_gdp = sum(gdp_billions), # sum should be cyan
    .groups = "drop" # .groups should be white
  ) |>
  arrange(desc(total_gdp)) # arrange, desc should be cyan

# Plotting
plot <- result |>
  ggplot(aes(x = year, y = avg_life_exp, color = continent)) + # + should be pink
  geom_line(size = 1.2) + # geom_line should be cyan
  geom_point(alpha = 0.7) + # alpha should be white
  labs(
    # labs should be cyan
    title = "Life Expectancy Trends", # strings should be yellow
    x = "Year",
    y = "Average Life Expectancy"
  ) +
  theme_minimal() # theme_minimal should be cyan

# Print the plot
print(plot)

# ============================================================================
# ADVANCED R FEATURES
# ============================================================================

# Environments and objects
my_env <- new.env()
my_env$variable <- "value"

# S3 Classes
my_object <- structure(
  list(data = 1:10),
  class = "my_class"
)

# Error handling
tryCatch(
  {
    result <- risky_operation()
  },
  error = function(e) {
    message("An error occurred: ", e$message)
  },
  warning = function(w) {
    message("A warning occurred: ", w$message)
  },
  finally = {
    cleanup()
  }
)

# Anonymous functions
lapply(1:5, function(x) x^2) # function should be pink
Map(function(x, y) x + y, 1:3, 4:6) # function should be pink

# Modern anonymous function syntax (R 4.1+)
sapply(1:5, \(x) x^2) # \( should be pink

# ============================================================================
# END OF TEST FILE
# ============================================================================

# If this file looks correct with the following colors:
# - Comments: italic gray (#808080)
# - Operators (+, -, |>, %in%, etc.): pink (#F92672)
# - Variables: pink (#F92672)
# - User functions: green (#A6E22E)
# - Built-in functions: cyan (#66D9EF)
# - Strings: yellow (#E6DB74)
# - Numbers/constants: purple (#AE81FF)
# - Keywords (if, for, function): pink (#F92672)
# Then the theme is working correctly!
