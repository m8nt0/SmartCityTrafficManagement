library(testthat)

test_that("model evaluation", {
  model <- lm(mpg ~ wt, data = mtcars)
  predictions <- predict(model, newdata = mtcars)
  expect_equal(length(predictions), nrow(mtcars))
})
