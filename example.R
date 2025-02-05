# Hello world!

# We can do math with + - * / and ^
1 + 10 - 4 # Addition and subtraction
936 / 12 # Division
7 * 12 # Multiplication
2^10 # Exponents
10 %% 3 # Modulo, "division with rest"
1.01 * 3.2 # R uses the period (.) as a decimal separator!
-3 * 4 # Negative numbers use the same symbol as subtraction

# Common mathematical functions are also available
sin(13) + cos(2 * pi) # sine and cosine
exp(1.3234) # exponential function, e
pi # The value of pi up to some threshold
726 + 1234 # fine
"Hello" + "world" # not fine
2 + "2" # Also not fine

# We can store values in variables using <- or =
age <- 30 # Very common and "normal" in the R community
age = 30 # Very common and "normal" in basically every other language!

# We can do math with variables as with the numbers
age + 1

# We can change variables by reassigning them
age <- age + 1
age

height_cm <- 182
height_m <- height_cm / 100

# We can also manually delete variables
rm(height_cm)
height_cm

library(gapminder)

gapminder |>
  mutate(life_expectancy = lifeExp) |>
  ggplot(aes(x = year, y = life_expectancy)) +
  geom_point()

#' Roxygen comments
#' @param foo bar
#' @examples
#' foo(bar = "baz")
