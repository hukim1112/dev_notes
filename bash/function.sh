string_test() {
    echo "string test"
}

function string_test1() {
    echo "string test 2"
    echo "인자값: ${0}" # function name
}

function string_test1() {
    echo "string test 1"
    echo "인자값: ${1}" # first argument
}

function string_test2() {
    echo "string test 2"
    echo "인자값: ${@}" # every argument
}
string_test
string_test1 "hello" "world"
string_test2 "hello" "world"
