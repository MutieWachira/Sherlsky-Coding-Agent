from compiler.semantic.types import (
    INT,
    STRING,
    FunctionType,
    ClassType,
)


def test_primitive():

    assert INT.name == "int"

    assert STRING.name == "str"


def test_function():

    t = FunctionType(
        name="login",
        parameters=[STRING],
        returns=INT,
    )

    assert t.returns == INT

    assert len(t.parameters) == 1


def test_class():

    cls = ClassType("User")

    cls.fields["name"] = STRING

    assert "name" in cls.fields
