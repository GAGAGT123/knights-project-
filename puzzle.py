from logic import *

# تعريف الرموز لكل شخصية
AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")
BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")
CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# المعرفة الأساسية: كل شخص إما فارس أو كاذب
knowledge = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave))
)

# اللغز 0: A يقول "أنا فارس وكاذب في نفس الوقت"
knowledge0 = And(
    knowledge,
    Implication(AKnight, And(AKnight, AKnave)),  # إذا كان فارساً، كلامه صحيح
    Implication(AKnave, Not(And(AKnight, AKnave)))  # إذا كان كاذباً، كلامه خطأ
)

# اللغز 1: A يقول "كلانا كاذبان"، B لا يقول شيئاً
knowledge1 = And(
    knowledge,
    Implication(AKnight, And(AKnave, BKnave)),
    Implication(AKnave, Not(And(AKnave, BKnave)))
)

# اللغز 2: A يقول "نحن من نفس النوع"، B يقول "نحن من نوع مختلف"
knowledge2 = And(
    knowledge,
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),
    Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),
    Implication(BKnave, Not(Or(And(AKnight, BKnave), And(AKnave, BKnight))))
)

# اللغز 3: أكثر تعقيداً
knowledge3 = And(
    knowledge,
    # A يقول إما "أنا فارس" أو "أنا كاذب" (لا نعرف أيها)
    Or(
        And(Implication(AKnight, AKnight), Implication(AKnave, Not(AKnight))),
        And(Implication(AKnight, AKnave), Implication(AKnave, Not(AKnave)))
    ),
    # B يقول "A قال 'أنا كاذب'"
    Implication(BKnight, 
        And(Implication(AKnight, AKnave), Implication(AKnave, Not(AKnave)))
    ),
    Implication(BKnave,
        Not(And(Implication(AKnight, AKnave), Implication(AKnave, Not(AKnave))))
    ),
    # B يقول "C كاذب"
    Implication(BKnight, CKnave),
    Implication(BKnave, Not(CKnave)),
    # C يقول "A فارس"
    Implication(CKnight, AKnight),
    Implication(CKnave, Not(AKnight))
)

def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    
    for puzzle_name, knowledge_base in puzzles:
        print(f"{puzzle_name}:")
        
        # تحقق من كل رمز
        for symbol in symbols:
            if model_check(knowledge_base, symbol):
                print(f"    {symbol}")

if __name__ == "__main__":
    main()

