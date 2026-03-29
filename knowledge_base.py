"""
╔══════════════════════════════════════════════════════════════════════╗
║  knowledge_base.py — Advanced Mathematics Assistant V2              ║
║                                                                      ║
║  Contains:                                                           ║
║    1. CLASS_EXAMPLES  → sidebar dropdown data (112 chapters)        ║
║    2. MATH_KNOWLEDGE_BASE → all NCERT documents for RAG             ║
║                                                                      ║
║  Current coverage:                                                   ║
║    ✅ Class 6  — 14 chapters                                        ║
║    🔜 Class 7  — coming next session                                ║
║    🔜 Class 8  — coming next session                                ║
║    🔜 Class 9  — coming next session                                ║
║    🔜 Class 10 — coming next session                                ║
║    🔜 Class 11 — coming next session                                ║
║    🔜 Class 12 — coming next session                                ║
║    🔜 JEE Advanced — coming next session                            ║
║                                                                      ║
║  HOW TO ADD MORE:                                                    ║
║    Just append more Document(...) objects to MATH_KNOWLEDGE_BASE    ║
║    Then run: python3.11 main.py --rebuild                           ║
╚══════════════════════════════════════════════════════════════════════╝
"""

try:
    from langchain_core.documents import Document
except ImportError:
    try:
        from langchain.schema import Document
    except ImportError:
        class Document:
            def __init__(self, page_content: str, metadata: dict = None):
                self.page_content = page_content
                self.metadata = metadata or {}


# ════════════════════════════════════════════════════════════════════
#  SECTION 1 — CLASS_EXAMPLES
#  Used by sidebar dropdown. One sample question per chapter.
#  Structure: { "Class Name": { "Ch· Title": "question..." } }
# ════════════════════════════════════════════════════════════════════

