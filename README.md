# kaprekars-routine.py

[Prompt](https://www.reddit.com/r/dailyprogrammer/comments/56tbds/20161010_challenge_287_easy_kaprekars_routine)

## Help
```
usage: kaprekars-routine.py [-h]
                            [--operation {largest_digit,descend_digits,ascend_digits,kaprekar}]
                            n

Kaprekar's Routine

positional arguments:
  n                     Number to perform operation on

optional arguments:
  -h, --help            show this help message and exit
  --operation {largest_digit,descend_digits,ascend_digits,kaprekar}, -o {largest_digit,descend_digits,ascend_digits,kaprekar}
                        Which operation to perform
```

## Examples
### ascend_digits
```
> python kaprekars-routine.py 14662 --operation ascend_digits
```

```
12466
```

### descend_digits
```
> python kaprekars-routine.py 14662 --operation descend_digits
```

```
66421
```

## largest_digit
```
python kaprekars-routine.py 14662 --operation largest_digit
```

```
6
```

## kaprekar
```
> python kaprekars-routine.py 1466 --operation kaprekar
```

```
7 steps
```
