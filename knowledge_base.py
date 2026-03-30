"""
╔══════════════════════════════════════════════════════════════════════╗
║  knowledge_base.py — Advanced Mathematics Assistant V2              ║
║  ✅ Class 6  — 14 chapters                                          ║
║  ✅ Class 7  — 15 chapters                                          ║
║  🔜 Class 8, 9, 10, 11, 12, JEE — coming next sessions             ║
║  HOW TO ADD MORE: append Document objects, then --rebuild           ║
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
#  SECTION 1 — CLASS_EXAMPLES (sidebar dropdown data)
# ════════════════════════════════════════════════════════════════════

CLASS_EXAMPLES = {
    "📘 Class 6": {
        "Ch1 · Knowing Our Numbers":      "Write 5,08,01,592 in words and find the difference between place value and face value of 8 in this number",
        "Ch2 · Whole Numbers":            "Show 3 + 4 = 4 + 3 and 2 x (3 + 4) = 2x3 + 2x4 on a number line and explain the properties used",
        "Ch3 · Playing With Numbers":     "Find HCF and LCM of 36 and 48 using prime factorisation method step by step",
        "Ch4 · Basic Geometrical Ideas":  "Define point, line, line segment, ray and angle with diagrams. What is the difference between a line and a line segment?",
        "Ch5 · Elementary Shapes":        "Classify angles: 35, 90, 120, 180, 270 degrees. Name the type of triangle with sides 3cm, 4cm, 5cm",
        "Ch6 · Integers":                 "Solve using number line: (-5) + 8, 3 - (-4), (-6) + (-2). Explain rules for addition of integers",
        "Ch7 · Fractions":                "Solve: 3/4 + 5/6 - 1/3. Also arrange 2/3, 3/4, 5/8, 7/12 in ascending order",
        "Ch8 · Decimals":                 "Convert 2.375 to fraction. Multiply 3.25 x 1.4 and divide 8.64 by 0.6 with full steps",
        "Ch9 · Data Handling":            "Find mean, median and mode of: 12, 15, 11, 18, 15, 13, 20, 15, 10",
        "Ch10 · Mensuration":             "Find perimeter and area of a rectangle 15cm x 8cm and a square of side 9cm",
        "Ch11 · Algebra":                 "Write expressions for: 5 added to 3 times x, y subtracted from 10. Find value when x=4, y=3",
        "Ch12 · Ratio and Proportion":    "Divide 720 between Arjun and Bharat in ratio 4:5. Check if 3:4 and 9:12 are in proportion",
        "Ch13 · Symmetry":                "How many lines of symmetry: equilateral triangle, square, rectangle, circle, regular hexagon?",
        "Ch14 · Practical Geometry":      "Construct a line segment of 6.5cm. Draw perpendicular bisector and angle bisector of 60 degrees",
    },
    "📗 Class 7": {
        "Ch1 · Integers":                 "Evaluate: (-8) x (-5), (-36) divided by 4, (-7) x 8 + (-7) x 2. State properties of multiplication of integers",
        "Ch2 · Fractions and Decimals":   "Multiply 2 and 3/4 by 1 and 1/3. Divide 3 and 1/2 by 1 and 2/3. Convert 0.125, 1.625 to fractions",
        "Ch3 · Data Handling":            "Find mean of first 10 natural numbers. Find mode and median of 4,7,2,9,4,8,4,6. Probability of even number on die?",
        "Ch4 · Simple Equations":         "Solve: 2x + 7 = 19, 3(y - 4) = 2y + 1, (x+2)/3 = (x-1)/4. Verify answers by substitution",
        "Ch5 · Lines and Angles":         "Two parallel lines cut by transversal. One angle is 65 degrees. Find all 8 angles and name each pair",
        "Ch6 · Triangle Properties":      "In triangle ABC, angle A=50, angle B=70. Find angle C. Verify exterior angle theorem",
        "Ch7 · Congruence of Triangles":  "State all congruence rules SSS SAS ASA AAS RHS with examples. When can we NOT use AAA?",
        "Ch8 · Comparing Quantities":     "Find 15% of 400. What % is 45 of 180? SP when CP=850 profit=12%. SP when CP=600 loss=8%",
        "Ch9 · Rational Numbers":         "Represent -3/5 on number line. Find 3 rational numbers between 1/4 and 1/2",
        "Ch10 · Practical Geometry":      "Construct triangle PQR where PQ=5cm, QR=4.5cm, angle Q=60 degrees using compass and ruler",
        "Ch11 · Perimeter and Area":      "Find area of parallelogram base 8cm height 5cm. Find circumference and area of circle radius 7cm",
        "Ch12 · Algebraic Expressions":   "Add 3x squared + 2x - 5 and x squared - 3x + 2. Subtract 2a-3b from 5a+2b",
        "Ch13 · Exponents and Powers":    "Simplify: 2 to the 5 times 2 to the 3, 3 to the 7 divided by 3 to the 4. Express 48000000 in standard form",
        "Ch14 · Symmetry":                "Find order of rotational symmetry of square, rectangle, equilateral triangle, circle, regular pentagon",
        "Ch15 · Solid Shapes":            "Draw nets for cube, cuboid, triangular prism. Find faces, edges, vertices. Verify Euler formula F+V-E=2",
    },
    "📙 Class 8": {
        "Ch1 · Rational Numbers":         "Find 5 rational numbers between -1/2 and 1/3. Verify commutativity for -2/3 and 4/5",
        "Ch2 · Linear Equations":         "Solve: (2x+3)/5 - (x-4)/3 = 2. A number is 4 more than twice another and their sum is 40",
        "Ch3 · Quadrilaterals":           "In parallelogram ABCD, angle A=75 degrees. Find all angles. State properties of rhombus and kite",
        "Ch4 · Practical Geometry":       "Construct quadrilateral ABCD: AB=4cm, BC=3.5cm, CD=4.5cm, DA=3cm, AC=5cm",
        "Ch5 · Data Handling":            "Draw pie chart: Wheat 40%, Rice 30%, Maize 20%, Others 10%. Probability of red card from 52",
        "Ch6 · Squares and Square Roots": "Find square root of 1764 by prime factorisation and long division. Is 1352 a perfect square?",
        "Ch7 · Cubes and Cube Roots":     "Find cube root of 13824 by prime factorisation. Find smallest multiplier to make 675 a perfect cube",
        "Ch8 · Comparing Quantities":     "Find CI on 12000 at 10% per year for 2 years compounded annually. Compare with SI",
        "Ch9 · Algebraic Identities":     "Expand (3x+2y) squared, (4a-3b) squared, (x+3)(x-3). Factorise x squared+8x+16",
        "Ch10 · Solid Shapes":            "Draw top view, front view and side view of cube, cylinder and cone",
        "Ch11 · Mensuration":             "Find area of trapezium parallel sides 8cm and 5cm height 4cm. Surface area of cuboid 5x4x3cm",
        "Ch12 · Exponents and Powers":    "Simplify: (2 to -3 times 3 to -2) divided by 6 to -1. Express 0.00000605 in standard form",
        "Ch13 · Direct Inverse Proportion":"8 workers finish in 12 days. How many days for 6 workers? If 15 bags cost 450, cost of 24 bags?",
        "Ch14 · Factorisation":           "Factorise: 12x squared y - 9xy squared + 6xyz, x squared + 7x + 12, 2x squared + 7x + 3",
        "Ch15 · Introduction to Graphs":  "Plot A(2,3), B(-1,4), C(0,-2). Draw graph of x+y=5 and find where it cuts both axes",
        "Ch16 · Playing With Numbers":    "A 2-digit number is 4 times sum of its digits. If 18 is added digits reverse. Find the number",
    },
    "📒 Class 9": {
        "Ch1 · Number Systems":           "Prove root 2 is irrational. Represent root 5 on number line. Rationalise 3/(2+root3)",
        "Ch2 · Polynomials":              "Find remainder when x cubed - 6x squared + 11x - 6 is divided by x-2. Factorise x cubed - 23x squared + 142x - 120",
        "Ch3 · Coordinate Geometry":      "Plot A(3,4), B(-2,3), C(-4,-1), D(2,-3). Find which quadrant each lies in. Find distance AB",
        "Ch4 · Linear Equations 2 Var":   "Draw graph of 2x+3y=12. Find x-intercept and y-intercept. Find 3 solutions",
        "Ch5 · Euclid's Geometry":        "State Euclid's 5 postulates. Explain parallel postulate. Give 2 theorems from postulates",
        "Ch6 · Lines and Angles":         "Prove vertically opposite angles are equal. Find all 8 angles when parallel lines cut by transversal",
        "Ch7 · Triangles":                "Prove angles opposite equal sides of isosceles triangle are equal. State and prove ASA rule",
        "Ch8 · Quadrilaterals":           "Prove diagonals of parallelogram bisect each other. Prove mid-point theorem with full proof",
        "Ch9 · Areas Parallelogram":      "Prove parallelograms on same base and between same parallels are equal in area",
        "Ch10 · Circles":                 "Prove equal chords subtend equal angles at centre. Prove angle in semicircle is 90 degrees",
        "Ch11 · Constructions":           "Construct triangle with perimeter 11cm and base angles 60 and 45 degrees",
        "Ch12 · Heron's Formula":         "Find area of triangle with sides 13cm, 14cm, 15cm using Heron's formula",
        "Ch13 · Surface Areas Volumes":   "Find total surface area and volume of cone radius 5cm slant height 13cm",
        "Ch14 · Statistics":              "Find mean by assumed mean method. Find median and mode for grouped frequency data",
        "Ch15 · Probability":             "Bag has 5 red, 7 blue, 3 green balls. Find probability of red, not blue, green or red",
    },
    "📓 Class 10": {
        "Ch1 · Real Numbers":             "Prove root 3 is irrational. Find HCF of 96 and 404 by Euclid's algorithm",
        "Ch2 · Polynomials":              "Find zeroes of 6x squared - 3 - 7x and verify sum and product of zeroes formulas",
        "Ch3 · Pair of Linear Equations": "Solve by cross multiplication: 2x+3y=11, 2x-4y=-24. Solve graphically and find area of triangle formed",
        "Ch4 · Quadratic Equations":      "Solve 2x squared - 7x + 3 = 0 by factorisation, completing square and quadratic formula",
        "Ch5 · Arithmetic Progressions":  "Find sum of first 40 positive integers divisible by 6. If 7th term is 34 and 13th term is 64, find the AP",
        "Ch6 · Triangles":                "State and prove Basic Proportionality Theorem. Prove area ratio equals square of side ratio for similar triangles",
        "Ch7 · Coordinate Geometry":      "Find area of triangle A(2,3), B(-1,0), C(2,-4). Find point dividing line joining (1,3) and (4,6) in ratio 2:1",
        "Ch8 · Introduction to Trig":     "If sin theta = 3/5 find all trig ratios. Prove sin squared + cos squared = 1",
        "Ch9 · Applications of Trig":     "From top of 75m tower angles of depression of two boats are 30 and 45 degrees. Find distance between boats",
        "Ch10 · Circles":                 "Prove tangent is perpendicular to radius. Find length of tangent from point 17cm from centre radius 8cm",
        "Ch11 · Constructions":           "Divide line segment 7cm in ratio 3:2. Draw pair of tangents from point 10cm from centre radius 4cm",
        "Ch12 · Areas Related to Circles":"Find area of sector radius 14cm angle 60 degrees. Find area of segment",
        "Ch13 · Surface Areas Volumes":   "Solid is cone on hemisphere radius 3.5cm cone height 4cm. Find total surface area and volume",
        "Ch14 · Statistics":              "Find mean by step deviation method. Find median and mode of frequency distribution",
        "Ch15 · Probability":             "Two dice thrown. Find probability sum is 8, sum is prime, same number on both dice",
    },
    "📕 Class 11": {
        "Ch1 · Sets":                     "If A={1,2,3,4,5} B={2,4,6,8} find A union B, A intersection B, A-B, B-A. Verify n(A union B) formula",
        "Ch2 · Relations and Functions":  "Find domain and range of f(x)=root(9-x squared). Find fog and gof if f(x)=2x+1 and g(x)=x squared-1",
        "Ch3 · Trigonometric Functions":  "Prove sin(A+B)sin(A-B)=sin squared A - sin squared B. Solve 2cos squared x - 3cosx + 1 = 0",
        "Ch4 · Math Induction":           "Prove by PMI: 1+2+3+...+n = n(n+1)/2. Prove 4 to n - 1 is divisible by 3",
        "Ch5 · Complex Numbers":          "Find modulus and argument of z = -1 + i root 3. Express in polar form. Find cube roots of unity",
        "Ch6 · Linear Inequalities":      "Solve 3x-2 > 2x+1 and show on number line. Solve system x+y<=10, x+3y<=15, x>=0, y>=0",
        "Ch7 · Permutations Combinations":"5 boys and 3 girls sit in row if girls always sit together. Find 7C3. Prove nCr + nCr-1 = n+1Cr",
        "Ch8 · Binomial Theorem":         "Expand (2x-3y) to 4th power. Find 5th term in (x+2) to 8th. Find term independent of x in (x+1/x) to 10th",
        "Ch9 · Sequences and Series":     "Find sum of GP 1+3+9+...+2187. If AM=10 and GM=8 find the numbers",
        "Ch10 · Straight Lines":          "Find equation through (2,-3) perpendicular to 3x-4y+5=0. Distance between parallel lines 3x+4y-5=0 and 3x+4y+15=0",
        "Ch11 · Conic Sections":          "Find focus, directrix, latus rectum of y squared = 12x. Equation of ellipse with foci (plus minus 3, 0) and a=5",
        "Ch12 · 3D Geometry":             "Find distance between A(1,2,3) and B(4,-2,6). Find point dividing AB in ratio 2:1",
        "Ch13 · Limits and Derivatives":  "Find limit of sin3x/x as x approaches 0. Differentiate x cubed times sinx using product rule",
        "Ch14 · Math Reasoning":          "Write negation of: All primes are odd. Write converse and contrapositive of: If x>5 then x squared > 25",
        "Ch15 · Statistics":              "Find variance and standard deviation of 6,8,10,12,14. Compare variability using coefficient of variation",
        "Ch16 · Probability":             "P(A)=0.4, P(B)=0.5, P(A intersection B)=0.2. Find P(A union B) and P(A given B)",
    },
    "📔 Class 12": {
        "Ch1 · Relations and Functions":  "Show f(x)=2x+3 is bijective. Is R={(a,b): a-b divisible by 5} an equivalence relation?",
        "Ch2 · Inverse Trig Functions":   "Find sin inverse(-1/2), cos inverse(-root3/2), tan inverse(root3). Prove sin inverse x + cos inverse x = pi/2",
        "Ch3 · Matrices":                 "If A=[[1,2],[3,4]] find A + A transpose. Show it is symmetric. Express A as sum of symmetric and skew-symmetric",
        "Ch4 · Determinants":             "Find determinant of 3x3 matrix. Find inverse using adjoint. Solve using Cramer's rule: x+y+z=6, 2x-y+z=3",
        "Ch5 · Continuity Differentiability":"Check continuity of |x-3| at x=3. Differentiate x to x, sin(logx), e to x squared",
        "Ch6 · Applications of Derivatives":"Find intervals where 2x cubed - 9x squared + 12x - 5 is increasing. Find local maxima and minima",
        "Ch7 · Integrals":                "Evaluate integral of x squared e to x dx by parts. Integral of 1/(x squared - 4) by partial fractions",
        "Ch8 · Application of Integrals": "Find area bounded by y=x squared and y=x+2. Area of circle x squared + y squared = 16",
        "Ch9 · Differential Equations":   "Solve dy/dx = (x squared + y squared)/2xy homogeneous. Solve linear DE dy/dx + 2y/x = x squared",
        "Ch10 · Vector Algebra":          "If a=2i+3j-k and b=i-2j+3k find a dot b, a cross b, angle between them",
        "Ch11 · 3D Geometry":             "Find angle between two lines given in symmetric form. Distance from point (1,2,3) to plane 2x-3y+z=5",
        "Ch12 · Linear Programming":      "Maximise Z=3x+4y subject to x+y<=450, 2x+y<=600, x>=0, y>=0. Find all corner points",
        "Ch13 · Probability":             "Bag A has 3 red 5 black. Bag B has 4 red 6 black. Ball drawn is red. Find P(from bag A) using Bayes theorem",
    },
    "🏆 JEE Advanced": {
        "Definite Integrals":             "Evaluate integral from 0 to pi of x sinx/(1+cos squared x) dx using King's property. Show full working",
        "Complex Numbers":                "If z=(root3+i)/(1-i*root3), find modulus, argument and polar form. Find z to the 10th using De Moivre",
        "Theory of Equations":            "If roots of x cubed - 6x squared + 11x - 6 = 0 are in AP find them. Find conditions for both roots of quadratic in (1,2)",
        "Binomial Advanced":              "Find sum C(n,0) squared + C(n,1) squared + ... + C(n,n) squared. Find greatest term in (3+2x) to 10 when x=3/2",
        "Advanced Trigonometry":          "Solve sin2x - sinx = cosx - cos2x for x in [0,2pi]. Prove cos(pi/7) times cos(2pi/7) times cos(3pi/7) = 1/8",
        "Vectors and 3D Advanced":        "Find shortest distance between skew lines r=(i+j)+t(2i-j+k) and r=(2i+j-k)+s(3i-5j+2k)",
        "Probability Advanced":           "4 cards drawn without replacement. Find P(all suits represented) and P(exactly 2 aces)",
        "Inequalities":                   "Prove AM >= GM for 3 positive numbers. Find minimum of (x+1/x) squared + (y+1/y) squared for positive x,y with xy=1",
    },
}


# ════════════════════════════════════════════════════════════════════
#  SECTION 2 — MATH_KNOWLEDGE_BASE (RAG documents)
# ════════════════════════════════════════════════════════════════════

MATH_KNOWLEDGE_BASE = [

    # ── CLASS 6 — All 14 Chapters ───────────────────────────────────

    Document(page_content="""Class 6 | Ch1: Knowing Our Numbers