CLASS_EXAMPLES = {

    "📘 Class 6": {
        "Ch1 · Knowing Our Numbers":      "Write 5,08,01,592 in words and find the difference between place value and face value of 8 in this number",
        "Ch2 · Whole Numbers":            "Show 3 + 4 = 4 + 3 and 2 × (3 + 4) = 2×3 + 2×4 on a number line and explain the properties used",
        "Ch3 · Playing With Numbers":     "Find HCF and LCM of 36 and 48 using prime factorisation method step by step",
        "Ch4 · Basic Geometrical Ideas":  "Define point, line, line segment, ray and angle with diagrams. What is the difference between a line and a line segment?",
        "Ch5 · Elementary Shapes":        "Classify angles: 35°, 90°, 120°, 180°, 270°. Name the type of triangle with sides 3cm, 4cm, 5cm",
        "Ch6 · Integers":                 "Solve using number line: (-5) + 8, 3 - (-4), (-6) + (-2). Explain rules for addition of integers",
        "Ch7 · Fractions":                "Solve: 3/4 + 5/6 - 1/3. Also arrange 2/3, 3/4, 5/8, 7/12 in ascending order",
        "Ch8 · Decimals":                 "Convert 2.375 to fraction. Multiply 3.25 × 1.4 and divide 8.64 ÷ 0.6 with full steps",
        "Ch9 · Data Handling":            "Find mean, median and mode of: 12, 15, 11, 18, 15, 13, 20, 15, 10. Draw a bar graph",
        "Ch10 · Mensuration":             "Find perimeter and area of a rectangle 15cm × 8cm and a square of side 9cm",
        "Ch11 · Algebra":                 "Write expressions for: 5 added to 3 times x, y subtracted from 10. Find value when x=4, y=3",
        "Ch12 · Ratio and Proportion":    "Divide 720 between Arjun and Bharat in ratio 4:5. Check if 3:4 and 9:12 are in proportion",
        "Ch13 · Symmetry":                "How many lines of symmetry: equilateral triangle, square, rectangle, circle, regular hexagon?",
        "Ch14 · Practical Geometry":      "Construct a line segment of 6.5cm. Draw perpendicular bisector and angle bisector of 60°",
    },

    "📗 Class 7": {
        "Ch1 · Integers":                 "Evaluate: (-8) × (-5), (-36) ÷ 4, (-7) × 8 + (-7) × 2. State properties of multiplication of integers",
        "Ch2 · Fractions and Decimals":   "Multiply 2(3/4) × 1(1/3) and divide 3(1/2) ÷ 1(2/3). Convert 0.125, 1.625 to fractions",
        "Ch3 · Data Handling":            "Find mean of first 10 natural numbers. Find mode and median of: 4,7,2,9,4,8,4,6. Probability of even number on die?",
        "Ch4 · Simple Equations":         "Solve: 2x + 7 = 19, 3(y - 4) = 2y + 1, (x+2)/3 = (x-1)/4. Verify answers by substitution",
        "Ch5 · Lines and Angles":         "Two parallel lines cut by transversal. If one angle is 65°, find all 8 angles and name each pair",
        "Ch6 · Triangle Properties":      "In triangle ABC, angle A=50°, angle B=70°. Find angle C. Verify exterior angle theorem",
        "Ch7 · Congruence of Triangles":  "State all congruence rules SSS SAS ASA AAS RHS with diagrams. When can we NOT use AAA?",
        "Ch8 · Comparing Quantities":     "Find: 15% of 400, what % is 45 of 180, SP when CP=850 profit=12%, SP when CP=600 loss=8%",
        "Ch9 · Rational Numbers":         "Represent -3/5 and 7/(-4) on number line. Find 3 rational numbers between 1/4 and 1/2",
        "Ch10 · Practical Geometry":      "Construct triangle PQR where PQ=5cm, QR=4.5cm, angle Q=60° using compass and ruler",
        "Ch11 · Perimeter and Area":      "Find area of parallelogram base 8cm height 5cm. Find circumference and area of circle r=7cm",
        "Ch12 · Algebraic Expressions":   "Add 3x²+2x-5 and x²-3x+2. Subtract 2a-3b from 5a+2b. Find value of 2x²-3x+1 when x=2",
        "Ch13 · Exponents and Powers":    "Simplify: 2⁵×2³, 3⁷÷3⁴, (2³)², 2³×5³. Express 48000000 in standard form",
        "Ch14 · Symmetry":                "Find order of rotational symmetry of square, rectangle, equilateral triangle, circle, regular pentagon",
        "Ch15 · Solid Shapes":            "Draw nets for cube, cuboid, triangular prism. Find faces, edges, vertices. Verify Euler's formula F+V-E=2",
    },

    "📙 Class 8": {
        "Ch1 · Rational Numbers":         "Find 5 rational numbers between -1/2 and 1/3. Verify commutativity for -2/3 and 4/5",
        "Ch2 · Linear Equations":         "Solve: (2x+3)/5 - (x-4)/3 = 2. A number is 4 more than twice another and their sum is 40",
        "Ch3 · Quadrilaterals":           "In parallelogram ABCD, angle A=75°. Find all angles. State properties of rhombus and kite",
        "Ch4 · Practical Geometry":       "Construct quadrilateral ABCD: AB=4cm, BC=3.5cm, CD=4.5cm, DA=3cm, AC=5cm",
        "Ch5 · Data Handling":            "Draw pie chart: Wheat 40%, Rice 30%, Maize 20%, Others 10%. Find probability of red card from 52",
        "Ch6 · Squares and Square Roots": "Find square root of 1764 by prime factorisation and long division. Is 1352 a perfect square?",
        "Ch7 · Cubes and Cube Roots":     "Find cube root of 13824 by prime factorisation. Find smallest multiplier to make 675 a perfect cube",
        "Ch8 · Comparing Quantities":     "Find CI on 12000 at 10% per year for 2 years compounded annually. Compare with SI",
        "Ch9 · Algebraic Identities":     "Expand: (3x+2y)², (4a-3b)², (x+3)(x-3), (2x+3)(2x+5). Factorise: x²+8x+16, 9a²-12ab+4b²",
        "Ch10 · Solid Shapes":            "Draw top view, front view and side view of cube, cylinder and cone",
        "Ch11 · Mensuration":             "Find area of trapezium parallel sides 8cm and 5cm height 4cm. Surface area of cuboid 5×4×3cm",
        "Ch12 · Exponents and Powers":    "Simplify: (2⁻³ × 3⁻²)/(6⁻¹), (5/3)⁻² × (3/5)³. Express 0.00000605 in standard form",
        "Ch13 · Direct Inverse Proportion":"8 workers finish in 12 days. How many days for 6 workers? If 15 bags cost 450, cost of 24 bags?",
        "Ch14 · Factorisation":           "Factorise: 12x²y-9xy²+6xyz, a²-b²+a-b, x²+7x+12, 2x²+7x+3 using splitting the middle term",
        "Ch15 · Introduction to Graphs":  "Plot A(2,3), B(-1,4), C(0,-2). Draw graph of x+y=5 and find where it cuts both axes",
        "Ch16 · Playing With Numbers":    "A 2-digit number is 4 times sum of its digits. If 18 is added digits reverse. Find the number",
    },

    "📒 Class 9": {
        "Ch1 · Number Systems":           "Prove √2 is irrational. Represent √5 on number line. Rationalise 3/(2+√3) and 5/(√7-√2)",
        "Ch2 · Polynomials":              "Find remainder when x³-6x²+11x-6 is divided by x-2. Factorise x³-23x²+142x-120",
        "Ch3 · Coordinate Geometry":      "Plot A(3,4), B(-2,3), C(-4,-1), D(2,-3). Find which quadrant. Find distance AB",
        "Ch4 · Linear Equations 2 Var":   "Draw graph of 2x+3y=12. Find x-intercept and y-intercept. Find 3 solutions",
        "Ch5 · Euclid's Geometry":        "State Euclid's 5 postulates. Explain parallel postulate. Give 2 theorems from postulates",
        "Ch6 · Lines and Angles":         "Prove vertically opposite angles are equal. Find all 8 angles when parallel lines cut by transversal",
        "Ch7 · Triangles":                "Prove angles opposite equal sides of isosceles triangle are equal. State and prove ASA rule",
        "Ch8 · Quadrilaterals":           "Prove diagonals of parallelogram bisect each other. Prove mid-point theorem",
        "Ch9 · Areas Parallelogram":      "Prove parallelograms on same base and between same parallels are equal. Area of parallelogram base 8cm",
        "Ch10 · Circles":                 "Prove equal chords subtend equal angles at centre. Prove angle in semicircle is 90°",
        "Ch11 · Constructions":           "Construct triangle with perimeter 11cm and base angles 60° and 45°",
        "Ch12 · Heron's Formula":         "Find area of triangle with sides 13cm, 14cm, 15cm using Heron's formula",
        "Ch13 · Surface Areas Volumes":   "Find total surface area and volume of cone r=5cm l=13cm. Surface area of sphere r=7cm",
        "Ch14 · Statistics":              "Find mean by assumed mean method. Find median and mode for grouped data",
        "Ch15 · Probability":             "Bag has 5 red, 7 blue, 3 green balls. Find probability of red, not blue, green or red",
    },

    "📓 Class 10": {
        "Ch1 · Real Numbers":             "Prove √3 is irrational. Find HCF of 96 and 404 by Euclid's algorithm",
        "Ch2 · Polynomials":              "Find zeroes of 6x²-3-7x and verify α+β=-b/a and αβ=c/a. Find cubic polynomial with zeroes 2,-1,-3",
        "Ch3 · Pair of Linear Equations": "Solve by cross-multiplication: 2x+3y=11, 2x-4y=-24. Solve graphically and find area of triangle",
        "Ch4 · Quadratic Equations":      "Solve 2x²-7x+3=0 by factorisation, completing square and quadratic formula. Find nature of roots",
        "Ch5 · Arithmetic Progressions":  "Find sum of first 40 positive integers divisible by 6. If 7th term is 34 and 13th term is 64, find AP",
        "Ch6 · Triangles":                "State and prove Basic Proportionality Theorem. Prove area ratio equals square of side ratio",
        "Ch7 · Coordinate Geometry":      "Find area of triangle A(2,3), B(-1,0), C(2,-4). Find point dividing (1,3)-(4,6) in ratio 2:1",
        "Ch8 · Introduction to Trig":     "If sinθ=3/5 find all trig ratios. Prove sin²θ+cos²θ=1. Evaluate 2tan²45°+cos²30°-sin²60°",
        "Ch9 · Applications of Trig":     "From top of 75m tower angles of depression of two boats are 30° and 45°. Find distance between boats",
        "Ch10 · Circles":                 "Prove tangent is perpendicular to radius. Find length of tangent from point 17cm from centre radius 8cm",
        "Ch11 · Constructions":           "Divide 7cm in ratio 3:2. Draw tangents from point 10cm from centre r=4cm",
        "Ch12 · Areas Related to Circles":"Find area of sector r=14cm angle 60°. Find area of segment. Area when square inscribed in circle r=10cm",
        "Ch13 · Surface Areas Volumes":   "Solid is cone on hemisphere r=3.5cm cone height 4cm. Find total surface area and volume",
        "Ch14 · Statistics":              "Find mean by step deviation. Find median and mode. Verify mode=3median-2mean",
        "Ch15 · Probability":             "Two dice thrown. Find probability sum is 8, sum is prime, same number on both dice",
    },

    "📕 Class 11": {
        "Ch1 · Sets":                     "If A={1,2,3,4,5} B={2,4,6,8} find A∪B, A∩B, A-B, B-A. Verify n(A∪B)=n(A)+n(B)-n(A∩B)",
        "Ch2 · Relations and Functions":  "Find domain and range of f(x)=√(9-x²). Find fog and gof if f(x)=2x+1 and g(x)=x²-1",
        "Ch3 · Trigonometric Functions":  "Prove sin(A+B)sin(A-B)=sin²A-sin²B. Solve 2cos²x-3cosx+1=0. Find general solution of sinx=√3/2",
        "Ch4 · Math Induction":           "Prove by PMI: 1+2+3+...+n=n(n+1)/2. Prove 2ⁿ>n for all n≥1 and 4ⁿ-1 is divisible by 3",
        "Ch5 · Complex Numbers":          "Find modulus and argument of z=-1+i√3. Express in polar form. Find cube roots of unity",
        "Ch6 · Linear Inequalities":      "Solve 3x-2>2x+1 and show on number line. Solve system x+y≤10, x+3y≤15, x≥0, y≥0",
        "Ch7 · Permutations Combinations":"5 boys and 3 girls sit in row if girls always together. Find ⁷C₃. Prove ⁿCᵣ+ⁿCᵣ₋₁=ⁿ⁺¹Cᵣ",
        "Ch8 · Binomial Theorem":         "Expand (2x-3y)⁴. Find 5th term in (x+2)⁸. Find term independent of x in (x+1/x)¹⁰",
        "Ch9 · Sequences and Series":     "Find sum of GP 1+3+9+...+2187. If AM=10 and GM=8 find the numbers. Find ∑(2k+1) k=1 to 20",
        "Ch10 · Straight Lines":          "Find equation through (2,-3) perpendicular to 3x-4y+5=0. Distance between 3x+4y-5=0 and 3x+4y+15=0",
        "Ch11 · Conic Sections":          "Find focus directrix latus rectum of y²=12x. Equation of ellipse with foci (±3,0) and a=5",
        "Ch12 · 3D Geometry":             "Find distance between A(1,2,3) and B(4,-2,6). Find point dividing AB in ratio 2:1",
        "Ch13 · Limits and Derivatives":  "Find lim(x→0) sin3x/x. Differentiate x³sinx. Find derivative of (x²+1)/(x²-1)",
        "Ch14 · Math Reasoning":          "Write negation of: All primes are odd. Write converse, inverse, contrapositive of: If x>5 then x²>25",
        "Ch15 · Statistics":              "Find variance and standard deviation of 6,8,10,12,14. Compare variability using coefficient of variation",
        "Ch16 · Probability":             "P(A)=0.4, P(B)=0.5, P(A∩B)=0.2. Find P(A∪B) and P(A|B). Card drawn — find P(red or king)",
    },

    "📔 Class 12": {
        "Ch1 · Relations and Functions":  "Show f(x)=2x+3 is bijective. Find inverse. Is R={(a,b): a-b divisible by 5} an equivalence relation?",
        "Ch2 · Inverse Trig Functions":   "Find sin⁻¹(-1/2), cos⁻¹(-√3/2), tan⁻¹(√3). Prove sin⁻¹x+cos⁻¹x=π/2",
        "Ch3 · Matrices":                 "If A=[[1,2],[3,4]] find A+Aᵀ and show it is symmetric. Express A as sum of symmetric and skew-symmetric",
        "Ch4 · Determinants":             "Find determinant of 3×3 matrix. Find inverse using adjoint. Solve using Cramer's rule: x+y+z=6, 2x-y+z=3",
        "Ch5 · Continuity Differentiability":"Check continuity of |x-3| at x=3. Differentiate x^x, sin(logx), e^(x²). Find d²y/dx² for parametric",
        "Ch6 · Applications of Derivatives":"Find intervals where 2x³-9x²+12x-5 is increasing. Find local maxima minima. Two numbers sum 24 max product",
        "Ch7 · Integrals":                "Evaluate ∫x²eˣdx by parts, ∫dx/(x²-4) by partial fractions, ∫sin³x dx. Use ILATE rule",
        "Ch8 · Application of Integrals": "Find area bounded by y=x² and y=x+2. Area of circle x²+y²=16. Area between y=x² and x=y²",
        "Ch9 · Differential Equations":   "Solve dy/dx=(x²+y²)/2xy (homogeneous). Solve linear DE dy/dx+2y/x=x². Solve eˣ⁺ʸ variable separable",
        "Ch10 · Vector Algebra":          "If a=2i+3j-k and b=i-2j+3k find a·b, a×b, angle between them. Find unit vector",
        "Ch11 · 3D Geometry":             "Find angle between lines x-1/2=y+1/3=z-2/6 and x+2/1=y-3/4=z+1/2. Distance from (1,2,3) to plane 2x-3y+z=5",
        "Ch12 · Linear Programming":      "Maximise Z=3x+4y subject to x+y≤450, 2x+y≤600, x≥0, y≥0. Find all corner points",
        "Ch13 · Probability":             "Bag A has 3 red 5 black. Bag B has 4 red 6 black. One bag chosen, one ball drawn is red. P(ball from A)?",
    },

    "🏆 JEE Advanced": {
        "Definite Integrals":             "Evaluate ∫₀^π x·sinx/(1+cos²x) dx using King's rule. Show full working",
        "Complex Numbers":                "If z=(√3+i)/(1-i√3), find |z|, arg(z) and polar form. Find z¹⁰ using De Moivre's theorem",
        "Theory of Equations":            "If roots of x³-6x²+11x-6=0 are in AP find them. For ax²+bx+c=0 both roots in (1,2) — find conditions",
        "Binomial Advanced":              "Find sum C(n,0)²+C(n,1)²+...+C(n,n)². Find greatest term in (3+2x)¹⁰ when x=3/2",
        "Advanced Trigonometry":          "Solve sin2x-sinx=cosx-cos2x for x in [0,2π]. Prove cos(π/7)·cos(2π/7)·cos(3π/7)=1/8",
        "Vectors and 3D Advanced":        "Find shortest distance between skew lines r=(i+j)+t(2i-j+k) and r=(2i+j-k)+s(3i-5j+2k)",
        "Probability Advanced":           "4 cards drawn without replacement. Find P(all suits represented). P(exactly 2 aces)",
        "Inequalities":                   "Prove AM≥GM for 3 positive numbers. Find minimum of (x+1/x)²+(y+1/y)² for positive x,y with xy=1",
    },
}


