package governance

default allow = true

den y[msg] {
    input.category_weight_total != 100
    msg := "Category weights must sum to 100%"
}