Indian number system: ones, thousands, lakhs, crores.
Place value = digit x position value. Face value = digit itself.
For 5,08,01,592: 5 in crores=5,00,00,000. Face value of 8=8 always.
Comparison: more digits=greater. Same digits: compare from left.
Rounding: nearest 10 (look at ones), nearest 100 (look at tens).
Roman: I=1,V=5,X=10,L=50,C=100,D=500,M=1000. Before=subtract(IV=4), After=add(VI=6).
Example: 7,35,02,814 = Seven crore thirty-five lakh two thousand eight hundred fourteen.
Common mistake: place value depends on position, face value is always the digit itself.""",
    metadata={"source": "ncert", "topic": "numbers", "class_level": "class_6", "chapter": "ch1", "difficulty": "beginner"}),

    Document(page_content="""Class 6 | Ch2: Whole Numbers
Natural Numbers: 1,2,3,... Whole Numbers: 0,1,2,3,... (0 is whole but NOT natural)
Properties: Closure(a+b and a×b always whole), Commutativity(a+b=b+a), Associativity, Distributivity(a×(b+c)=a×b+a×c)
Identity: a+0=a (additive), a×1=a (multiplicative). Zero property: a×0=0.
Predecessor of n=n-1. Successor of n=n+1.
Triangular numbers: 1,3,6,10,15 (n(n+1)/2). Square numbers: 1,4,9,16,25.
Sum 1+2+...+100 = 100×101/2 = 5050.
Common mistake: 0 is NOT natural. Subtraction/division NOT always closed for whole numbers.""",
    metadata={"source": "ncert", "topic": "numbers", "class_level": "class_6", "chapter": "ch2", "difficulty": "beginner"}),

    Document(page_content="""Class 6 | Ch3: Playing With Numbers - HCF and LCM
Prime: exactly 2 factors. Composite: more than 2. 1=neither. 2=only even prime.
Divisibility: by 2(last digit even), 3(digit sum div by 3), 5(last digit 0 or 5), 9(digit sum div by 9), 11(alternate digit difference=0 or multiple of 11).
Prime factorisation: 48=2^4 x 3.
HCF = product of COMMON prime factors with LOWEST powers.
LCM = product of ALL prime factors with HIGHEST powers.
KEY: HCF x LCM = product of the two numbers.
Example: HCF(36,48)=12, LCM(36,48)=144. Check: 12×144=1728=36×48.
Three bells every 6,10,15 min → together at LCM(6,10,15)=30 min.
Common mistake: HCF uses LOWEST powers, LCM uses HIGHEST powers (students mix these up).""",
    metadata={"source": "ncert", "topic": "number_theory", "class_level": "class_6", "chapter": "ch3", "difficulty": "beginner"}),

    Document(page_content="""Class 6 | Ch4: Basic Geometrical Ideas
