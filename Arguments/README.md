## Simple argparse 
```py
import argparse
```

## Creating Parser 
```py
parser = argparse.ArgumentParser(
	description='DESCRIPTION:  this tool is a very fast tool for fuzzing',
 	usage='file.py <url> [OPTIONS]',
 	add_help=True
 	)

```

## add Positional arguemnt 
```py
parser.add_argument('URL', help="Specify the URL")
```


## add argument with another type (Default str), so you can do Math operations 
```py
parser.add_argument('-n', metavar='number', help='input a number', type=int)
```

## add long Option
```py
parser.add_argument('--verbose', help="increase output verbosity", action='store_true')  
```
## add short Option

```py
parser.add_argument("-v", help="increase output verbosity", action="store_true")
```

## changing verbosity level 
```py
parser.add_argument('-V', help='Verbosity Level', action='count', default=0)
```	

## add long & short option
```py
parser.add_argument("-hf", '--hidden-files', help="list only hidden files", action="store_false")
```

## Parse arguments
```py
args = parser.parse_args()
```


## Manage conflicts 
```py
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
```
![conflict](images/fast-slow)

## show results 
```py
print(f'all the arguments: {args}')
print(f'URL: {args.URL}')
print(f'Math Operations: {args.n}^2 = {args.n**2}')
print(f'not Verbosity: {args.verbose}')
print(f'verbose? (long option): {args.verbose}')
print(f'verbose? (short option): {args.v}')
print(f'hidden files: {args.hidden_files}') # note: this is hidden_files not hidden-files like line # note: you can't use the short options if there is long -> can't use  args.hf because args.hidden_files exists
print(f'mode: {"fast" if args.fast else "slow"}')
```
![help](images/help)
![test](images/test)

