from logic import *

A = Symbol("A")
knowledge = And(
    Or(A, Not(A)),  
    Implication(A, And(A, Not(A))),
    Implication(Not(A), Not(And(A, Not(A))))
)
print("A is knight:", model_check(knowledge, A))


A = Symbol("A")
B = Symbol("B")
knowledge = And(
    Implication(A, And(Not(A), Not(B))),
    Implication(Not(A), Not(And(Not(A), Not(B)))))

print("A is knight:", model_check(knowledge, A))
print("B is knight:", model_check(knowledge, B))


A = Symbol("A")
B = Symbol("B")
knowledge = And(
    Implication(
        A,
        Or(
            And(A, B),
            And(Not(A), Not(B))
        )
    ),
    Implication(
        Not(A),
        Not(Or(
            And(A, B),
            And(Not(A), Not(B))
        ))
    ),
    Implication(
        B,
        Or(
            And(A, Not(B)),
            And(Not(A), B)
        )
    ),
    Implication(
        Not(B),
        Not(Or(
            And(A, Not(B)),
            And(Not(A), B)
        ))
    )
)
print("A is knight:", model_check(knowledge, A))
print("B is knight:", model_check(knowledge, B))