Point: exact location, no size. Line: infinite both ways. Line segment: two endpoints. Ray: one endpoint infinite one way.
Angles: Acute(0-90), Right(90), Obtuse(90-180), Straight(180), Reflex(180-360), Complete(360).
Circle parts: Centre(fixed point), Radius(centre to circle), Diameter(chord through centre=2r), Chord(any two points on circle), Arc(part of circle), Sector(two radii + arc), Segment(chord + arc).
One line through two points. Infinite lines through one point.
Diameter is a chord but chord is not always diameter.""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_6", "chapter": "ch4", "difficulty": "beginner"}),

    Document(page_content="""Class 6 | Ch5: Understanding Elementary Shapes
Triangles by sides: Equilateral(all equal, all 60°), Isosceles(2 equal), Scalene(all different).
Triangles by angles: Acute(all<90°), Right(one=90°), Obtuse(one>90°).
Pythagorean triplets: (3,4,5),(5,12,13),(8,15,17),(7,24,25). Check: 3^2+4^2=25=5^2.
Quadrilaterals: Rectangle(4 right angles, opposite sides equal), Square(4 right angles, all sides equal), Parallelogram(opposite sides parallel equal), Rhombus(all sides equal), Trapezium(one pair parallel sides).
3D: Cube(F=6,E=12,V=8), Cuboid(F=6,E=12,V=8). Euler: F+V-E=2.
Square is special rectangle AND special rhombus. Hypotenuse=longest side opposite 90°.""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_6", "chapter": "ch5", "difficulty": "beginner"}),

    Document(page_content="""Class 6 | Ch6: Integers
Integers: ...-3,-2,-1,0,1,2,3... Right=greater, left=smaller on number line.
Positive > Zero > Negative. Among negatives: closer to zero is greater (-2>-5).
Addition: same sign(add, keep sign), different signs(subtract smaller absolute, keep sign of larger).
Subtraction: a-b = a+(-b). So 5-8=5+(-8)=-3. Also -3-(-5)=-3+5=2.
Ascending: -8<-5<-1<0<2<3.
Real life: temperature below zero, basement floors, bank withdrawals.
Common mistake: -5 is NOT greater than -2. Subtracting negative = adding positive: 5-(-3)=8.""",
    metadata={"source": "ncert", "topic": "numbers", "class_level": "class_6", "chapter": "ch6", "difficulty": "beginner"}),

    Document(page_content="""Class 6 | Ch7: Fractions
Types: Proper(p<q), Improper(p>=q), Mixed(whole+proper), Unit(p=1).
Equivalent: 1/2=2/4=3/6. Multiply or divide both by same number.
Comparing: same denominator compare numerators. Same numerator: smaller denominator=LARGER fraction.
Add/subtract: same denominator add numerators. Different: find LCM first.
Example: 3/4+5/6-1/3. LCM=12. = 9/12+10/12-4/12 = 15/12 = 5/4 = 1 and 1/4.
Ascending 2/3,3/4,5/8,7/12: LCM=24 → 16,18,15,14 over 24 → 7/12 < 5/8 < 2/3 < 3/4.
Common mistake: 1/2+1/3 ≠ 2/5. Correct: 3/6+2/6=5/6.""",
    metadata={"source": "ncert", "topic": "arithmetic", "class_level": "class_6", "chapter": "ch7", "difficulty": "beginner"}),

    Document(page_content="""Class 6 | Ch8: Decimals
Place value: 45.378 → 4=tens, 5=ones, 3=tenths, 7=hundredths, 8=thousandths.
Conversion: 0.375=375/1000=3/8. Fraction to decimal: divide (3/4=0.75).
Multiplication: count total decimal places. 3.25×1.4=325×14/1000=4550/1000=4.55.
Division by decimal: multiply both to remove decimal. 8.64÷0.6=86.4÷6=14.4.
Comparison: compare whole part, then tenths, then hundredths.
Always align decimal points during addition and subtraction.
0.5×0.5=0.25 (not 0.025). Count 1+1=2 decimal places.""",
    metadata={"source": "ncert", "topic": "arithmetic", "class_level": "class_6", "chapter": "ch8", "difficulty": "beginner"}),

    Document(page_content="""Class 6 | Ch9: Data Handling
Mean = Sum/Count. Median = middle value when arranged in order.
Odd count: middle term. Even count: average of two middle terms.
Mode = most frequent value. Range = Max - Min.
Bar graph: equal width bars, height=frequency. Tally: groups of 5.
Probability: P(event)=favourable/total. Always between 0 and 1.
Example: 12,15,11,18,15,13,20,15,10. Mean=129/9=14.33. Arranged→Median=15. Mode=15.
P(even on die)=3/6=1/2.
Must arrange data BEFORE finding median. Mode is most FREQUENT not largest.""",
    metadata={"source": "ncert", "topic": "statistics", "class_level": "class_6", "chapter": "ch9", "difficulty": "beginner"}),

    Document(page_content="""Class 6 | Ch10: Mensuration
Perimeter: Rectangle=2(l+b), Square=4s, Triangle=a+b+c.
Area: Rectangle=l×b, Square=s^2, Triangle=(1/2)×base×height.
Units: perimeter in cm/m, area in cm^2/m^2. 1m^2=10000cm^2. 1 hectare=10000m^2.
Example: Rectangle 15×8: P=46cm, A=120cm^2. Square 9cm: P=36cm, A=81cm^2.
Triangle base 12cm height 7cm: A=42cm^2.
Room 5m×4m tiles 25cm×25cm: Area=20m^2=200000cm^2. Tiles=200000/625=320.
Height of triangle must be PERPENDICULAR to base. Area of square=s^2 NOT 4s.""",
    metadata={"source": "ncert", "topic": "mensuration", "class_level": "class_6", "chapter": "ch10", "difficulty": "beginner"}),

    Document(page_content="""Class 6 | Ch11: Algebra - Introduction
Variable: letter for unknown (x,y,n). Constant: fixed value.
3x means 3×x. x^2 means x×x. "5 less than x" = x-5 NOT 5-x.
Like terms: same variable and power (3x and 7x). Unlike: different.
Expression: no equal sign (2x+3). Equation: has equal sign (2x+3=11).
Substitution: x=4 in 3x+5 = 3(4)+5=17.
"5 added to 3 times x"=3x+5. "y subtracted from 10"=10-y.
"Twice a number decreased by 4"=2n-4.
An expression has no solution. Only equations can be solved.""",
    metadata={"source": "ncert", "topic": "algebra", "class_level": "class_6", "chapter": "ch11", "difficulty": "beginner"}),

    Document(page_content="""Class 6 | Ch12: Ratio and Proportion
Ratio a:b = a/b. No units. Both quantities must be in SAME unit first.
Equivalent: 2:3=4:6=6:9.
Proportion a:b::c:d: product of extremes = product of means: a×d=b×c.
Unitary method: find cost of 1, multiply for required number.
Example: Divide 720 in 4:5. Total parts=9. Shares: 4/9×720=320 and 5/9×720=400.
Proportion check 3:4 and 9:12: 3×12=36=4×9=36. YES.
6 pens cost 90 → 1 pen=15 → 10 pens=150.
50cm:2m must convert → 50:200=1:4. Ratio requires SAME units.""",
    metadata={"source": "ncert", "topic": "arithmetic", "class_level": "class_6", "chapter": "ch12", "difficulty": "beginner"}),

    Document(page_content="""Class 6 | Ch13: Symmetry
Line of symmetry divides figure into two mirror-image halves.
Symmetry count: Equilateral triangle=3, Square=4, Rectangle=2(midpoints only NOT diagonals), Rhombus=2(diagonals), Circle=infinite, Pentagon=5, Hexagon=6, Isosceles triangle=1, Scalene=0, Parallelogram=0.
Regular n-sided polygon has n lines of symmetry.
Rectangle: 2 lines (horizontal+vertical through midpoints). Diagonals NOT lines of symmetry.
Rhombus: 2 lines (both diagonals are lines of symmetry).
Letters: Vertical symmetry: A,H,I,M,O,T,U,V,W,X,Y. Horizontal: B,C,D,E.
Parallelogram has NO line of symmetry at all.""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_6", "chapter": "ch13", "difficulty": "beginner"}),

    Document(page_content="""Class 6 | Ch14: Practical Geometry
Tools: Ruler, Compass, Protractor, Divider, Set squares.
Perpendicular bisector of AB: open compass>half AB, arcs from A and B, intersect at P and Q, join PQ.
Angle bisector of angle AOB: arc from O cuts both rays at P,Q. Equal arcs from P,Q intersect at R. OR bisects angle.
Standard angles with compass: 60°(equilateral triangle), 90°(perp bisector method), 30°(bisect 60°), 45°(bisect 90°), 75°=60°+15°.
Compass must not slip while drawing arc. Centre of protractor EXACTLY on vertex.
Must open compass MORE than half segment for perpendicular bisector to work.""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_6", "chapter": "ch14", "difficulty": "beginner"}),

    # ── CLASS 7 — All 15 Chapters ───────────────────────────────────

    Document(page_content="""Class 7 | Ch1: Integers
Absolute value |a| = distance from zero (always positive).
Multiplication: same signs=positive, different signs=negative.
(+)×(+)=+, (-)×(-)=+, (+)×(-)=-, (-)×(+)=-.
Division: same sign rules as multiplication.
(-36)÷(-6)=+6. (-36)÷(+6)=-6.
Distributivity: (-7)×8+(-7)×2 = (-7)(8+2) = (-7)(10) = -70.
Properties: closure under +,-,×. Commutativity for + and ×. Associativity. a×0=0.
Temperature: -3°C fell 5°C = -3+(-5) = -8°C.
Common mistake: (-3)^2=+9 but -(3^2)=-9. Two negatives multiply to positive.""",
    metadata={"source": "ncert", "topic": "numbers", "class_level": "class_7", "chapter": "ch1", "difficulty": "beginner"}),

    Document(page_content="""Class 7 | Ch2: Fractions and Decimals
Multiplication of fractions: (a/b)×(c/d)=ac/bd. Convert mixed to improper first.
2(3/4)×1(1/3) = (11/4)×(4/3) = 44/12 = 11/3 = 3(2/3).
Division: a/b ÷ c/d = a/b × d/c (multiply by RECIPROCAL of second).
3(1/2)÷1(2/3) = (7/2)÷(5/3) = (7/2)×(3/5) = 21/10 = 2.1.
Decimal multiplication: count total decimal places. 0.4×0.3=0.12 (1+1=2 places).
Division by decimal: 2.4÷0.6 = 24÷6 = 4 (multiply both by 10).
Conversion: 0.125=125/1000=1/8. 1.625=1625/1000=13/8=1(5/8).
Common mistake: flip SECOND fraction not first when dividing fractions.""",
    metadata={"source": "ncert", "topic": "arithmetic", "class_level": "class_7", "chapter": "ch2", "difficulty": "beginner"}),

    Document(page_content="""Class 7 | Ch3: Data Handling
Mean=Sum/n. Mean of first n natural numbers=(n+1)/2.
Median: arrange in order. Odd: middle term. Even: average of two middle terms.
Mode: most frequent. Range=Max-Min.
Double bar graph: compares two datasets side by side.
Probability: P(event)=favourable/total. Between 0 and 1.
Example: 4,7,2,9,4,8,4,6. Mean=44/8=5.5. Arranged:2,4,4,4,6,7,8,9. Median=(4+6)/2=5. Mode=4.
P(even on die)=3/6=1/2 (even numbers: 2,4,6).
Always arrange data BEFORE median. Probability never exceeds 1.""",
    metadata={"source": "ncert", "topic": "statistics", "class_level": "class_7", "chapter": "ch3", "difficulty": "beginner"}),

    Document(page_content="""Class 7 | Ch4: Simple Equations
Equation: LHS=RHS. Solution: value making equation true.
Transposition: move term to other side changing sign. +a becomes -a, ×a becomes ÷a.
Golden rule: same operation on BOTH sides.
Steps: collect variables one side, constants other side, divide by coefficient.
Solve 2x+7=19: 2x=12, x=6. Verify: 2(6)+7=19 correct.
Solve 3(y-4)=2y+1: 3y-12=2y+1, y=13. Verify: 3(9)=27=2(13)+1 correct.
Cross multiply: (x+2)/3=(x-1)/4 → 4(x+2)=3(x-1) → x=-11.
Word problem: consecutive integers sum=53. n+(n+1)=53 → n=26. Integers: 26,27.
Always verify by substituting back. Expand brackets BEFORE transposing.""",
    metadata={"source": "ncert", "topic": "algebra", "class_level": "class_7", "chapter": "ch4", "difficulty": "beginner"}),

    Document(page_content="""Class 7 | Ch5: Lines and Angles
Complementary=90° total. Supplementary=180° total. Linear pair=180°. Vertically opposite=EQUAL.
Parallel lines + transversal: 8 angles formed.
Corresponding angles: same position=EQUAL (F-shape).
Alternate interior angles: between lines, alternate sides=EQUAL (Z-shape).
Co-interior angles: between lines, same side=SUPPLEMENTARY=180° (C-shape).
Alternate exterior angles: outside, alternate sides=EQUAL.
Converse: if corresponding/alternate angles equal → lines parallel.
Example: angle=65°. Corresponding=65°. Alternate interior=65°. Co-interior=115°.
Two supplementary angles, one=3 times other: x+3x=180 → x=45°, angles=45° and 135°.
Co-interior angles SUPPLEMENTARY not equal. Vertically opposite ALWAYS equal.""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_7", "chapter": "ch5", "difficulty": "beginner"}),

    Document(page_content="""Class 7 | Ch6: Triangle Properties
Angle sum property: A+B+C=180° for any triangle.
Exterior angle = sum of two remote interior angles (not all three).
Triangle inequality: sum of any two sides > third side.
Pythagoras: c^2=a^2+b^2 where c=hypotenuse (opposite 90°, always longest).
Triplets: (3,4,5),(5,12,13),(8,15,17),(7,24,25).
Converse: if a^2+b^2=c^2 then right-angled.
Median: vertex to midpoint of opposite side. 3 medians meet at centroid.
Altitude: perpendicular from vertex. 3 meet at orthocentre.
Example: A=50°,B=70°,C=60°. Exterior at C=120°=A+B=50+70 verified.
Sides 9,40,41: 81+1600=1681=41^2 → right triangle.""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_7", "chapter": "ch6", "difficulty": "beginner"}),

    Document(page_content="""Class 7 | Ch7: Congruence of Triangles
Congruent: same shape AND same size. Symbol: congruent to.
ORDER MATTERS: triangle ABC congruent to triangle PQR means A-P, B-Q, C-R.
Rules: SSS(all 3 sides), SAS(2 sides+INCLUDED angle), ASA(2 angles+INCLUDED side), AAS(2 angles+non-included side), RHS(right angle+hypotenuse+one side).
AAA: gives SIMILAR triangles not congruent (same shape, different size).
SSA: FAILS - ambiguous case (two possible triangles).
CPCT: Corresponding Parts of Congruent Triangles are equal (used AFTER proving congruence).
Isosceles proof: AB=AC. Draw altitude AD. Triangles ABD and ACD congruent by RHS. Angle B=angle C by CPCT.
SAS: angle must be INCLUDED between the two sides. ASA: side must be INCLUDED between two angles.""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_7", "chapter": "ch7", "difficulty": "beginner"}),

    Document(page_content="""Class 7 | Ch8: Comparing Quantities
Percentage=per hundred. x%=x/100.
Fraction to %: multiply by 100. % to fraction: divide by 100.
Profit=SP-CP (when SP>CP). Loss=CP-SP (when CP>SP).
Profit%=(Profit/CP)×100. Loss%=(Loss/CP)×100.
SP=CP×(100+Profit%)/100. SP=CP×(100-Loss%)/100.
Simple Interest: SI=(P×R×T)/100. Amount A=P+SI.
Example: CP=850, Profit=12%: SP=850×112/100=952.
CP=600, Loss=8%: SP=600×92/100=552.
45 as % of 180: (45/180)×100=25%.
SI on 5000 at 6% for 3 years: SI=(5000×6×3)/100=900. A=5900.
Profit% always on CP NOT SP. Time in YEARS for SI. Discount on MARKED PRICE.""",
    metadata={"source": "ncert", "topic": "arithmetic", "class_level": "class_7", "chapter": "ch8", "difficulty": "beginner"}),

    Document(page_content="""Class 7 | Ch9: Rational Numbers
Rational: p/q where p,q integers and q≠0. Every integer=rational(n=n/1).
Standard form: q>0 and HCF(p,q)=1. So -6/4=-3/2.
Comparison: convert to same positive denominator, compare numerators.
-3/5 vs -2/3: LCM=15 → -9/15 vs -10/15 → -3/5>-2/3.
Dense: infinite rationals between any two rationals.
Operations: p/q+r/s=(ps+qr)/qs. Division: (p/q)÷(r/s)=ps/qr.
Finding rationals between 1/4 and 1/2: between 2/8 and 4/8 → 3/8, 5/16, 7/16.
-3/5+2/3=(-9+10)/15=1/15.
Denominator must be POSITIVE in standard form. -2/3 is greater than -1 (closer to zero).""",
    metadata={"source": "ncert", "topic": "numbers", "class_level": "class_7", "chapter": "ch9", "difficulty": "beginner"}),

    Document(page_content="""Class 7 | Ch10: Practical Geometry
Five triangle construction cases: SSS, SAS, ASA, RHS, AAS.
SSS: draw base, arc from both ends, intersection=third vertex.
SAS: draw base, angle at one end, mark distance on angle ray, join.
ASA: draw base (included side), angles at both ends, intersection=third vertex.
RHS: right angle, hypotenuse from far end, intersection=right angle vertex.
AAS: find third angle (180-sum of two given), then use ASA method.
Parallel lines: draw transversal, copy angle at new point.
SAS example: PQ=5cm, QR=4.5cm, angle Q=60°. Draw QR=4.5. Angle 60° at Q. Mark P at 5cm. Join PR.
SSS example: sides 5,6,7. Draw base 6. Arc radius 5 from one end. Arc radius 7 from other. Intersection=third vertex.
Check triangle inequality before constructing. Use sharp pencil.""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_7", "chapter": "ch10", "difficulty": "beginner"}),

    Document(page_content="""Class 7 | Ch11: Perimeter and Area
Perimeter: Triangle=a+b+c. Rectangle=2(l+b). Square=4s. Circle C=2πr=πd.
Area: Rectangle=l×b. Square=s^2. Triangle=(1/2)×b×h. Parallelogram=b×h. Circle=πr^2.
Height MUST be perpendicular to base for parallelogram and triangle.
π=22/7 (when radius is multiple of 7) or 3.14.
Path outside rectangle (width w): outer=(l+2w)×(b+2w). Area of path=outer-inner.
Example: Parallelogram base=8, height=5. Area=40cm^2 (NOT using slant side).
Circle r=7: C=2×(22/7)×7=44cm. A=(22/7)×49=154cm^2.
Rectangle 12m×8m, path 1m inside: inner=10×6. Path area=96-60=36m^2.
1m^2=10000cm^2. 1 hectare=10000m^2. Parallelogram uses PERPENDICULAR height.""",
    metadata={"source": "ncert", "topic": "mensuration", "class_level": "class_7", "chapter": "ch11", "difficulty": "beginner"}),

    Document(page_content="""Class 7 | Ch12: Algebraic Expressions
Term: single number, variable or product. Like terms: same variable same power.
Monomial(1 term), Binomial(2 terms), Trinomial(3 terms), Polynomial(1+ terms).
Addition: combine LIKE terms only. (3x^2+2x-5)+(x^2-3x+2)=4x^2-x-3.
Subtraction: change sign of ALL terms. (5a+2b)-(2a-3b)=5a+2b-2a+3b=3a+5b.
Substitution: 2x^2-3x+1 when x=2: 2(4)-3(2)+1=8-6+1=3.
Coefficient: numerical part. In -5xy, coefficient=-5.
Degree: sum of powers. 3x^2y has degree 3.
3x+2x^2 CANNOT be simplified (unlike terms). -(2a-3b)=-2a+3b NOT -2a-3b.
3x×2x=6x^2 (multiply coefficients AND add powers).""",
    metadata={"source": "ncert", "topic": "algebra", "class_level": "class_7", "chapter": "ch12", "difficulty": "beginner"}),

    Document(page_content="""Class 7 | Ch13: Exponents and Powers
a^n = a×a×...×a (n times). 2^5=32.
Laws (same base): a^m×a^n=a^(m+n), a^m÷a^n=a^(m-n), (a^m)^n=a^(mn).
Same power: a^m×b^m=(ab)^m, a^m÷b^m=(a/b)^m.
a^0=1 for any a≠0.
Standard form: number between 1 and 10 times power of 10.
48000000=4.8×10^7. 0.0000035=3.5×10^(-6).
Examples: 2^5×2^3=2^8=256. 3^7÷3^4=3^3=27. (2^3)^2=2^6=64. 2^3×5^3=10^3=1000.
2^3=8 NOT 6. a^m×a^n=a^(m+n) ADD not multiply powers. (2+3)^2≠2^2+3^2.""",
    metadata={"source": "ncert", "topic": "numbers", "class_level": "class_7", "chapter": "ch13", "difficulty": "beginner"}),

    Document(page_content="""Class 7 | Ch14: Symmetry
Line symmetry: one half is mirror image. Regular n-sided polygon: n lines of symmetry.
Lines of symmetry: Equilateral triangle=3, Square=4, Rectangle=2(midpoints only), Rhombus=2(diagonals), Isosceles=1, Scalene=0, Kite=1, Parallelogram=0, Pentagon=5, Hexagon=6, Circle=infinite.
Rotational symmetry: looks same after rotation<360°. Order=number of times in full rotation. Angle=360°÷order.
Rotational: Square(order 4, angle 90°), Rectangle(order 2, 180°), Equilateral triangle(order 3, 120°), Hexagon(order 6, 60°), Parallelogram(order 2, 180°), Scalene(order 1=none).
Square has BOTH line and rotational symmetry.
Parallelogram: NO line symmetry but HAS rotational (order 2).
Rectangle: 2 lines symmetry, order 2 rotation.
Pentagon: order 5, angle 72°.""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_7", "chapter": "ch14", "difficulty": "beginner"}),

    Document(page_content="""Class 7 | Ch15: Visualising Solid Shapes
3D shapes (F=faces, E=edges, V=vertices):
Cube: F=6,E=12,V=8. Cuboid: F=6,E=12,V=8. Triangular prism: F=5,E=9,V=6.
Square pyramid: F=5,E=8,V=5. Tetrahedron: F=4,E=6,V=4.
Cylinder: F=3(2 circles+1 curved),E=2 curved,V=0. Cone: F=2,E=1,V=1(apex). Sphere: F=1,E=0,V=0.
Euler's formula for polyhedra: F+V-E=2. Cylinder/cone/sphere NOT polyhedra.
Cube: F+V-E=6+8-12=2. Tetrahedron: 4+4-6=2. Triangular prism: 5+6-9=2.
Nets: 2D folded into 3D. Cube has exactly 11 valid nets.
Views: Cylinder→front=rectangle, top=circle. Cone→front=triangle, top=circle with point.
Cross-section: cube horizontal=square. Cone through apex=triangle. Cone parallel to base=circle.
Cylinder has 3 faces not 2. Cube has 12 edges (4 top+4 bottom+4 vertical).""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_7", "chapter": "ch15", "difficulty": "beginner"}),

    # ── ORIGINAL 6 DOCUMENTS (backward compatibility) ───────────────

    Document(page_content="""Calculus Fundamentals:
Power Rule: d/dx[x^n]=n*x^(n-1). Product Rule: d/dx[f*g]=f'g+fg'.
Chain Rule: d/dx[f(g(x))]=f'(g(x))*g'(x). Quotient Rule: d/dx[f/g]=(f'g-fg')/g^2.
d/dx[sin(x)]=cos(x), d/dx[cos(x)]=-sin(x), d/dx[e^x]=e^x, d/dx[ln(x)]=1/x.
integral(x^n dx)=x^(n+1)/(n+1)+C, integral(e^x dx)=e^x+C.
Fundamental Theorem: integral[a to b]f(x)dx=F(b)-F(a) where F'(x)=f(x).""",
    metadata={"source": "knowledge_base", "topic": "calculus", "class_level": "class_12", "difficulty": "advanced"}),

    Document(page_content="""Linear Algebra Essentials:
Matrix multiplication: row-by-column. Determinant 2x2: ad-bc.
Inverse: A^(-1)=adj(A)/det(A), exists iff det(A)≠0.
Eigenvalues: det(A-lambda*I)=0. Eigenvectors: solve (A-lambda*I)v=0.
Rank-Nullity: rank(A)+nullity(A)=n. Dot product: u·v=|u||v|cos(theta). Orthogonal: u·v=0.""",
    metadata={"source": "knowledge_base", "topic": "linear_algebra", "class_level": "class_12", "difficulty": "advanced"}),

    Document(page_content="""Statistics and Probability:
Mean=sum(x)/n. Variance=sum((x-mu)^2)/n. SD=sqrt(variance).
P(A∪B)=P(A)+P(B)-P(A∩B). P(A|B)=P(A∩B)/P(B).
Bayes: P(A|B)=P(B|A)*P(A)/P(B).
Binomial: P(X=k)=C(n,k)*p^k*(1-p)^(n-k).
CLT: sample means approach normal distribution as n increases.""",
    metadata={"source": "knowledge_base", "topic": "statistics", "class_level": "class_11", "difficulty": "intermediate"}),

    Document(page_content="""Algebra and Number Theory:
Quadratic: x=(-b±sqrt(b^2-4ac))/2a. D=b^2-4ac.
D>0: two real roots. D=0: repeated root. D<0: complex roots.
log(ab)=log(a)+log(b). log(a^n)=n*log(a).
a^2-b^2=(a+b)(a-b). a^3+b^3=(a+b)(a^2-ab+b^2).
AP: S_n=n/2*(2a+(n-1)d). GP: S=a(1-r^n)/(1-r). Infinite GP: a/(1-r) for |r|<1.""",
    metadata={"source": "knowledge_base", "topic": "algebra", "class_level": "class_10", "difficulty": "intermediate"}),

    Document(page_content="""Trigonometry:
sin^2(x)+cos^2(x)=1. tan(x)=sin(x)/cos(x).
sin(A+B)=sinA*cosB+cosA*sinB. cos(A+B)=cosA*cosB-sinA*sinB.
sin(2x)=2sin(x)cos(x). cos(2x)=cos^2(x)-sin^2(x).
Values: sin30=1/2, sin45=sqrt(2)/2, sin60=sqrt(3)/2, sin90=1.
Law of Sines: a/sinA=b/sinB=c/sinC. Law of Cosines: c^2=a^2+b^2-2ab*cosC.""",
    metadata={"source": "knowledge_base", "topic": "trigonometry", "class_level": "class_10", "difficulty": "intermediate"}),

    Document(page_content="""Discrete Mathematics:
Permutations: P(n,r)=n!/(n-r)!. Combinations: C(n,r)=n!/(r!*(n-r)!).
GCD(a,b)=GCD(b,a mod b). LCM(a,b)=a*b/GCD(a,b).
Modular: a≡b(mod n) means n divides (a-b).
Fermat's Little: a^(p-1)≡1(mod p) for prime p.
De Morgan: NOT(A AND B)=NOT(A) OR NOT(B).""",
    metadata={"source": "knowledge_base", "topic": "discrete_math", "class_level": "class_11", "difficulty": "advanced"}),

    # ── CLASS 8 — All 16 Chapters ───────────────────────────────────

    Document(page_content="""Class 8 | Ch1: Rational Numbers
Rational number: p/q where p,q integers and q≠0. Includes integers, fractions, terminating and repeating decimals.
PROPERTIES OF RATIONAL NUMBERS:
Closure: rationals closed under +,-,×. Division closed except by zero.
Commutativity: a+b=b+a, a×b=b×a. NOT for subtraction or division.
Associativity: (a+b)+c=a+(b+c), (a×b)×c=a×(b×c). NOT for subtraction or division.
Distributivity: a×(b+c)=a×b+a×c.
Additive identity: 0. Multiplicative identity: 1.
Additive inverse of p/q is -p/q. Multiplicative inverse (reciprocal) of p/q is q/p.
REPRESENTATION ON NUMBER LINE:
Between any two rational numbers there are infinite rational numbers (dense property).
Standard form: denominator positive and HCF of numerator and denominator=1.
FINDING RATIONAL NUMBERS BETWEEN TWO NUMBERS:
Method 1: find mean (average) of the two numbers repeatedly.
Method 2: convert to same denominator with larger LCM.
Between -1/2 and 1/3: mean=(-1/2+1/3)/2=(-1/6)/2=-1/12. Continue for more.
SOLVED EXAMPLES:
Example 1: Find 5 rational numbers between -1/2 and 1/3.
Convert: -1/2=-9/18 and 1/3=6/18. Between -9/18 and 6/18: -8/18,-7/18,-6/18,-5/18,-4/18.
Simplified: -4/9, -7/18, -1/3, -5/18, -2/9.
Example 2: Verify -2/3 + 4/5 = 4/5 + (-2/3) (commutativity)
LHS: (-10+12)/15=2/15. RHS: (12-10)/15=2/15. Equal, commutativity verified.
COMMON MISTAKES:
Between any two rationals there are INFINITE rationals, not finite.
Reciprocal of 0 does NOT exist. Reciprocal of 1 is 1. Reciprocal of -1 is -1.""",
    metadata={"source": "ncert", "topic": "numbers", "class_level": "class_8", "chapter": "ch1", "difficulty": "beginner"}),

    Document(page_content="""Class 8 | Ch2: Linear Equations in One Variable
Linear equation: variable has power 1 only. ax+b=c form.
Can involve fractions and variables on both sides.
SOLVING EQUATIONS WITH VARIABLES ON BOTH SIDES:
Collect variable terms on one side, constants on other.
3x+2=5x-4 → 2+4=5x-3x → 6=2x → x=3.
SOLVING EQUATIONS WITH FRACTIONS:
Multiply both sides by LCM of all denominators to clear fractions.
(2x+3)/5-(x-4)/3=2. LCM=15. Multiply: 3(2x+3)-5(x-4)=30.
6x+9-5x+20=30 → x+29=30 → x=1.
WORD PROBLEMS - STANDARD TYPES:
Age problems: Let present age=x. Set up equation from given conditions.
Number problems: Let number=x. Translate words to equation.
Geometry problems: Use perimeter/area formulas.
Money/mixture problems: Set up equation for totals.
SOLVED EXAMPLES:
Example 1: (2x+3)/5-(x-4)/3=2
Multiply by 15: 3(2x+3)-5(x-4)=30 → 6x+9-5x+20=30 → x=1.
Verify: (2+3)/5-(1-4)/3=1+1=2. Correct.
Example 2: A number is 4 more than twice another. Sum=40.
Let numbers be x and 2x+4. x+(2x+4)=40 → 3x=36 → x=12.
Numbers: 12 and 28. Verify: 12+28=40 and 28=2(12)+4. Correct.
Example 3: Present age ratio of A and B is 3:4. After 5 years ratio becomes 4:5. Find ages.
Let ages: 3x and 4x. (3x+5)/(4x+5)=4/5 → 15x+25=16x+20 → x=5.
Ages: 15 and 20.
COMMON MISTAKES:
When multiplying by LCM, multiply EVERY term including constants.
Verify answer by substituting back in ORIGINAL equation.""",
    metadata={"source": "ncert", "topic": "algebra", "class_level": "class_8", "chapter": "ch2", "difficulty": "beginner"}),

    Document(page_content="""Class 8 | Ch3: Understanding Quadrilaterals
ANGLE SUM PROPERTY:
Sum of interior angles of polygon with n sides = (n-2)×180°.
Triangle(n=3): (3-2)×180=180°.
Quadrilateral(n=4): (4-2)×180=360°.
Pentagon(n=5): 540°. Hexagon(n=6): 720°.
Sum of exterior angles of ANY convex polygon = 360°.
TYPES OF QUADRILATERALS AND PROPERTIES:
Trapezium: one pair of parallel sides. Area=(1/2)×(sum of parallel sides)×height.
Kite: two pairs of adjacent sides equal. One diagonal bisects the other at right angles.
Parallelogram: opposite sides parallel and equal, opposite angles equal, diagonals bisect each other.
Rectangle: parallelogram with all right angles, diagonals equal.
Rhombus: parallelogram with all sides equal, diagonals bisect at right angles.
Square: all sides equal, all angles 90°, diagonals equal and bisect at right angles.
HIERARCHY: Square → Rectangle → Parallelogram → Quadrilateral.
Square is special rhombus AND special rectangle.
SOLVED EXAMPLES:
Example 1: In parallelogram ABCD, angle A=75°.
Angle C=75° (opposite angles equal). Angle B=180-75=105° (co-interior=180°). Angle D=105°.
Example 2: Exterior angle of regular polygon=40°. How many sides?
Number of sides=360°/40°=9 sides.
Example 3: In kite ABCD, AB=AD=5cm, BC=DC=8cm. diagonal AC=6cm. Find BD.
Diagonals of kite are perpendicular. One diagonal bisects the other.
COMMON MISTAKES:
All rectangles are parallelograms but NOT all parallelograms are rectangles.
Rhombus diagonals bisect at 90° but are NOT equal. Rectangle diagonals are equal but NOT at 90°.
Sum of angles of quadrilateral=360° (not 180°).""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_8", "chapter": "ch3", "difficulty": "beginner"}),

    Document(page_content="""Class 8 | Ch4: Practical Geometry (Quadrilaterals)
A quadrilateral has 4 sides, 4 angles, 2 diagonals = 10 measurements total.
Minimum 5 measurements needed to uniquely construct a quadrilateral.
CONSTRUCTION CASES:
Case 1 — Four sides and one diagonal (SSS triangles method):
Draw diagonal first, construct both triangles on either side.
Case 2 — Two diagonals and three sides:
Draw one diagonal, use given measurements to find vertices.
Case 3 — Two adjacent sides and three angles:
Use angles to set directions, mark lengths.
Case 4 — Three sides and two included angles:
Draw one side, use angles at both ends.
Case 5 — Special quadrilaterals (rhombus, rectangle, square):
Use their special properties to simplify construction.
CONSTRUCTING QUADRILATERAL ABCD (4 sides + 1 diagonal):
Given: AB=4cm, BC=3.5cm, CD=4.5cm, DA=3cm, AC=5cm.
Step 1: Draw AC=5cm (diagonal).
Step 2: From A, draw arc radius 4cm. From C, draw arc radius 3.5cm. Intersection=B.
Step 3: From A, draw arc radius 3cm. From C, draw arc radius 4.5cm. Intersection=D.
Step 4: Join all vertices. ABCD is the required quadrilateral.
RHOMBUS CONSTRUCTION: Both diagonals given (they bisect at right angles at midpoint).
RECTANGLE CONSTRUCTION: One side and one diagonal (use Pythagoras to find other side).
COMMON MISTAKES:
Check if given measurements form a valid quadrilateral before constructing.
In rhombus construction, diagonals bisect each other at 90°, not just bisect.""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_8", "chapter": "ch4", "difficulty": "beginner"}),

    Document(page_content="""Class 8 | Ch5: Data Handling
GROUPED DATA AND FREQUENCY:
Class interval: range of values grouped together. e.g., 0-10, 10-20, 20-30.
Class width = upper limit - lower limit.
Frequency: number of observations in each class.
Cumulative frequency: sum of all frequencies up to that class.
HISTOGRAM: bar graph for continuous data (no gaps between bars).
CIRCLE GRAPH (PIE CHART):
Central angle for each component = (component value/total) × 360°.
Example: Wheat 40% → angle = 0.40×360 = 144°.
PROBABILITY:
Experiment: activity with outcomes (throwing die, tossing coin).
Event: collection of one or more outcomes.
P(event) = number of favourable outcomes / total number of outcomes.
P(sure event)=1. P(impossible event)=0. 0≤P(E)≤1.
P(E)+P(not E)=1. So P(not E)=1-P(E).
SOLVED EXAMPLES:
Example 1: Die thrown. Find P(number>4).
Favourable: 5,6 → 2 outcomes. Total=6. P=2/6=1/3.
Example 2: Pie chart for budget. Food=40%, Rent=25%, Education=20%, Others=15%.
Angles: Food=144°, Rent=90°, Education=72°, Others=54°. Total=360°.
Example 3: P(drawing red card from deck)=26/52=1/2.
P(face card)=12/52=3/13. P(ace)=4/52=1/13.
COMMON MISTAKES:
In histogram, class intervals must be continuous (no gaps).
P(E)+P(not E)=1 always. P(E) cannot be greater than 1 or negative.""",
    metadata={"source": "ncert", "topic": "statistics", "class_level": "class_8", "chapter": "ch5", "difficulty": "beginner"}),

    Document(page_content="""Class 8 | Ch6: Squares and Square Roots
PERFECT SQUARES: 1,4,9,16,25,36,49,64,81,100,121,144,169,196,225...
Properties:
A number ending in 2,3,7,8 is NEVER a perfect square.
A perfect square ending in 1 → number ends in 1 or 9.
A perfect square ending in 4 → number ends in 2 or 8.
A perfect square ending in 9 → number ends in 3 or 7.
A perfect square ending in 6 → number ends in 4 or 6.
Number of zeros at end of perfect square is always EVEN.
SQUARE ROOT METHODS:
Method 1 - Prime factorisation: pair up prime factors, take one from each pair.
sqrt(1764): 1764=2^2×3^2×7^2 → sqrt=2×3×7=42.
Method 2 - Long division: group digits in pairs from right, find largest square≤group.
PYTHAGOREAN TRIPLETS PATTERN:
For any m>1: (2m, m²-1, m²+1) form a Pythagorean triplet.
m=2: (4,3,5). m=3: (6,8,10). m=4: (8,15,17).
ESTIMATING SQUARE ROOT: find between which two consecutive perfect squares the number lies.
sqrt(200): between sqrt(196)=14 and sqrt(225)=15. Closer to 14.
SOLVED EXAMPLES:
Example 1: Is 1352 a perfect square?
1352=2^3×13^2. Power of 2 is odd (3), so NOT a perfect square.
To make perfect square: multiply by 2 → 2704=2^4×13^2=(2^2×13)^2=52^2.
Example 2: Find least number to multiply 675 to make perfect square.
675=3^3×5^2. Need one more 3: multiply by 3 → 2025=45^2.
COMMON MISTAKES:
sqrt(a^2+b^2) ≠ a+b. sqrt(25+144)=sqrt(169)=13, NOT 5+12=17.
A number ending in 0 is perfect square only if it ends in EVEN number of zeros.""",
    metadata={"source": "ncert", "topic": "numbers", "class_level": "class_8", "chapter": "ch6", "difficulty": "beginner"}),

    Document(page_content="""Class 8 | Ch7: Cubes and Cube Roots
PERFECT CUBES: 1,8,27,64,125,216,343,512,729,1000...
1^3=1, 2^3=8, 3^3=27, 4^3=64, 5^3=125, 6^3=216, 7^3=343, 8^3=512, 9^3=729, 10^3=1000.
PROPERTIES OF CUBES:
Cube of even number is even. Cube of odd number is odd.
Cube of negative number is negative: (-2)^3=-8.
A perfect cube can end in any digit 0-9 (unlike squares).
CUBE ROOT BY PRIME FACTORISATION:
Group prime factors in sets of 3. Take one from each group.
cbrt(13824): 13824=2^9×3^3=(2^3)^3×3^3=(8×3)^3=24^3. So cbrt(13824)=24.
FINDING SMALLEST MULTIPLIER/DIVISOR:
To make a perfect cube: each prime factor must appear in multiples of 3.
675=3^3×5^2. Need one more 5^1 to make 5^3. Multiply by 5. 675×5=3375=15^3.
SOLVED EXAMPLES:
Example 1: cbrt(13824). 13824=2×6912=2×2×3456=...=2^9×3^3. cbrt=2^3×3=24.
Example 2: Is 1728 a perfect cube? 1728=2^6×3^3=(2^2×3)^3=12^3. YES, cbrt=12.
Example 3: Find smallest number to divide 81 to make perfect cube.
81=3^4. Need to remove one 3 (keep 3^3). Divide by 3. 81÷3=27=3^3. Answer: 3.
Example 4: What is cube of -5? (-5)^3=-125.
COMMON MISTAKES:
cbrt(-8)=-2 (negative cube root exists, unlike square roots).
cbrt(a^3+b^3) ≠ a+b. Must factorise properly.
Perfect cube can end in any digit, not restricted like perfect squares.""",
    metadata={"source": "ncert", "topic": "numbers", "class_level": "class_8", "chapter": "ch7", "difficulty": "beginner"}),

    Document(page_content="""Class 8 | Ch8: Comparing Quantities (Compound Interest)
RECAP - PROFIT/LOSS AND SIMPLE INTEREST:
Profit%=(Profit/CP)×100. Loss%=(Loss/CP)×100.
SI=(P×R×T)/100. Amount=P+SI=P(1+RT/100).
COMPOUND INTEREST:
Interest calculated on principal AND accumulated interest.
Formula: A=P(1+R/100)^n where P=principal, R=rate%, n=time in years.
CI=A-P=P[(1+R/100)^n - 1].
Compounded half-yearly: A=P(1+R/200)^(2n) (rate halved, time doubled).
Compounded quarterly: A=P(1+R/400)^(4n).
CI>SI for same P,R,T (except for 1 year when CI=SI).
DIFFERENCE FORMULA (for 2 years):
CI-SI = P×(R/100)^2.
APPLICATIONS:
Population growth: P_n=P_0(1+R/100)^n.
Depreciation: V_n=V_0(1-R/100)^n.
SOLVED EXAMPLES:
Example 1: CI on 12000 at 10% for 2 years compounded annually.
A=12000(1+10/100)^2=12000×(1.1)^2=12000×1.21=14520.
CI=14520-12000=2520.
SI=12000×10×2/100=2400.
CI-SI=2520-2400=120=12000×(10/100)^2=12000×0.01=120. Verified.
Example 2: CI on 8000 at 10% for 1.5 years compounded half-yearly.
Rate per half year=5%, number of periods=3.
A=8000(1+5/100)^3=8000×(1.05)^3=8000×1.157625=9261.
Example 3: Population 20000, grows 5% per year. After 2 years?
P=20000(1.05)^2=20000×1.1025=22050.
COMMON MISTAKES:
For half-yearly compounding: halve the rate AND double the time period.
CI and SI are EQUAL only for first year. After that CI>SI.""",
    metadata={"source": "ncert", "topic": "arithmetic", "class_level": "class_8", "chapter": "ch8", "difficulty": "intermediate"}),

    Document(page_content="""Class 8 | Ch9: Algebraic Expressions and Identities
MULTIPLICATION OF ALGEBRAIC EXPRESSIONS:
Monomial × Monomial: multiply coefficients, add powers. 3x^2 × 4x^3=12x^5.
Monomial × Polynomial: distribute. 2x(3x^2-5x+1)=6x^3-10x^2+2x.
Polynomial × Polynomial: each term of first × each term of second.
STANDARD ALGEBRAIC IDENTITIES:
Identity 1: (a+b)^2 = a^2+2ab+b^2
Identity 2: (a-b)^2 = a^2-2ab+b^2
Identity 3: (a+b)(a-b) = a^2-b^2
Identity 4: (x+a)(x+b) = x^2+(a+b)x+ab
USING IDENTITIES FOR CALCULATIONS:
105^2=(100+5)^2=10000+1000+25=11025.
98×102=(100-2)(100+2)=10000-4=9996.
FACTORISATION USING IDENTITIES:
x^2+8x+16=(x+4)^2. Check: 2×4=8, 4^2=16. Correct.
9a^2-12ab+4b^2=(3a-2b)^2. Check: 2×3a×2b=12ab. Correct.
x^2-25=(x+5)(x-5). (a^2-b^2 type)
SOLVED EXAMPLES:
Example 1: Expand (3x+2y)^2=9x^2+12xy+4y^2.
Example 2: Expand (4a-3b)^2=16a^2-24ab+9b^2.
Example 3: (2x+3)(2x+5)=4x^2+(3+5)2x+15=4x^2+16x+15. Using identity 4: (x+a)(x+b) with 2x,3,5.
Example 4: Evaluate 97^2=(100-3)^2=10000-600+9=9409.
COMMON MISTAKES:
(a+b)^2=a^2+2ab+b^2 NOT a^2+b^2 (missing middle term 2ab).
(a-b)^2=a^2-2ab+b^2 NOT a^2-2ab-b^2 (last term is always positive).
Factorisation: must check using expansion.""",
    metadata={"source": "ncert", "topic": "algebra", "class_level": "class_8", "chapter": "ch9", "difficulty": "intermediate"}),

    Document(page_content="""Class 8 | Ch10: Visualising Solid Shapes
VIEWS OF 3D OBJECTS:
Front view, Side view (left or right), Top view (plan view).
Different views give 2D shapes from different angles.
Cube: all views are squares.
Cuboid: views are rectangles (different dimensions for different views).
Cylinder: front/side=rectangle, top=circle.
Cone: front/side=triangle, top=circle with centre point.
Sphere: all views are circles.
MAPPING AND SCALE:
Map is a scale drawing of a region.
Scale: 1cm represents actual distance. Scale 1:50000 means 1cm=50000cm=500m.
Distance on map × scale = actual distance.
POLYHEDRA:
Polyhedron: solid with flat faces, all faces are polygons.
Regular polyhedra (Platonic solids): all faces identical regular polygons.
Tetrahedron: 4 equilateral triangular faces.
Cube: 6 square faces.
Octahedron: 8 equilateral triangular faces.
Dodecahedron: 12 regular pentagonal faces.
Icosahedron: 20 equilateral triangular faces.
Euler's formula: F+V-E=2 for all polyhedra.
NON-POLYHEDRA: cone, cylinder, sphere (have curved surfaces).
SOLVED EXAMPLES:
Example 1: Top view of a cone is a circle with a point (apex) at centre.
Example 2: Map scale 1:50000. Distance on map=3cm. Actual distance=3×50000cm=1.5km.
Example 3: Verify Euler: Octahedron F=8,V=6,E=12. F+V-E=8+6-12=2. Correct.
COMMON MISTAKES:
Cylinder and cone are NOT polyhedra (have curved surfaces).
Top view of cone shows circle with a dot in centre, not just a circle.""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_8", "chapter": "ch10", "difficulty": "beginner"}),

    Document(page_content="""Class 8 | Ch11: Mensuration
AREA FORMULAS:
Trapezium: A=(1/2)×(a+b)×h where a,b=parallel sides, h=height.
Rhombus: A=(1/2)×d1×d2 where d1,d2=diagonals.
General quadrilateral: A=(1/2)×diagonal×(sum of perpendiculars from opposite vertices).
Polygon: divide into triangles, sum their areas.
SURFACE AREA:
Cube: Total SA=6a^2. Lateral SA=4a^2.
Cuboid: Total SA=2(lb+bh+lh). Lateral SA=2(l+b)×h.
Cylinder: Total SA=2πr(r+h). Curved SA=2πrh. Base area=πr^2.
VOLUME:
Cube: V=a^3.
Cuboid: V=l×b×h.
Cylinder: V=πr^2h.
UNIT CONVERSIONS:
1m=100cm → 1m^2=10^4cm^2 → 1m^3=10^6cm^3.
1km=1000m → 1km^2=10^6m^2.
1 litre=1000cm^3=1000ml.
SOLVED EXAMPLES:
Example 1: Trapezium parallel sides 8cm and 5cm, height 4cm.
A=(1/2)(8+5)(4)=(1/2)(13)(4)=26cm^2.
Example 2: Cuboid 5×4×3cm.
Total SA=2(5×4+4×3+5×3)=2(20+12+15)=2×47=94cm^2.
Volume=5×4×3=60cm^3.
Example 3: Cylinder r=7cm, h=10cm.
Curved SA=2×(22/7)×7×10=440cm^2.
Total SA=440+2×(22/7)×49=440+308=748cm^2.
Volume=(22/7)×49×10=1540cm^3.
COMMON MISTAKES:
Trapezium area uses PERPENDICULAR height, not slant side.
Cylinder Total SA includes BOTH circular ends (2πr^2) plus curved surface.
Volume of cylinder=πr^2×h (cross-section area × height).""",
    metadata={"source": "ncert", "topic": "mensuration", "class_level": "class_8", "chapter": "ch11", "difficulty": "intermediate"}),

    Document(page_content="""Class 8 | Ch12: Exponents and Powers
NEGATIVE EXPONENTS:
a^(-n)=1/a^n for any non-zero a. 2^(-3)=1/8. 10^(-4)=0.0001.
a^(-1)=1/a (reciprocal).
LAWS (extend from Class 7 to include negative exponents):
a^m × a^n=a^(m+n). a^m ÷ a^n=a^(m-n). (a^m)^n=a^(mn).
a^m × b^m=(ab)^m. a^m ÷ b^m=(a/b)^m. a^0=1.
These ALL work for negative exponents too.
STANDARD FORM (SCIENTIFIC NOTATION):
Number between 1 and 10 multiplied by integer power of 10.
Large: 6,020,000,000=6.02×10^9.
Small: 0.000000000016=1.6×10^(-11).
To compare: larger power of 10=larger number.
EXPRESSING IN STANDARD FORM:
Move decimal point until you get a number between 1 and 10.
Number of places moved = power of 10 (positive if moved left, negative if moved right).
485 → move 2 left → 4.85×10^2.
0.00605 → move 3 right → 6.05×10^(-3).
SOLVED EXAMPLES:
Example 1: (2^(-3)×3^(-2))÷(6^(-1)).
=1/8×1/9÷1/6=1/72×6=6/72=1/12.
Example 2: (5/3)^(-2)×(3/5)^3=(3/5)^2×(3/5)^3=(3/5)^5=243/3125.
Example 3: Express 0.00000605 in standard form.
Move decimal 6 places right → 6.05×10^(-6).
COMMON MISTAKES:
2^(-3) = 1/8 NOT -8. Negative exponent means reciprocal, not negative number.
(a/b)^(-n)=(b/a)^n. So (2/3)^(-2)=(3/2)^2=9/4.
In scientific notation, first number MUST be between 1 and 10.""",
    metadata={"source": "ncert", "topic": "numbers", "class_level": "class_8", "chapter": "ch12", "difficulty": "intermediate"}),

    Document(page_content="""Class 8 | Ch13: Direct and Inverse Proportion
DIRECT PROPORTION:
x and y are in direct proportion if x/y=k (constant) or x1/y1=x2/y2.
As x increases, y increases proportionally. Symbol: x∝y.
Graph: straight line through origin.
Examples: cost∝quantity, distance∝time(constant speed), simple interest∝time.
INVERSE PROPORTION:
x and y are in inverse proportion if xy=k (constant) or x1×y1=x2×y2.
As x increases, y decreases proportionally. Symbol: x∝1/y.
Graph: hyperbola (not straight line).
Examples: speed∝1/time, workers∝1/days, pipes∝1/fill time.
SOLVED EXAMPLES:
Example 1 (Direct): If 15 bags of rice cost ₹450, find cost of 24 bags.
15/450=24/x → x=24×450/15=₹720. OR cost per bag=30, 24×30=720.
Example 2 (Inverse): 8 workers finish in 12 days. How many days for 6 workers?
8×12=6×d → d=96/6=16 days. (fewer workers → more days → inverse)
Example 3 (Inverse): 3 pipes fill tank in 8 hours. How long for 4 pipes?
3×8=4×t → t=24/4=6 hours.
Example 4: Car travels 150km in 3 hours. How long for 250km at same speed?
3/150=t/250 → t=500/100=5 hours. (direct proportion)
IDENTIFYING TYPE:
More→More: Direct proportion.
More→Less: Inverse proportion.
Workers and days: MORE workers, LESS days → INVERSE.
Speed and time: MORE speed, LESS time → INVERSE.
COMMON MISTAKES:
Workers and days is INVERSE not direct.
In inverse proportion: x1×y1=x2×y2 (NOT x1/y1=x2/y2).""",
    metadata={"source": "ncert", "topic": "arithmetic", "class_level": "class_8", "chapter": "ch13", "difficulty": "beginner"}),

    Document(page_content="""Class 8 | Ch14: Factorisation
METHODS OF FACTORISATION:
Method 1 - Common Factor: take out HCF of all terms.
12x^2y-9xy^2+6xyz = 3xy(4x-3y+2z).
Method 2 - Grouping: group terms to find common factor.
ax+ay+bx+by = a(x+y)+b(x+y) = (a+b)(x+y).
a^2-b^2+a-b = (a-b)(a+b)+(a-b) = (a-b)(a+b+1).
Method 3 - Using Identities:
x^2+8x+16 = x^2+2(4)x+4^2 = (x+4)^2.
4x^2-9 = (2x)^2-3^2 = (2x+3)(2x-3).
Method 4 - Splitting Middle Term (for quadratics ax^2+bx+c):
Find two numbers p,q such that p+q=b and p×q=a×c.
x^2+7x+12: p+q=7, p×q=12 → p=3,q=4. So x^2+3x+4x+12=x(x+3)+4(x+3)=(x+3)(x+4).
2x^2+7x+3: p+q=7, p×q=2×3=6 → p=6,q=1. So 2x^2+6x+x+3=2x(x+3)+1(x+3)=(2x+1)(x+3).
DIVISION OF ALGEBRAIC EXPRESSIONS:
Polynomial ÷ Monomial: divide each term separately.
(6x^3-4x^2+2x) ÷ 2x = 3x^2-2x+1.
Polynomial ÷ Polynomial: factorise numerator and denominator, cancel common factors.
SOLVED EXAMPLES:
Example 1: Factorise 12x^2y-9xy^2+6xyz = 3xy(4x-3y+2z).
Example 2: x^2+7x+12 = (x+3)(x+4). Verify: (x+3)(x+4)=x^2+7x+12. Correct.
Example 3: 2x^2+7x+3. Product=6, sum=7. Factors: 6 and 1. = (2x+1)(x+3).
COMMON MISTAKES:
Always take out the COMPLETE HCF in method 1 (common factor).
When splitting middle term: product must equal a×c (coefficient of x^2 × constant).
Verify factorisation by expanding back.""",
    metadata={"source": "ncert", "topic": "algebra", "class_level": "class_8", "chapter": "ch14", "difficulty": "intermediate"}),

    Document(page_content="""Class 8 | Ch15: Introduction to Graphs
TYPES OF GRAPHS:
Bar graph: compares discrete data using bars.
Line graph: shows change over time (continuous data).
Pie chart: shows proportions (parts of a whole).
Histogram: bar graph for continuous grouped data (no gaps).
LINEAR GRAPHS:
Equation of straight line: y=mx+c where m=slope, c=y-intercept.
x-intercept: point where line crosses x-axis (y=0).
y-intercept: point where line crosses y-axis (x=0).
Slope m: if line passes through (x1,y1) and (x2,y2): m=(y2-y1)/(x2-x1).
PLOTTING POINTS AND GRAPHS:
For any linear equation, find at least 2 points (3 to verify).
For x+y=5: when x=0,y=5. When x=5,y=0. When x=2,y=3.
Plot these points and join with straight line.
READING GRAPHS:
Distance-time graph: slope=speed. Horizontal line=stationary. Steep line=fast.
Temperature-time graph: shows heating/cooling patterns.
APPLICATIONS:
Finding values from graph (interpolation and extrapolation).
Conversion graphs: between units (km to miles, °C to °F).
SOLVED EXAMPLES:
Example 1: Draw graph of y=2x+1. Plot (-1,-1), (0,1), (1,3). Join them.
Example 2: For graph x+2y=6, find x and y intercepts.
x-intercept (y=0): x=6. y-intercept (x=0): y=3.
Example 3: Plot points A(2,3), B(-1,4), C(0,-2).
A: right 2, up 3. B: left 1, up 4. C: at origin, down 2.
Example 4: Distance-time graph, car goes 60km in 1 hour. Speed=60/1=60kmph.
COMMON MISTAKES:
x-intercept: set y=0 (NOT x=0). y-intercept: set x=0.
Plotting: x-coordinate first (horizontal), then y-coordinate (vertical).
In distance-time graph, slope=speed. Greater slope=greater speed.""",
    metadata={"source": "ncert", "topic": "algebra", "class_level": "class_8", "chapter": "ch15", "difficulty": "beginner"}),

    Document(page_content="""Class 8 | Ch16: Playing With Numbers
NUMBERS IN GENERAL FORM:
2-digit number ab = 10a+b (a=tens digit, b=units digit).
3-digit number abc = 100a+10b+c.
Example: 57 = 10×5+7. 347 = 100×3+10×4+7.
REVERSING DIGITS:
2-digit number ab=10a+b. Reversed ba=10b+a.
Sum: (10a+b)+(10b+a)=11(a+b). Always divisible by 11.
Difference: (10a+b)-(10b+a)=9(a-b). Always divisible by 9.
3-digit number abc=100a+10b+c. Reversed cba=100c+10b+a.
Difference: (100a+10b+c)-(100c+10b+a)=99(a-c). Always divisible by 99.
CYCLIC NUMBERS (3 digits abc, bca, cab):
abc+bca+cab=111(a+b+c). Always divisible by 111 and 3.
LETTERS FOR DIGITS (cryptarithmetic):
Each letter represents a unique digit. Use logic to find values.
AB+BA=121 → (10a+b)+(10b+a)=11(a+b)=121 → a+b=11.
DIVISIBILITY TESTS REVISITED:
Div by 3: sum of digits divisible by 3.
Div by 9: sum of digits divisible by 9.
Div by 11: (sum of odd position digits)-(sum of even position digits)=0 or multiple of 11.
SOLVED EXAMPLES:
Example 1: A 2-digit number is 4 times sum of its digits. If 18 added, digits reverse.
Let number=10a+b. 10a+b=4(a+b) → 10a+b=4a+4b → 6a=3b → b=2a.
After adding 18: 10a+b+18=10b+a → 9a-9b=-18 → b-a=2.
From b=2a and b-a=2: 2a-a=2 → a=2, b=4. Number=24.
Verify: 24=4×(2+4)=4×6=24. 24+18=42 (digits reversed). Correct.
Example 2: If 1A×A=9A where A is same digit, find A.
Try A=5: 15×5=75=9×5? No. Try A=6: 16×6=96=9×6? 9×6=54. No. 
Think: 1A×A means (10+A)×A=10A+A^2. This should equal 90+A.
10A+A^2=90+A → A^2+9A-90=0 → (A+15)(A-6)=0 → A=6.
Check: 16×6=96. Yes! 1A×A=16×6=96=9A where A=6.
COMMON MISTAKES:
General form of 2-digit number ab is 10a+b NOT a×b or a+b.
When digits are reversed: the tens digit becomes units and vice versa.""",
    metadata={"source": "ncert", "topic": "numbers", "class_level": "class_8", "chapter": "ch16", "difficulty": "intermediate"}),


    # ── CLASS 9 — All 15 Chapters ───────────────────────────────────

    Document(page_content="""Class 9 | Ch1: Number Systems
RATIONAL NUMBERS: p/q form where q≠0. Terminating or repeating decimals.
IRRATIONAL NUMBERS: cannot be written as p/q. Non-terminating non-repeating decimals.
Examples: sqrt(2), sqrt(3), sqrt(5), pi, e.
REAL NUMBERS = Rational + Irrational numbers.
PROVING IRRATIONALITY (contradiction method):
Assume sqrt(2) is rational → sqrt(2)=p/q (lowest terms, HCF=1).
Squaring: 2=p^2/q^2 → p^2=2q^2 → p^2 is even → p is even → p=2m.
4m^2=2q^2 → q^2=2m^2 → q is even. Both p,q even contradicts HCF=1. So sqrt(2) is irrational.
REPRESENTATION ON NUMBER LINE:
sqrt(n) on number line: draw right triangle with legs 1 and sqrt(n-1), hypotenuse=sqrt(n).
sqrt(2): right triangle with both legs=1. Hypotenuse=sqrt(2). Mark on number line.
OPERATIONS ON REAL NUMBERS:
sqrt(a) × sqrt(b) = sqrt(ab). sqrt(a)/sqrt(b)=sqrt(a/b).
(sqrt(a)+sqrt(b))(sqrt(a)-sqrt(b))=a-b.
RATIONALISATION: multiply numerator and denominator by conjugate.
3/(2+sqrt(3)): multiply by (2-sqrt(3))/(2-sqrt(3)) = 3(2-sqrt(3))/(4-3) = 3(2-sqrt(3)) = 6-3sqrt(3).
5/(sqrt(7)-sqrt(2)): multiply by (sqrt(7)+sqrt(2)) = 5(sqrt(7)+sqrt(2))/(7-2) = sqrt(7)+sqrt(2).
LAWS OF EXPONENTS FOR REAL NUMBERS:
a^m × a^n = a^(m+n). (a^m)^n = a^(mn). a^m × b^m = (ab)^m.
a^(1/n) = nth root of a. a^(m/n) = (nth root of a)^m.
SOLVED EXAMPLES:
Example 1: Simplify (sqrt(5)+sqrt(3))^2 = 5+2sqrt(15)+3 = 8+2sqrt(15).
Example 2: Rationalise 1/(sqrt(5)+sqrt(2)) = (sqrt(5)-sqrt(2))/((sqrt(5))^2-(sqrt(2))^2) = (sqrt(5)-sqrt(2))/3.
Example 3: Express 2^(1/2) × 2^(1/3) = 2^(1/2+1/3) = 2^(5/6).
COMMON MISTAKES:
sqrt(a+b) ≠ sqrt(a)+sqrt(b). sqrt(9+16)=sqrt(25)=5, NOT 3+4=7.
Irrational + Rational = Irrational. Irrational × Irrational can be rational: sqrt(2)×sqrt(2)=2.""",
    metadata={"source": "ncert", "topic": "numbers", "class_level": "class_9", "chapter": "ch1", "difficulty": "intermediate"}),

    Document(page_content="""Class 9 | Ch2: Polynomials
POLYNOMIAL: p(x) = a_n*x^n + a_(n-1)*x^(n-1) + ... + a_1*x + a_0 where coefficients are real numbers.
Degree: highest power of variable. Linear(degree 1), Quadratic(degree 2), Cubic(degree 3).
Zero polynomial: p(x)=0. Degree not defined.
Constant polynomial: p(x)=c. Degree=0.
ZEROES OF POLYNOMIAL: value of x where p(x)=0.
Linear polynomial ax+b has zero at x=-b/a.
Quadratic can have 0, 1 or 2 zeroes. Cubic can have 1, 2 or 3 zeroes.
REMAINDER THEOREM:
When p(x) is divided by (x-a), remainder = p(a).
No need to do long division — just substitute x=a.
p(x)=x^3-6x^2+11x-6 divided by (x-2): remainder=p(2)=8-24+22-6=0. So (x-2) is a factor.
FACTOR THEOREM:
(x-a) is a factor of p(x) if and only if p(a)=0.
To factorise: find a value 'a' where p(a)=0, then divide by (x-a).
FACTORISING CUBIC POLYNOMIALS:
Try factors of constant term. If p(a)=0, divide p(x) by (x-a) to get quadratic. Factorise quadratic.
ALGEBRAIC IDENTITIES:
(x+y+z)^2 = x^2+y^2+z^2+2xy+2yz+2zx.
(x+y)^3 = x^3+3x^2y+3xy^2+y^3 = x^3+y^3+3xy(x+y).
(x-y)^3 = x^3-3x^2y+3xy^2-y^3 = x^3-y^3-3xy(x-y).
x^3+y^3+z^3-3xyz = (x+y+z)(x^2+y^2+z^2-xy-yz-zx).
Special case: if x+y+z=0 then x^3+y^3+z^3=3xyz.
SOLVED EXAMPLES:
Example 1: Find remainder when x^3-6x^2+11x-6 divided by x-2.
p(2)=8-24+22-6=0. Remainder=0. So (x-2) is a factor.
Example 2: Factorise x^3-23x^2+142x-120.
Try x=1: 1-23+142-120=0. So (x-1) is factor.
Divide: x^3-23x^2+142x-120 = (x-1)(x^2-22x+120) = (x-1)(x-10)(x-12).
COMMON MISTAKES:
Degree of zero polynomial is undefined, not zero or -1.
Remainder theorem uses SUBSTITUTION, not division, for finding remainder quickly.
Factor theorem: (x-a) is factor iff p(a)=0 (note: x MINUS a, not x PLUS a).""",
    metadata={"source": "ncert", "topic": "algebra", "class_level": "class_9", "chapter": "ch2", "difficulty": "intermediate"}),

    Document(page_content="""Class 9 | Ch3: Coordinate Geometry
CARTESIAN PLANE:
Two perpendicular lines: x-axis (horizontal) and y-axis (vertical).
Origin O = (0,0). Point P = (x,y) where x=abscissa, y=ordinate.
QUADRANTS:
I: (+,+) — right of y-axis, above x-axis.
II: (-,+) — left of y-axis, above x-axis.
III: (-,-) — left of y-axis, below x-axis.
IV: (+,-) — right of y-axis, below x-axis.
Points ON axes: x-axis has y=0. y-axis has x=0.
PLOTTING POINTS:
Start at origin. Move right/left for x (positive=right, negative=left).
Then move up/down for y (positive=up, negative=down). Mark the point.
DISTANCE FORMULA (introduced here, developed in Class 10):
Distance between A(x1,y1) and B(x2,y2) = sqrt((x2-x1)^2+(y2-y1)^2).
COLLINEAR POINTS: three points lie on same straight line.
SECTION FORMULA (for later): divides line segment in given ratio.
GRAPHS OF LINEAR EQUATIONS:
y=x: line through origin at 45°. y=-x: line through origin at 135°.
x=a: vertical line. y=b: horizontal line.
SOLVED EXAMPLES:
Example 1: Plot A(3,4), B(-2,3), C(-4,-1), D(2,-3).
A: Quadrant I (both positive). B: Quadrant II. C: Quadrant III. D: Quadrant IV.
Example 2: Find distance between A(3,4) and B(-2,3).
AB = sqrt((-2-3)^2+(3-4)^2) = sqrt(25+1) = sqrt(26) units.
Example 3: In which quadrant is (-3,-5)?
Both negative → Quadrant III.
COMMON MISTAKES:
Point (3,4) is NOT same as (4,3). First coordinate is always x (horizontal).
Origin (0,0) is not in any quadrant — it's at the intersection of axes.
Points on x-axis have y-coordinate=0, not x-coordinate=0.""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_9", "chapter": "ch3", "difficulty": "beginner"}),

    Document(page_content="""Class 9 | Ch4: Linear Equations in Two Variables
FORM: ax+by+c=0 where a,b are not both zero. x and y are variables.
A linear equation in two variables has INFINITELY MANY solutions.
Each solution is an ordered pair (x,y) that satisfies the equation.
GRAPH OF LINEAR EQUATION IN TWO VARIABLES:
Graph is always a STRAIGHT LINE.
To draw: find at least 2 solutions (3 recommended to verify).
For 2x+3y=12:
x=0: 3y=12, y=4. Point (0,4).
y=0: 2x=12, x=6. Point (6,0).
x=3: 6+3y=12, y=2. Point (3,2). All 3 collinear confirms straight line.
X-INTERCEPT: point where line crosses x-axis. Set y=0 and solve for x.
Y-INTERCEPT: point where line crosses y-axis. Set x=0 and solve for y.
EQUATIONS OF SPECIAL LINES:
x=a: vertical line parallel to y-axis, passing through (a,0).
y=b: horizontal line parallel to x-axis, passing through (0,b).
y=x: line through origin, bisects I and III quadrants.
EXPRESSING WORD PROBLEMS AS LINEAR EQUATIONS:
"Cost of x pencils at 2 each and y pens at 5 each is 50": 2x+5y=50.
SOLVED EXAMPLES:
Example 1: Draw graph of 2x+3y=12. Find x and y intercepts.
y-intercept (x=0): y=4. So (0,4).
x-intercept (y=0): x=6. So (6,0).
Plot (0,4), (6,0), (3,2). Join them.
Example 2: Find 3 solutions of x+2y=8.
(0,4), (8,0), (2,3). Verify: 0+8=8, 8+0=8, 2+6=8. All correct.
COMMON MISTAKES:
A linear equation in two variables has infinite solutions (not just 2 or 3).
Every point on the graph is a solution. Every solution gives a point on the graph.
Graph of x=3 is a VERTICAL line (not a point on x-axis).""",
    metadata={"source": "ncert", "topic": "algebra", "class_level": "class_9", "chapter": "ch4", "difficulty": "beginner"}),

    Document(page_content="""Class 9 | Ch5: Introduction to Euclid's Geometry
EUCLID'S DEFINITIONS (important ones):
A point is that which has no part.
A line is breadthless length.
A surface has length and breadth only.
Ends of a line are points. Ends of a surface are lines.
EUCLID'S POSTULATES:
1. A straight line segment can be drawn from any point to any other point.
2. A terminated line (line segment) can be extended indefinitely.
3. A circle can be drawn with any centre and any radius.
4. All right angles are equal to each other.
5. Parallel postulate: If a line falls on two lines such that interior angles on one side sum less than two right angles, those two lines if extended will meet on that side.
EUCLID'S AXIOMS (Common Notions):
1. Things equal to the same thing are equal to each other.
2. If equals are added to equals, the wholes are equal.
3. If equals are subtracted from equals, the remainders are equal.
4. Things which coincide with one another are equal.
5. The whole is greater than the part.
UNDEFINED TERMS: point, line, plane (defined informally).
THEOREMS FROM POSTULATES:
Theorem 1: Two distinct lines cannot have more than one point in common.
Theorem 2: A unique line passes through two distinct points.
EQUIVALENT VERSIONS OF 5TH POSTULATE:
Given a line and a point not on it, exactly one parallel line passes through that point.
This is Playfair's axiom (equivalent to Euclid's 5th postulate).
SOLVED EXAMPLES:
Example 1: If AB=CD and EF=GH and AB=EF, prove CD=GH.
AB=CD (given). EF=GH (given). AB=EF (given).
By Axiom 1: CD=EF. By Axiom 1: CD=GH.
Example 2: How many lines through 2 distinct points? Exactly 1 (from Postulate 1).
COMMON MISTAKES:
Axioms are assumptions (self-evident truths). Theorems are proved from axioms and postulates.
The 5th postulate is NOT self-evident — this led to non-Euclidean geometry.""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_9", "chapter": "ch5", "difficulty": "beginner"}),

    Document(page_content="""Class 9 | Ch6: Lines and Angles
KEY THEOREMS (with proofs):
Theorem 1: If two lines intersect, vertically opposite angles are equal.
Proof: angle 1 + angle 2 = 180° (linear pair). angle 3 + angle 2 = 180° (linear pair).
So angle 1 = angle 3. Similarly angle 2 = angle 4.
Theorem 2: Sum of angles on a straight line = 180°.
Theorem 3: If transversal cuts parallel lines:
(a) Corresponding angles are equal.
(b) Alternate interior angles are equal.
(c) Co-interior angles are supplementary (sum=180°).
Theorem 4 (Converse): If corresponding angles are equal → lines are parallel.
ANGLE SUM PROPERTY OF TRIANGLE:
Sum of angles of triangle = 180°. Proof using parallel line through vertex.
Draw BC. Draw line PQ through A parallel to BC.
Angle PAB = Angle ABC (alternate interior). Angle QAC = Angle ACB (alternate interior).
Angle PAB + Angle BAC + Angle QAC = 180° (straight line PQ).
Therefore Angle ABC + Angle BAC + Angle ACB = 180°.
EXTERIOR ANGLE THEOREM:
Exterior angle of triangle = sum of two non-adjacent interior angles.
SOLVED EXAMPLES:
Example 1: Two parallel lines cut by transversal. One angle=65°.
All 8 angles: 65°, 115°, 65°, 115°, 65°, 115°, 65°, 115°.
Alternate interior=65° (equal). Co-interior=115° (supplementary). Corresponding=65° (equal).
Example 2: Prove vertically opposite angles are equal.
Lines AB and CD intersect at O.
Angle AOC + Angle AOD = 180° (linear pair on line CD).
Angle BOD + Angle AOD = 180° (linear pair on line AB).
Therefore Angle AOC = Angle BOD. (both equal 180° - Angle AOD)
COMMON MISTAKES:
Co-interior angles are SUPPLEMENTARY (sum=180°), not equal.
Exterior angle = sum of REMOTE interior angles, NOT the adjacent interior angle.""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_9", "chapter": "ch6", "difficulty": "intermediate"}),

    Document(page_content="""Class 9 | Ch7: Triangles (Congruence)
CONGRUENCE CRITERIA:
SAS: Two sides and included angle equal.
ASA: Two angles and included side equal.
AAS: Two angles and any corresponding side equal.
SSS: All three sides equal.
RHS: Right angle, hypotenuse and one side equal (right triangles).
IMPORTANT THEOREMS:
Theorem 1: Angles opposite equal sides of isosceles triangle are equal.
If AB=AC then Angle B=Angle C.
Proof: In triangles ABD and ACD (D=midpoint of BC):
AB=AC (given), BD=CD (D is midpoint), AD=AD (common). By SSS: triangles congruent. Angle B=Angle C by CPCT.
Theorem 2 (Converse): If two angles of triangle are equal, sides opposite them are equal.
Theorem 3: In right triangle, hypotenuse is the longest side.
Theorem 4: The sum of any two sides of triangle > third side.
Theorem 5: Of all line segments drawn from external point to line, perpendicular is shortest.
INEQUALITIES IN TRIANGLES:
In triangle, greater angle has greater opposite side.
If Angle A > Angle B then BC > AC.
CPCT: Corresponding Parts of Congruent Triangles.
SOLVED EXAMPLES:
Example 1: ABC is isosceles with AB=AC. D is midpoint of BC. Prove AD perpendicular to BC.
In triangles ABD and ACD: AB=AC, BD=CD, AD=AD. SSS congruence.
Angle ADB=Angle ADC (CPCT). Both on straight line, so each=90°. AD perpendicular to BC.
Example 2: Prove that triangle ABC where AB=BC=CA (equilateral) has all angles 60°.
AB=BC → Angle A=Angle C. BC=CA → Angle A=Angle B. So A=B=C. A+B+C=180°. Each=60°.
COMMON MISTAKES:
RHS works ONLY for right triangles. Cannot apply to other triangles.
CPCT used only AFTER proving congruence.
SAS: the angle must be INCLUDED (between the two sides).""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_9", "chapter": "ch7", "difficulty": "intermediate"}),

    Document(page_content="""Class 9 | Ch8: Quadrilaterals
ANGLE SUM: Sum of angles of quadrilateral=360°.
PARALLELOGRAM PROPERTIES:
(i) Opposite sides are parallel and equal.
(ii) Opposite angles are equal.
(iii) Consecutive angles are supplementary (sum=180°).
(iv) Diagonals bisect each other.
THEOREMS:
Theorem 1: Diagonal divides parallelogram into two congruent triangles.
Theorem 2: Opposite sides of parallelogram are equal (and converse).
Theorem 3: Opposite angles of parallelogram are equal (and converse).
Theorem 4: Diagonals of parallelogram bisect each other (and converse).
Theorem 5: Parallelograms on same base and between same parallels are equal in area.
MID-POINT THEOREM:
The line joining midpoints of two sides of triangle is parallel to third side and half its length.
If D=midpoint of AB and E=midpoint of AC then DE parallel to BC and DE=BC/2.
CONVERSE: Line through midpoint of one side parallel to another side bisects the third side.
SOLVED EXAMPLES:
Example 1: ABCD is parallelogram. Angle A=70°. Find all angles.
Angle C=70° (opposite). Angle B=Angle D=180-70=110° (supplementary to A).
Example 2: In parallelogram ABCD, diagonals AC and BD meet at O. AO=5cm. Find AC.
AO=OC (diagonals bisect each other). AC=2×AO=10cm.
Example 3: Mid-point theorem — D and E are midpoints of AB and AC. DE=4cm. Find BC.
BC=2×DE=8cm.
COMMON MISTAKES:
Diagonals of parallelogram bisect each other but are NOT equal (unless rectangle).
Diagonals of rectangle are equal but do NOT bisect at 90° (unless square).
Diagonals of rhombus bisect at 90° but are NOT equal (unless square).""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_9", "chapter": "ch8", "difficulty": "intermediate"}),

    Document(page_content="""Class 9 | Ch9: Areas of Parallelograms and Triangles
KEY CONCEPT: Two figures with equal areas are not necessarily congruent.
Two congruent figures always have equal areas.
THEOREMS:
Theorem 1: Parallelograms on same base and between same parallels are equal in area.
Theorem 2: Triangles on same base and between same parallels are equal in area.
Theorem 3: Median divides triangle into two equal area triangles.
Theorem 4: Triangle area = half of parallelogram area if same base and same parallels.
AREA FORMULAS:
Parallelogram = base × height (perpendicular height).
Triangle = (1/2) × base × height.
If parallelogram ABCD and triangle ABE are on same base AB between same parallels:
Area(ABE) = (1/2) × Area(ABCD).
SOLVED EXAMPLES:
Example 1: ABCD is parallelogram. E is point on DC. Show area(ABE)=area(ABD).
Both triangles ABD and ABE have same base AB.
Both between same parallels AB and DC.
Area(ABD)=Area(ABE)=(1/2)Area(ABCD).
Example 2: Parallelogram ABCD and rectangle ABEF on same base AB between same parallels.
Area(ABCD)=Area(ABEF)=AB×h.
Example 3: In triangle PQR, S is midpoint of QR. Area(PQS)=Area(PRS).
PS is median. Median divides triangle into two equal areas.
Example 4: Parallelogram base=8cm, height=5cm. Area=8×5=40cm^2.
Triangle between same base and parallels: area=20cm^2.
COMMON MISTAKES:
Height must be PERPENDICULAR to base.
Two parallelograms on same base with same height have equal area even if they look different.
Median divides area in HALF (not sides in half — it divides opposite side in half).""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_9", "chapter": "ch9", "difficulty": "intermediate"}),

    Document(page_content="""Class 9 | Ch10: Circles
KEY DEFINITIONS:
Circle: set of all points at equal distance (radius) from centre.
Chord: line segment joining any two points on circle.
Diameter: longest chord passing through centre = 2r.
Arc: part of circle. Minor arc < semicircle. Major arc > semicircle.
Sector: region between two radii and arc.
Segment: region between chord and arc.
THEOREMS:
Theorem 1: Equal chords are equidistant from centre (and converse).
Theorem 2: Equal chords subtend equal angles at centre (and converse).
Proof: In triangles OAB and OCD (O=centre, AB=CD):
OA=OC=OB=OD=radius. AB=CD (given). By SSS: triangles congruent. Angle AOB=Angle COD.
Theorem 3: Perpendicular from centre bisects chord (and converse).
Theorem 4: Angle in semicircle is 90°.
Theorem 5: Angles in same segment are equal.
Theorem 6: Angle at centre = double angle at circumference (same arc).
Theorem 7: Opposite angles of cyclic quadrilateral sum to 180°.
SOLVED EXAMPLES:
Example 1: Chord AB=10cm. Distance from centre=12cm. Find radius.
Perpendicular from centre bisects chord. Half chord=5cm.
r^2=12^2+5^2=144+25=169. r=13cm.
Example 2: Angle at centre=120°. Find angle at circumference (same arc).
Angle at circumference=120/2=60°.
Example 3: In cyclic quadrilateral, one angle=75°. Find opposite angle.
Opposite angles sum=180°. Other angle=105°.
COMMON MISTAKES:
Angle at centre = TWICE angle at circumference (not half).
Angle in semicircle=90° (angle subtended by diameter).
Equal chords have equal angles at centre: equal angle does NOT mean equal chord unless same circle.""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_9", "chapter": "ch10", "difficulty": "intermediate"}),

    Document(page_content="""Class 9 | Ch11: Constructions
BASIC CONSTRUCTIONS (Class 6 review):
Perpendicular bisector, angle bisector, 60°, 90°, 45°, 30° using compass.
CLASS 9 CONSTRUCTIONS:
Construction 1: Angle of 60° (without protractor).
Draw ray OA. Arc from O cuts OA at P. Same radius arc from P cuts first arc at Q. Angle QOP=60°.
Construction 2: Bisect any given angle.
Construction 3: Draw perpendicular to given line from given point.
Construction 4: Construct triangle given base, base angle, and sum of other two sides.
Steps: Draw BC (base). Draw angle at B. Mark D on ray such that BD=AB+AC. Join DC. Bisect DC to get perpendicular bisector meeting BD at A. Join AC. Triangle ABC is constructed.
Construction 5: Construct triangle given base, base angle, and DIFFERENCE of other two sides.
Two cases: given side longer or shorter.
Construction 6: Construct triangle given perimeter and two base angles.
Steps: Draw line XY=perimeter. Draw angles at X and Y. Bisect both angles. Bisectors meet at A. Draw perpendicular bisectors of XA and YA to get B and C. Triangle ABC is the required triangle.
Construction 7: Construct right triangle given hypotenuse and one side.
JUSTIFICATION OF CONSTRUCTIONS:
Each construction must be justified by proving why the constructed figure satisfies given conditions.
SOLVED EXAMPLES:
Example 1: Construct triangle with perimeter 11cm and base angles 60° and 45°.
Step 1: Draw XY=11cm.
Step 2: Draw 60° at X, 45° at Y.
Step 3: Bisect these angles. Bisectors meet at A.
Step 4: Perpendicular bisectors of XA and YA meet XY at B and C respectively.
Triangle ABC has perimeter 11cm and base angles 60° and 45°.
COMMON MISTAKES:
Always bisect the BASE angles at X and Y (not the constructed angles).
In construction 4: bisect DC (the line joining end of ray to far end), not the base BC.""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_9", "chapter": "ch11", "difficulty": "intermediate"}),

    Document(page_content="""Class 9 | Ch12: Heron's Formula
HERON'S FORMULA: Area of triangle when all 3 sides are known.
Area = sqrt(s(s-a)(s-b)(s-c))
where a, b, c are the three sides and s = semi-perimeter = (a+b+c)/2.
STEPS:
1. Find s = (a+b+c)/2.
2. Find (s-a), (s-b), (s-c).
3. Multiply: s × (s-a) × (s-b) × (s-c).
4. Take square root.
APPLICATION TO QUADRILATERALS:
Divide quadrilateral into two triangles using diagonal.
Apply Heron's formula to each triangle.
Total area = sum of both triangle areas.
EQUILATERAL TRIANGLE (special case):
All sides = a. s = 3a/2.
Area = sqrt((3a/2)(a/2)(a/2)(a/2)) = (sqrt(3)/4)×a^2.
ISOSCELES TRIANGLE:
If a=b, formula simplifies but Heron's formula still works.
SOLVED EXAMPLES:
Example 1: Sides 13cm, 14cm, 15cm.
s=(13+14+15)/2=42/2=21.
s-a=21-13=8, s-b=21-14=7, s-c=21-15=6.
Area=sqrt(21×8×7×6)=sqrt(7056)=84cm^2.
Example 2: Equilateral triangle side=6cm.
s=9. Area=sqrt(9×3×3×3)=sqrt(243)=9sqrt(3)cm^2.
OR using formula: (sqrt(3)/4)×36=9sqrt(3)cm^2. Same answer.
Example 3: Quadrilateral ABCD. Diagonal AC=10cm. Triangle ABC sides 6,8,10. Triangle ACD sides 10,7,9.
For ABC: s=12. Area=sqrt(12×6×4×2)=sqrt(576)=24cm^2.
For ACD: s=13. Area=sqrt(13×3×6×4)=sqrt(936)=6sqrt(26)cm^2.
Total area=24+6sqrt(26)cm^2.
COMMON MISTAKES:
s is the SEMI-perimeter (half of perimeter), not the full perimeter.
Must check triangle inequality: sum of any two sides > third side.
All three (s-a), (s-b), (s-c) must be positive for valid triangle.""",
    metadata={"source": "ncert", "topic": "mensuration", "class_level": "class_9", "chapter": "ch12", "difficulty": "intermediate"}),

    Document(page_content="""Class 9 | Ch13: Surface Areas and Volumes
SURFACE AREA AND VOLUME FORMULAS:
CUBOID: l=length, b=breadth, h=height.
Total SA=2(lb+bh+lh). Lateral SA=2(l+b)h. Volume=lbh. Diagonal=sqrt(l^2+b^2+h^2).
CUBE: side=a.
Total SA=6a^2. Lateral SA=4a^2. Volume=a^3. Diagonal=a*sqrt(3).
CYLINDER: r=radius, h=height.
Curved SA=2*pi*r*h. Total SA=2*pi*r(r+h). Volume=pi*r^2*h.
CONE: r=base radius, h=vertical height, l=slant height.
l=sqrt(r^2+h^2). Curved SA=pi*r*l. Total SA=pi*r(r+l). Volume=(1/3)*pi*r^2*h.
SPHERE: r=radius.
SA=4*pi*r^2. Volume=(4/3)*pi*r^3.
HEMISPHERE: r=radius.
Curved SA=2*pi*r^2. Total SA=3*pi*r^2. Volume=(2/3)*pi*r^3.
SOLVED EXAMPLES:
Example 1: Cone r=5cm, l=13cm.
h=sqrt(13^2-5^2)=sqrt(144)=12cm.
Curved SA=pi×5×13=65pi=204.1cm^2.
Total SA=pi×5×(5+13)=90pi=282.6cm^2.
Volume=(1/3)×pi×25×12=100pi=314.2cm^3.
Example 2: Sphere r=7cm.
SA=4×(22/7)×49=616cm^2.
Volume=(4/3)×(22/7)×343=1437.3cm^3.
Example 3: Cylinder r=4cm, h=10cm.
Curved SA=2×pi×4×10=80pi=251.2cm^2.
Volume=pi×16×10=160pi=502.4cm^3.
COMMON MISTAKES:
Cone: slant height l=sqrt(r^2+h^2). Given l, find h=sqrt(l^2-r^2).
Hemisphere Total SA=3pi*r^2 (curved 2pi*r^2 + base circle pi*r^2).
Volume of cone=(1/3)×volume of cylinder with same base and height.""",
    metadata={"source": "ncert", "topic": "mensuration", "class_level": "class_9", "chapter": "ch13", "difficulty": "intermediate"}),

    Document(page_content="""Class 9 | Ch14: Statistics
TYPES OF DATA:
Primary data: collected by investigator. Secondary data: from other sources.
Raw data: unorganised. Grouped data: organised in class intervals.
FREQUENCY DISTRIBUTION TABLE:
Class interval: group of values (0-10, 10-20 etc). Class width=upper-lower limit.
Frequency: number of observations in each class.
Class mark (midpoint)=(upper limit+lower limit)/2.
Cumulative frequency: running total of frequencies.
MEAN FOR GROUPED DATA:
Direct method: Mean = sum(f×x)/sum(f) where x=class mark, f=frequency.
Assumed mean method: Mean = a + sum(f×d)/sum(f) where d=x-a, a=assumed mean.
Step deviation method: Mean = a + (sum(f×u)/sum(f))×h where u=(x-a)/h, h=class width.
MEDIAN FOR GROUPED DATA:
Median = L + ((n/2-cf)/f)×h
where L=lower limit of median class, n=total frequency, cf=cumulative frequency before median class, f=frequency of median class, h=class width.
MODE FOR GROUPED DATA:
Mode = L + ((f1-f0)/(2f1-f0-f2))×h
where L=lower limit of modal class, f1=frequency of modal class, f0=previous class frequency, f2=next class frequency, h=class width.
EMPIRICAL RELATIONSHIP: Mode = 3×Median - 2×Mean (approximately).
SOLVED EXAMPLES:
Example 1: Mean by assumed mean. Class marks: 10,20,30,40,50. Frequencies: 4,6,8,5,3. Assumed mean=30.
d values: -20,-10,0,10,20. sum(f×d)=4(-20)+6(-10)+8(0)+5(10)+3(20)=-80-60+0+50+60=-30.
Mean=30+(-30/26)=30-1.15=28.85.
Example 2: Find median class for n=26. n/2=13. Cumulative frequencies: 4,10,18,...
13 falls in third class (cf=10, f=8). Median class is the third class interval.
COMMON MISTAKES:
Class mark is MIDPOINT of class interval, not lower or upper limit.
For median: find n/2 first, then locate which cumulative frequency it falls in.
Modal class has HIGHEST frequency, not highest value.""",
    metadata={"source": "ncert", "topic": "statistics", "class_level": "class_9", "chapter": "ch14", "difficulty": "intermediate"}),

    Document(page_content="""Class 9 | Ch15: Probability
BASIC CONCEPTS:
Experiment: activity with defined set of outcomes. e.g., throwing die, tossing coin.
Sample space: set of ALL possible outcomes. S={H,T} for coin. S={1,2,3,4,5,6} for die.
Event: subset of sample space. Any collection of outcomes.
PROBABILITY FORMULA:
P(E) = Number of favourable outcomes / Total number of outcomes.
Range: 0 <= P(E) <= 1.
P(certain event) = 1. P(impossible event) = 0.
COMPLEMENTARY EVENT:
P(E) + P(not E) = 1. So P(not E) = 1 - P(E).
TYPES OF EVENTS:
Simple event: single outcome. Compound event: more than one outcome.
Mutually exclusive: cannot occur simultaneously. P(A or B)=P(A)+P(B).
EQUALLY LIKELY OUTCOMES: each outcome has same probability of occurring.
STANDARD PROBLEMS:
Die: P(even)=3/6=1/2. P(prime)=3/6=1/2 (2,3,5). P(>4)=2/6=1/3 (5,6).
Coin: P(H)=1/2. Two coins: P(both H)=1/4. P(at least one H)=3/4.
Cards (52): P(ace)=4/52=1/13. P(face card)=12/52=3/13. P(red)=26/52=1/2.
Two dice: Total outcomes=36. P(sum=7): (1,6),(2,5),(3,4),(4,3),(5,2),(6,1)=6/36=1/6.
SOLVED EXAMPLES:
Example 1: Bag has 5 red, 7 blue, 3 green balls. Total=15.
P(red)=5/15=1/3. P(not blue)=(15-7)/15=8/15. P(green or red)=8/15.
Example 2: Two dice thrown. P(sum=8)?
Pairs: (2,6),(3,5),(4,4),(5,3),(6,2)=5 pairs. P=5/36.
Example 3: Cards. P(king or queen)?
Kings=4, Queens=4. Total face cards include these. P(king or queen)=8/52=2/13.
COMMON MISTAKES:
P(E) must be between 0 and 1 inclusive.
For two dice: total outcomes=36 (not 12). Each die independent.
P(not E)=1-P(E), NOT P(E)-1.""",
    metadata={"source": "ncert", "topic": "probability", "class_level": "class_9", "chapter": "ch15", "difficulty": "intermediate"}),

]