# ════════════════════════════════════════════════════════════════════
#  SECTION 2 — MATH_KNOWLEDGE_BASE
#  RAG documents. Each Document = one NCERT chapter.
#  Format: concepts → formulas → solved examples → common mistakes
# ════════════════════════════════════════════════════════════════════

MATH_KNOWLEDGE_BASE = [

    # ────────────────────────────────────────────────────────────────
    #  CLASS 6 — All 14 Chapters
    # ────────────────────────────────────────────────────────────────

    Document(page_content="""Class 6 | Ch1: Knowing Our Numbers

KEY CONCEPTS:
Indian number system uses periods: ones, thousands, lakhs, crores.
International system uses: ones, thousands, millions, billions.
Place value of a digit = digit × position value.
Face value of a digit = digit itself regardless of position.

INDIAN PLACE VALUE CHART:
Crores | Ten Lakhs | Lakhs | Ten Thousands | Thousands | Hundreds | Tens | Ones
For number 5,08,01,592:
- 5 is in crores place → place value = 5,00,00,000
- 8 is in lakhs place → place value = 8,00,000
- Face value of 8 = 8 always

COMPARISON OF NUMBERS:
- More digits = greater number
- Same digits: compare from leftmost digit
- Ascending order: smallest to largest
- Descending order: largest to smallest

ESTIMATION (ROUNDING):
- Round to nearest 10: look at ones digit. ≥5 → round up, <5 → round down
- Round to nearest 100: look at tens digit
- Round to nearest 1000: look at hundreds digit

ROMAN NUMERALS:
I=1, V=5, X=10, L=50, C=100, D=500, M=1000
Rules: smaller before larger = subtract (IV=4, IX=9, XL=40, XC=90)
Smaller after larger = add (VI=6, XI=11, LX=60)

SOLVED EXAMPLES:
Example 1: Write 7,35,02,814 in words
= Seven crore thirty-five lakh two thousand eight hundred fourteen

Example 2: Place value vs face value of 6 in 56,43,218
Place value of 6 = 6,00,000 (six lakhs position)
Face value of 6 = 6

COMMON MISTAKES:
- Confusing place value (depends on position) with face value (always the digit)
- Forgetting commas in Indian system (groups of 2 after first 3)
- In International system groups are always 3: 7,350,281""",
    metadata={"source": "ncert", "topic": "numbers", "class_level": "class_6", "chapter": "ch1", "difficulty": "beginner"}),

    Document(page_content="""Class 6 | Ch2: Whole Numbers

KEY CONCEPTS:
Natural Numbers: 1, 2, 3, 4, 5, ... (counting numbers)
Whole Numbers: 0, 1, 2, 3, 4, 5, ... (natural numbers + zero)
Every natural number is a whole number. 0 is a whole number but NOT a natural number.
Predecessor of n = n - 1. Successor of n = n + 1.

NUMBER LINE:
- Whole numbers on number line go from 0 to the right
- Each number is 1 unit apart
- Addition = move right. Subtraction = move left.

PROPERTIES OF WHOLE NUMBERS:
Closure: a + b and a × b are always whole numbers (NOT subtraction or division)
Commutativity: a + b = b + a, a × b = b × a
Associativity: (a+b)+c = a+(b+c), (a×b)×c = a×(b×c)
Distributivity: a × (b + c) = a×b + a×c
Identity: a + 0 = a (additive identity = 0), a × 1 = a (multiplicative identity = 1)
Zero property: a × 0 = 0

PATTERNS IN WHOLE NUMBERS:
Triangular numbers: 1, 3, 6, 10, 15, ... (n(n+1)/2)
Square numbers: 1, 4, 9, 16, 25, ...

SOLVED EXAMPLES:
Example 1: Verify distributivity: 12 × (7 + 3) = 12×7 + 12×3
LHS = 12 × 10 = 120
RHS = 84 + 36 = 120 ✓

Example 2: Find sum 1 + 2 + 3 + ... + 100 using pattern
= 100 × 101 / 2 = 5050

COMMON MISTAKES:
- Thinking 0 is a natural number (it is NOT)
- Subtraction and division are NOT closed for whole numbers: 3 - 5 = -2 (not whole)
- Division by zero is undefined""",
    metadata={"source": "ncert", "topic": "numbers", "class_level": "class_6", "chapter": "ch2", "difficulty": "beginner"}),

    Document(page_content="""Class 6 | Ch3: Playing With Numbers (HCF and LCM)

KEY CONCEPTS:
Factor: a divides b exactly → a is factor of b. Example: factors of 12 = 1,2,3,4,6,12
Multiple: b = a × n for some integer n → b is multiple of a
Prime number: exactly 2 factors (1 and itself). Examples: 2,3,5,7,11,13,17,19,23
Composite number: more than 2 factors. Examples: 4,6,8,9,10,12
1 is neither prime nor composite. 2 is the only even prime.

DIVISIBILITY RULES:
÷2: last digit is 0,2,4,6,8
÷3: sum of digits divisible by 3
÷4: last two digits divisible by 4
÷5: last digit is 0 or 5
÷6: divisible by both 2 and 3
÷8: last three digits divisible by 8
÷9: sum of digits divisible by 9
÷10: last digit is 0
÷11: (sum of odd-position digits) - (sum of even-position digits) = 0 or multiple of 11

PRIME FACTORISATION (Factor Tree method):
48 = 2 × 24 = 2 × 2 × 12 = 2 × 2 × 2 × 6 = 2 × 2 × 2 × 2 × 3 = 2⁴ × 3

HCF (Highest Common Factor):
Method 1 - Prime factorisation: HCF = product of COMMON prime factors with LOWEST powers
Method 2 - Listing factors: list all factors of each number, find highest common one

LCM (Lowest Common Multiple):
Method 1 - Prime factorisation: LCM = product of ALL prime factors with HIGHEST powers
Method 2 - Division method: divide by common primes

KEY RELATIONSHIP: HCF × LCM = Product of the two numbers

SOLVED EXAMPLES:
Example 1: Find HCF and LCM of 36 and 48
36 = 2² × 3²
48 = 2⁴ × 3
HCF = 2² × 3 = 4 × 3 = 12 (common factors, lowest powers)
LCM = 2⁴ × 3² = 16 × 9 = 144 (all factors, highest powers)
Check: HCF × LCM = 12 × 144 = 1728 = 36 × 48 ✓

Example 2: Three bells ring at intervals of 6, 10, 15 minutes. When do they ring together?
LCM(6, 10, 15): 6=2×3, 10=2×5, 15=3×5
LCM = 2 × 3 × 5 = 30 minutes

COMMON MISTAKES:
- HCF uses LOWEST powers, LCM uses HIGHEST powers (students often mix these)
- 1 is a factor of every number
- HCF is always ≤ the smaller number, LCM is always ≥ the larger number""",
    metadata={"source": "ncert", "topic": "number_theory", "class_level": "class_6", "chapter": "ch3", "difficulty": "beginner"}),

    Document(page_content="""Class 6 | Ch4: Basic Geometrical Ideas

KEY CONCEPTS:
Point: exact location, no size, represented by a dot. Named by capital letters A, B, C.
Line: infinite length, no width, extends in both directions. Written as AB with arrows both ends.
Line segment: part of a line with two endpoints. Written as AB with bar on top.
Ray: starts at a point, extends infinitely in one direction. Written as AB with arrow one end.
Plane: flat surface extending infinitely in all directions.

ANGLE:
Formed by two rays with common endpoint (vertex).
Notation: ∠ABC where B is the vertex.
Types:
- Acute angle: 0° < angle < 90°
- Right angle: exactly 90°
- Obtuse angle: 90° < angle < 180°
- Straight angle: exactly 180°
- Reflex angle: 180° < angle < 360°
- Complete angle: exactly 360°

CURVES AND POLYGONS:
Simple curve: does not cross itself
Closed curve: starts and ends at same point
Polygon: closed figure made of line segments
Triangle: 3 sides. Quadrilateral: 4 sides. Pentagon: 5. Hexagon: 6.

PARTS OF A CIRCLE:
Centre: fixed point equidistant from all points on circle
Radius: line from centre to any point on circle
Diameter: chord passing through centre = 2 × radius
Chord: line segment joining any two points on circle
Arc: part of circle between two points
Sector: region between two radii and arc
Segment: region between chord and arc

SOLVED EXAMPLES:
Example 1: How many lines pass through one point? Infinite lines
How many lines pass through two points? Exactly one line

Example 2: Name all the radii, diameters and chords in a circle with centre O
and points A, B, C, D on circle where AC and BD are chords passing through O.
Radii: OA, OB, OC, OD
Diameters: AC, BD (pass through centre)
Chords: AC, BD (and any other line segment between two points on circle)

COMMON MISTAKES:
- A diameter is a chord but a chord is not always a diameter
- Radius and diameter are not the same: diameter = 2 × radius
- A line has no endpoints; a ray has one endpoint; a line segment has two""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_6", "chapter": "ch4", "difficulty": "beginner"}),

    Document(page_content="""Class 6 | Ch5: Understanding Elementary Shapes

KEY CONCEPTS:
MEASURING LINE SEGMENTS: Use ruler. Length = right end reading - left end reading.

ANGLES - MEASURING WITH PROTRACTOR:
Place centre of protractor on vertex. Align base line with one ray. Read angle from other ray.

TYPES OF TRIANGLES:
By sides:
- Equilateral: all 3 sides equal, all angles = 60°
- Isosceles: 2 sides equal, 2 base angles equal
- Scalene: all 3 sides different, all angles different
By angles:
- Acute triangle: all angles < 90°
- Right triangle: one angle = 90°
- Obtuse triangle: one angle > 90°

PYTHAGOREAN TRIPLETS (Right triangle sides):
(3,4,5): 3²+4²=9+16=25=5² ✓
(5,12,13): 25+144=169=13² ✓
(8,15,17), (7,24,25)

TYPES OF QUADRILATERALS:
Rectangle: 4 right angles, opposite sides equal
Square: 4 right angles, all sides equal
Parallelogram: opposite sides parallel and equal
Rhombus: all sides equal, opposite sides parallel
Trapezium: exactly one pair of parallel sides
Kite: two pairs of adjacent sides equal

3D SHAPES:
Cube: 6 square faces, 12 edges, 8 vertices
Cuboid: 6 rectangular faces, 12 edges, 8 vertices
Cylinder: 2 circular faces, 1 curved surface
Cone: 1 circular base, 1 curved surface, 1 apex
Sphere: 1 curved surface, no edges or vertices
Euler's formula for polyhedra: F + V - E = 2

SOLVED EXAMPLES:
Example 1: Is (3,4,5) a right triangle?
3² + 4² = 9 + 16 = 25 = 5² → YES, right triangle with hypotenuse 5

Example 2: How many faces, edges, vertices does a triangular prism have?
Faces = 5 (2 triangular + 3 rectangular)
Edges = 9, Vertices = 6
Check: F + V - E = 5 + 6 - 9 = 2 ✓

COMMON MISTAKES:
- Hypotenuse is always the LONGEST side in right triangle (opposite to 90°)
- Square is a special rectangle AND a special rhombus
- A cube is a special cuboid""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_6", "chapter": "ch5", "difficulty": "beginner"}),

    Document(page_content="""Class 6 | Ch6: Integers

KEY CONCEPTS:
Integers: ..., -4, -3, -2, -1, 0, 1, 2, 3, 4, ...
Positive integers: 1, 2, 3, ... (same as natural numbers)
Negative integers: -1, -2, -3, ...
Zero is neither positive nor negative.
Opposite of +5 is -5. Opposite of -8 is +8.

NUMBER LINE:
- Positive numbers → right of zero
- Negative numbers → left of zero
- Numbers increase going right, decrease going left
- -3 < -2 < -1 < 0 < 1 < 2 < 3

COMPARING INTEGERS:
- Positive > Zero > Negative
- Among negatives: -2 > -5 (closer to zero is greater)
- On number line: right is greater

ADDITION ON NUMBER LINE:
- Adding positive: move RIGHT
- Adding negative: move LEFT
Rule: (+) + (+) = + (add, keep sign)
Rule: (-) + (-) = - (add, keep sign)
Rule: (+) + (-) = subtract smaller from larger, keep sign of larger

SUBTRACTION OF INTEGERS:
a - b = a + (-b) (change subtraction to addition of opposite)
Examples:
5 - 8 = 5 + (-8) = -3
-3 - (-5) = -3 + 5 = 2
-4 - 7 = -4 + (-7) = -11

SOLVED EXAMPLES:
Example 1: Solve (-5) + 8 using number line
Start at -5, move 8 steps right → reach +3
Answer: (-5) + 8 = 3

Example 2: Solve 3 - (-4)
= 3 + 4 = 7
(subtracting a negative = adding positive)

Example 3: Arrange in ascending order: -8, 3, -1, 0, -5, 2
Ascending: -8 < -5 < -1 < 0 < 2 < 3

REAL LIFE USES:
- Temperature below zero: -5°C means 5 degrees below zero
- Floors below ground: basement -1, -2
- Bank: withdrawal makes account negative

COMMON MISTAKES:
- -5 is NOT greater than -2 (common error: thinking larger absolute value = greater)
- Subtracting a negative becomes positive: 5-(-3) = 5+3 = 8
- Zero is an integer but not positive or negative""",
    metadata={"source": "ncert", "topic": "numbers", "class_level": "class_6", "chapter": "ch6", "difficulty": "beginner"}),

    Document(page_content="""Class 6 | Ch7: Fractions

KEY CONCEPTS:
Fraction = part of a whole. Written as p/q where p=numerator, q=denominator (q≠0)

TYPES OF FRACTIONS:
Proper fraction: numerator < denominator. Examples: 1/2, 3/4, 5/7
Improper fraction: numerator ≥ denominator. Examples: 7/3, 5/5, 11/4
Mixed fraction: whole number + proper fraction. Example: 2(3/4) = 11/4
Unit fraction: numerator = 1. Examples: 1/2, 1/3, 1/7

EQUIVALENT FRACTIONS:
Same value, different forms: 1/2 = 2/4 = 3/6 = 4/8
To find equivalent: multiply or divide numerator and denominator by same number
Simplest form (lowest terms): HCF of numerator and denominator = 1

COMPARING FRACTIONS:
Same denominator: compare numerators (3/7 > 2/7)
Same numerator: compare denominators — smaller denominator = larger fraction (2/3 > 2/5)
Different both: convert to same denominator using LCM

OPERATIONS ON FRACTIONS:
Addition/Subtraction — Same denominator: a/c + b/c = (a+b)/c
Addition/Subtraction — Different denominator: find LCM, convert, then add

SOLVED EXAMPLES:
Example 1: Solve 3/4 + 5/6 - 1/3
LCM(4,6,3) = 12
= 9/12 + 10/12 - 4/12
= (9 + 10 - 4)/12
= 15/12 = 5/4 = 1(1/4)

Example 2: Arrange 2/3, 3/4, 5/8, 7/12 in ascending order
LCM(3,4,8,12) = 24
2/3 = 16/24, 3/4 = 18/24, 5/8 = 15/24, 7/12 = 14/24
Ascending: 14/24 < 15/24 < 16/24 < 18/24
= 7/12 < 5/8 < 2/3 < 3/4

COMMON MISTAKES:
- Adding fractions by adding numerators AND denominators separately: 1/2 + 1/3 ≠ 2/5
- Correct: 1/2 + 1/3 = 3/6 + 2/6 = 5/6
- Larger denominator means SMALLER fraction (for same numerator)""",
    metadata={"source": "ncert", "topic": "arithmetic", "class_level": "class_6", "chapter": "ch7", "difficulty": "beginner"}),

    Document(page_content="""Class 6 | Ch8: Decimals

KEY CONCEPTS:
Decimal point separates whole part from fractional part.
0.1 = 1/10 (one tenth)
0.01 = 1/100 (one hundredth)
0.001 = 1/1000 (one thousandth)

PLACE VALUE IN DECIMALS:
For number 45.378:
- 4 → tens (40)
- 5 → ones (5)
- 3 → tenths (3/10)
- 7 → hundredths (7/100)
- 8 → thousandths (8/1000)

CONVERSION:
Decimal to fraction: 0.375 = 375/1000 = 3/8 (simplify by HCF)
Fraction to decimal: 3/4 = 75/100 = 0.75 (divide numerator by denominator)

COMPARING DECIMALS:
Compare whole number part first.
If equal, compare tenths digit, then hundredths, etc.
Example: 2.35 vs 2.29 → same whole, 3>2 in tenths → 2.35 > 2.29

ADDITION AND SUBTRACTION:
Line up decimal points. Add zeros if needed. Then add/subtract normally.

MULTIPLICATION OF DECIMALS:
Multiply as whole numbers. Count total decimal places. Put decimal point in answer.
Example: 3.25 × 1.4
325 × 14 = 4550
Total decimal places = 2 + 1 = 3
Answer: 4.550 = 4.55

DIVISION OF DECIMALS:
Divide by whole number: divide normally, put decimal directly above.
Divide by decimal: multiply both by 10/100/1000 to make divisor whole.
Example: 8.64 ÷ 0.6 = 86.4 ÷ 6 = 14.4

SOLVED EXAMPLES:
Example 1: Convert 2.375 to fraction
= 2375/1000 = 19/8 = 2(3/8)

Example 2: Multiply 3.25 × 1.4
= 325 × 14 / 1000 = 4550/1000 = 4.55

Example 3: Divide 8.64 ÷ 0.6
= 86.4 ÷ 6 = 14.4

COMMON MISTAKES:
- Not aligning decimal points during addition: 2.5 + 0.35 ≠ 2.85 if not aligned
- Counting decimal places in multiplication (must count ALL places from both numbers)
- 0.5 × 0.5 = 0.25 (not 0.025 — count 1+1=2 decimal places in answer)""",
    metadata={"source": "ncert", "topic": "arithmetic", "class_level": "class_6", "chapter": "ch8", "difficulty": "beginner"}),

    Document(page_content="""Class 6 | Ch9: Data Handling

KEY CONCEPTS:
Data: collection of information (numbers or facts)
Raw data: data collected but not organized
Tally marks: groups of 5 (4 vertical lines + 1 diagonal)
Frequency: number of times a value occurs
Frequency table: organized table showing values and their frequencies

MEASURES OF CENTRAL TENDENCY:
Mean (Average) = Sum of all observations / Number of observations
Median = middle value when data is arranged in order
  - Odd number of values: middle term
  - Even number of values: average of two middle terms
Mode = value that occurs most frequently
  - A dataset can have no mode, one mode, or multiple modes

PICTOGRAPH: uses pictures/symbols to represent data
BAR GRAPH: uses rectangular bars to represent data
  - All bars same width, equal spacing, height represents frequency

SOLVED EXAMPLES:
Example 1: Find mean, median, mode of: 12, 15, 11, 18, 15, 13, 20, 15, 10
Mean = (12+15+11+18+15+13+20+15+10) / 9 = 129/9 = 14.33
Arrange: 10, 11, 12, 13, 15, 15, 15, 18, 20 (9 values → 5th value is median)
Median = 15
Mode = 15 (appears 3 times, most frequent)

Example 2: In a bar graph, scale is 1 unit = 5 students
Bar of height 6 units → 6 × 5 = 30 students

RANGE = Maximum value - Minimum value
In example above: Range = 20 - 10 = 10

COMMON MISTAKES:
- Mean is affected by extreme values (outliers); median is not
- Mode is most FREQUENT, not largest or smallest
- Must arrange data in order before finding median
- Even number of data values: median = average of n/2 th and (n/2+1)th values""",
    metadata={"source": "ncert", "topic": "statistics", "class_level": "class_6", "chapter": "ch9", "difficulty": "beginner"}),

    Document(page_content="""Class 6 | Ch10: Mensuration

KEY CONCEPTS:
Perimeter: total length of boundary of a closed figure (add all sides)
Area: amount of surface enclosed within boundary (square units)

PERIMETER FORMULAS:
Rectangle: P = 2(l + b) where l=length, b=breadth
Square: P = 4 × side
Triangle: P = a + b + c (sum of all three sides)
Regular polygon: P = n × side (n = number of sides)

AREA FORMULAS:
Rectangle: A = length × breadth = l × b
Square: A = side × side = s²
Triangle: A = (1/2) × base × height

UNITS:
Length: mm, cm, m, km
Area: mm², cm², m², km², hectare (1 hectare = 10,000 m²)
Conversion: 1 m² = 10,000 cm²

SOLVED EXAMPLES:
Example 1: Rectangle 15cm × 8cm
Perimeter = 2(15 + 8) = 2 × 23 = 46 cm
Area = 15 × 8 = 120 cm²

Example 2: Square of side 9cm
Perimeter = 4 × 9 = 36 cm
Area = 9 × 9 = 81 cm²

Example 3: Triangle base=12cm, height=7cm
Area = (1/2) × 12 × 7 = 42 cm²

Example 4: A room 5m × 4m needs tiles of 25cm × 25cm. How many tiles?
Area of room = 5 × 4 = 20 m² = 200,000 cm²
Area of each tile = 25 × 25 = 625 cm²
Number of tiles = 200,000 ÷ 625 = 320 tiles

PERIMETER vs AREA:
Perimeter is 1D measurement (length) — use linear units (cm, m)
Area is 2D measurement (surface) — use square units (cm², m²)

COMMON MISTAKES:
- Using wrong formula: P of rectangle = 2(l+b) NOT 2l+b
- Area of square = s² NOT 4s (that is perimeter)
- Not converting units before calculating
- Height of triangle must be PERPENDICULAR to base""",
    metadata={"source": "ncert", "topic": "mensuration", "class_level": "class_6", "chapter": "ch10", "difficulty": "beginner"}),

    Document(page_content="""Class 6 | Ch11: Algebra — Introduction to Variables

KEY CONCEPTS:
Variable: a letter that represents an unknown or changing quantity. Examples: x, y, n, l
Constant: a fixed value that does not change. Examples: 5, -3, 0, π
Algebraic expression: combination of variables and constants using operations
  Examples: 2x + 3, 5y - 7, x² + 2x - 1

FORMING EXPRESSIONS:
"5 added to 3 times x" = 3x + 5
"y subtracted from 10" = 10 - y
"Product of m and n" = mn
"Twice a number decreased by 4" = 2n - 4

TERMS IN EXPRESSIONS:
3x² + 2x - 5 has 3 terms: 3x², 2x, -5
Like terms: same variable and same power (3x and 7x are like terms)
Unlike terms: different variable or power (3x and 3x² are unlike terms)

EQUATION vs EXPRESSION:
Expression: 2x + 3 (no equal sign)
Equation: 2x + 3 = 11 (has equal sign, can be solved)

SIMPLE EQUATIONS:
Solve by finding value of variable that makes equation true
x + 5 = 12 → x = 12 - 5 = 7
3y = 21 → y = 21/3 = 7

SUBSTITUTION (finding value):
If x = 4: 3x + 5 = 3(4) + 5 = 12 + 5 = 17
If y = 3: 2y² - y + 1 = 2(9) - 3 + 1 = 18 - 3 + 1 = 16

PATTERNS AND RULES USING ALGEBRA:
Number of matchsticks for n squares in a row = 3n + 1
Perimeter of square with side s = 4s
Distance = Speed × Time → d = s × t

SOLVED EXAMPLES:
Example 1: Write as expression: "5 less than twice a number"
Let number = n. Answer = 2n - 5

Example 2: Find value of 3x² - 2x + 1 when x = 2
= 3(4) - 2(2) + 1 = 12 - 4 + 1 = 9

COMMON MISTAKES:
- 3x means 3 × x, NOT 3 + x
- x² means x × x, NOT 2 × x
- "5 less than x" is x - 5, NOT 5 - x
- An expression does not have a solution (only equations do)""",
    metadata={"source": "ncert", "topic": "algebra", "class_level": "class_6", "chapter": "ch11", "difficulty": "beginner"}),

    Document(page_content="""Class 6 | Ch12: Ratio and Proportion

KEY CONCEPTS:
Ratio: comparison of two quantities of the SAME KIND by division.
Written as a:b or a/b (read as "a is to b")
a and b are called terms. a is antecedent, b is consequent.

IMPORTANT PROPERTIES:
Ratio has no units (both quantities must be in same unit first)
Equivalent ratios: 2:3 = 4:6 = 6:9 (multiply/divide both by same number)
Simplest form: HCF of both terms = 1

COMPARISON OF RATIOS:
Convert to fractions and compare: 3:4 vs 5:7 → 3/4=0.75 vs 5/7=0.714 → 3:4 > 5:7

PROPORTION:
Four quantities a, b, c, d are in proportion if a:b = c:d
Written as a:b :: c:d (read as "a is to b as c is to d")
Property: Product of extremes = Product of means → a × d = b × c

UNITARY METHOD:
Find value of ONE unit, then multiply for required units.
Step 1: Find cost/value of 1 item
Step 2: Multiply by required number

SOLVED EXAMPLES:
Example 1: Divide 720 between Arjun and Bharat in ratio 4:5
Total parts = 4 + 5 = 9
Arjun gets = (4/9) × 720 = 320
Bharat gets = (5/9) × 720 = 400
Check: 320 + 400 = 720 ✓

Example 2: Check if 3:4 and 9:12 are in proportion
3/4 = 0.75 and 9/12 = 3/4 = 0.75
OR: 3 × 12 = 36 and 4 × 9 = 36 → YES, they are in proportion

Example 3: If 6 pens cost ₹90, find cost of 10 pens
Cost of 1 pen = 90/6 = ₹15
Cost of 10 pens = 15 × 10 = ₹150

COMMON MISTAKES:
- Ratio requires same units: 50cm : 2m must first convert → 50cm : 200cm = 1:4
- Ratio 2:3 does NOT mean first person gets 2 and second gets 3 (it means parts)
- In proportion a:b::c:d → a×d = b×c (extremes × means)""",
    metadata={"source": "ncert", "topic": "arithmetic", "class_level": "class_6", "chapter": "ch12", "difficulty": "beginner"}),

    Document(page_content="""Class 6 | Ch13: Symmetry

KEY CONCEPTS:
Line of symmetry (axis of symmetry): a line that divides a figure into two identical halves
  that are mirror images of each other.
A figure can have 0, 1, 2, or more lines of symmetry.

LINES OF SYMMETRY FOR COMMON SHAPES:
Equilateral triangle: 3 lines of symmetry
Isosceles triangle: 1 line of symmetry
Scalene triangle: 0 lines of symmetry
Square: 4 lines of symmetry (2 through midpoints + 2 diagonals)
Rectangle: 2 lines of symmetry (through midpoints only, NOT diagonals)
Rhombus: 2 lines of symmetry (both diagonals)
Circle: infinite lines of symmetry (any diameter)
Regular pentagon: 5 lines of symmetry
Regular hexagon: 6 lines of symmetry
Regular polygon with n sides: n lines of symmetry

REFLECTION (MIRROR) SYMMETRY:
When folded along line of symmetry, both halves overlap perfectly.
Mirror image: left-right are swapped.

LETTERS WITH SYMMETRY:
Horizontal axis: B, C, D, E, H, I, K, O, X
Vertical axis: A, H, I, M, O, T, U, V, W, X, Y
Both axes: H, I, O, X
No symmetry: F, G, J, L, N, P, Q, R, S, Z

INKBLOT SYMMETRY:
Fold paper, drop ink, press → creates symmetric patterns

SOLVED EXAMPLES:
Example 1: How many lines of symmetry does a regular hexagon have?
Regular hexagon has 6 sides → 6 lines of symmetry
(3 through opposite vertices + 3 through midpoints of opposite sides)

Example 2: Does a rectangle have diagonal lines of symmetry?
NO. When folded along diagonal, corners do not match.
Rectangle has only 2 lines of symmetry (through midpoints of opposite sides).

COMMON MISTAKES:
- Rectangle diagonals are NOT lines of symmetry (unlike square)
- Rhombus diagonals ARE lines of symmetry (unlike rectangle)
- A figure with 2 identical parts doesn't always have symmetry
  (the dividing line must create mirror images)""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_6", "chapter": "ch13", "difficulty": "beginner"}),

    Document(page_content="""Class 6 | Ch14: Practical Geometry

KEY CONCEPTS:
Tools used: Ruler (scale), Compass, Protractor, Divider, Set squares

CONSTRUCTING A LINE SEGMENT:
Method 1 (ruler): draw line, mark two points at required distance
Method 2 (compass): draw ray, set compass to required length, mark arc on ray

CONSTRUCTING PERPENDICULAR BISECTOR of segment AB:
Step 1: Open compass to more than half of AB
Step 2: Draw arcs from A above and below AB
Step 3: Draw arcs from B (same radius) — they intersect at P and Q
Step 4: Join P and Q → PQ is perpendicular bisector of AB
PQ bisects AB at 90° and the midpoint M divides AB equally.

CONSTRUCTING PERPENDICULAR TO A LINE:
From a point ON the line: use compass to mark equal distances on both sides, then bisect.
From a point NOT on the line: arc from point cuts line at two points, then bisect.

CONSTRUCTING ANGLES USING PROTRACTOR:
Step 1: Draw base ray OA
Step 2: Place protractor centre at O, base at OA
Step 3: Mark point B at required angle reading
Step 4: Join OB → angle AOB is the required angle

CONSTRUCTING ANGLE BISECTOR of angle AOB:
Step 1: Draw arc from vertex O cutting both rays at P and Q
Step 2: Draw equal arcs from P and Q intersecting at R
Step 3: Join OR → OR bisects angle AOB
Each half = half of original angle

CONSTRUCTING STANDARD ANGLES (using compass):
60°: Equilateral triangle construction
120° = 2 × 60°
90° = 60° + 30° or perpendicular bisector method
30° = bisect 60°
45° = bisect 90°

SOLVED EXAMPLES:
Example 1: Construct angle of 75°
75° = 60° + 15° = 60° + (30°/2)
OR: 90° - 15° = 90° - 30°/2
Step 1: Construct 60°
Step 2: Bisect to get 30°
Step 3: Add 60° + 15° (bisect the 30°) = 75°

COMMON MISTAKES:
- Compass must not slip while drawing arc (keep it firmly at same radius)
- Place protractor centre EXACTLY on vertex
- Perpendicular bisector works only when compass is opened MORE than half the segment
- Always verify construction by measuring the result""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_6", "chapter": "ch14", "difficulty": "beginner"}),

    # ────────────────────────────────────────────────────────────────
    #  ORIGINAL 6 DOCUMENTS (kept for backwards compatibility)
    #  These cover advanced topics the NCERT chapters don't detail
    # ────────────────────────────────────────────────────────────────

    Document(page_content="""Calculus Fundamentals:
The derivative of f(x) measures the rate of change. Key rules:
- Power Rule: d/dx[x^n] = n*x^(n-1)
- Product Rule: d/dx[f*g] = f'g + fg'
- Chain Rule: d/dx[f(g(x))] = f'(g(x)) * g'(x)
- Quotient Rule: d/dx[f/g] = (f'g - fg') / g^2
Common derivatives:
- d/dx[sin(x)] = cos(x), d/dx[cos(x)] = -sin(x)
- d/dx[e^x] = e^x, d/dx[ln(x)] = 1/x
Integration (antiderivative):
- integral(x^n dx) = x^(n+1)/(n+1) + C
- integral(e^x dx) = e^x + C
- integral(sin(x) dx) = -cos(x) + C
Fundamental Theorem: integral[a to b] f(x) dx = F(b) - F(a)""",
    metadata={"source": "knowledge_base", "topic": "calculus", "class_level": "class_12", "difficulty": "advanced"}),

    Document(page_content="""Linear Algebra Essentials:
Matrix Operations: multiplication (row-by-column), transpose, determinant of 2x2: ad-bc
Inverse: A^(-1) exists iff det(A) != 0. A^(-1) = adj(A)/det(A)
Eigenvalues: det(A - lambda*I) = 0. Eigenvectors: solve (A - lambda*I)v = 0
Vector Spaces: span, basis, dimension, linear independence
Rank-Nullity Theorem: rank(A) + nullity(A) = n (number of columns)
Dot Product: u·v = |u||v|cos(theta). Orthogonal: u·v = 0""",
    metadata={"source": "knowledge_base", "topic": "linear_algebra", "class_level": "class_12", "difficulty": "advanced"}),

    Document(page_content="""Statistics and Probability:
Mean = sum(x)/n. Variance = sum((x-mu)^2)/n. SD = sqrt(variance)
Probability: P(A∪B) = P(A)+P(B)-P(A∩B). P(A|B) = P(A∩B)/P(B)
Bayes Theorem: P(A|B) = P(B|A)*P(A)/P(B)
Distributions: Normal (bell curve), Binomial P(X=k)=C(n,k)*p^k*(1-p)^(n-k)
Central Limit Theorem: sample means → normal as n → infinity""",
    metadata={"source": "knowledge_base", "topic": "statistics", "class_level": "class_11", "difficulty": "intermediate"}),

    Document(page_content="""Algebra and Number Theory:
Quadratic: x = (-b ± sqrt(b^2-4ac))/2a. Discriminant D=b^2-4ac
D>0: two real roots. D=0: one repeated root. D<0: two complex roots
Logarithm: log(ab)=log(a)+log(b), log(a/b)=log(a)-log(b), log(a^n)=n*log(a)
Factoring: a^2-b^2=(a+b)(a-b), a^3+b^3=(a+b)(a^2-ab+b^2)
AP: a_n=a+(n-1)d, S_n=n/2*(2a+(n-1)d). GP: a_n=ar^(n-1), S=a(1-r^n)/(1-r)""",
    metadata={"source": "knowledge_base", "topic": "algebra", "class_level": "class_10", "difficulty": "intermediate"}),

    Document(page_content="""Trigonometry:
Identities: sin^2(x)+cos^2(x)=1, tan(x)=sin(x)/cos(x)
Sum formulas: sin(A+B)=sinA*cosB+cosA*sinB, cos(A+B)=cosA*cosB-sinA*sinB
Double angle: sin(2x)=2sin(x)cos(x), cos(2x)=cos^2(x)-sin^2(x)
Values: sin30=1/2, sin45=sqrt(2)/2, sin60=sqrt(3)/2, sin90=1
Law of Sines: a/sinA=b/sinB=c/sinC. Law of Cosines: c^2=a^2+b^2-2ab*cosC""",
    metadata={"source": "knowledge_base", "topic": "trigonometry", "class_level": "class_10", "difficulty": "intermediate"}),

    Document(page_content="""Discrete Mathematics:
Permutations: P(n,r)=n!/(n-r)!. Combinations: C(n,r)=n!/(r!*(n-r)!)
GCD via Euclidean algorithm: GCD(a,b)=GCD(b, a mod b). LCM(a,b)=a*b/GCD(a,b)
Modular arithmetic: a≡b(mod n) means n divides (a-b)
Fermat's Little Theorem: a^(p-1)≡1(mod p) for prime p
De Morgan's: NOT(A AND B)=NOT(A) OR NOT(B)""",
    metadata={"source": "knowledge_base", "topic": "discrete_math", "class_level": "class_11", "difficulty": "advanced"}),

]