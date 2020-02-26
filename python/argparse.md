# PYTHON USAGE NOTE

## 1. argument parsing

```
import argparse

# 1. create a parser
# The ArgumentParser object will hold all the information necessary 
# to parse the command line into Python data types.

parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('X', type=int, help="What is the first number?")
# 2. Add arguments
parser.add_argument()
```

## 2. parser.add_argument

- 우선 한 번에 한 종류의 스위치를 등록할 수 있다.
- **positional argument는 반드시 들어가야 하며, 'foo' 같이 dash가 없다. 위치에 따라 parsing된다.**
- **optional argument는 '-' 또는 '--' 가 앞에 들어가야 하며, '--foo' 뒤에 값을 넣어주면 된다.**
- `name or flags` : 등록할 파라미터의 이름이나 스위치를 등록한다. “foo”, “-f”, “–foo” 등이 가능하다.
- `action`: 스위치가 주어졌을 때, 표준 동작을 정한다. 기본값은 “store”이고 이는 주어진 스위치의 옵션 값을 플래그(혹은 이름)의 키에 저장한다. 단지 on/off 개념의 스위치라면 `"store_true"`를 줄 수 있다. 또 배열형태로 저장될 복수 사용되는 스위치([[GCC의 ‘-I’ 옵션]] 같은)에는 `"append"`를 줄 수 있다. 개수만 세는 경우 “count”를 줄 수도 있고.
- `nargs` : 스위치나 파라미터가 받을 수 있는 값의 개수를 가리킨다. 이 값보다 많은 값이 들어오는 경우 무시된다. “+”로 설정하는 경우 1개 이상.
- `default`: 뒤에 별도 값이 없는 경우 디폴트로 들어갈 값
- `type`: 파싱하여 저장할 때 타입을 변경할 수 있다.
- `choices`: 리스트 형태로 전달하면, 리스트의 원소와 일치하는 것만 취한다.
- `required`: 필수 파라미터인 경우 True로 설정. 없으면 알아서 에러메시지를 표시하고 자동으로 exit한다.
- `help`: –help 옵션을 받았을 때, 표시될 메시지 목록에서 스위치의 도움말을 설정한다.
- `metavar`: usage 메시지를 출력할 때 표시할 메타변수이름을 지정해준다.
- `dest` : 스위치나 파라미터이름이 아닌 별도의 변수를 지정할 때 쓴다. 외부에서 변수를 미리 선언한 경우, 해당 변수에 값이 들어간다.



### 3. 일반적 예제

```
from __future__ import print_function
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('X', type=int,
                help="What is the first number?")
    parser.add_argument('Y', type=int,
                help="What is the second number?")

    args = parser.parse_args()
    X = args.X
    Y = args.Y
    print("%d + %d = %d" % (X, Y, X+Y))

if __name__=="__main__":
    main()
```

* 보충 설명 1) argparse.**ArgumentParser**함수를 통해 parser를 생성한다. 2) parser.**add_argument**를 이용하여 입력받고자 하는 인자의 조건을 설정한다. 3) parser.**parse_args** 함수를 통해 인자들을 파싱하여 args에 저장한다. 각 인자는 add_argument의 *type*에 지정된 형식으로 저장된다.

#### 사용 예

*실행*1 error occurs!

python argparse_example.py    
usage: argparse_example.py [-h] X Y
argparse_example.py: error: the following arguments are required: X, Y

*실행2* normally run

python argparse_example.py 3 2
3 + 2 = 5

### 4. 고급 예제

```
from __future__ import print_function
import argparse

def main():
	parser = argparse.ArgumentParser(description='This code is written for practice about argparse')
	parser.add_argument('X', type=float,
			metavar='First_number',
			help='What is the first number?')
	parser.add_argument('Y', type=float,
			metavar='Second_number',
			help='What is the second number?')
	parser.add_argument('--op', type=str, default='add',
			choices=['add','sub','mul','div'],
			help='What operation?')
	args = parser.parse_args()
	
	X = args.X
	Y = args.Y
	op = args.op
	print(calc(X,Y,op))

def calc(x, y, op):
	if op == 'add':
		return x + y
	elif op == 'sub':
		return x - y
	elif op == 'mul':
		return x * y
	elif op == 'div':
		return x / y

if __name__=="__main__":
	main()
```

* 보충 설명 
* 1) ArgumentParser에서 **description**으로 코드에 대한 소개를 작성할 수 있다. 
* 2) add_argument에서 help가 인자에 대한 설명을 적는 곳이라면, **metavar**는 인자의 이름을 명시하는데 사용된다. 3) **default**는 인자가 주어지지 않을 때의 기본값을 지정하는데에 사용된다. 
* 4) **choices**는 가능한 인자 목록을 제한하는데 사용된다. 
* 5) 연산에 대한 add_argument에서는 **dest** 옵션을 사용하지 않았다. 변수명이 지정되지 않았다면, '--op'에서 '--'만 뗀 뒷부분을 변수명으로 사용한다.

#### 사용 예

python ex_calc.py --op sub 1.2 2.2

=> -1.0