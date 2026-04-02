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


    # ── CLASS 10 — All 15 Chapters ──────────────────────────────────

    Document(page_content="""Class 10 | Ch1: Real Numbers
EUCLID'S DIVISION LEMMA:
For any two positive integers a and b, there exist unique integers q and r such that:
a = bq + r where 0 <= r < b.
a=dividend, b=divisor, q=quotient, r=remainder.
EUCLID'S DIVISION ALGORITHM (for HCF):
Step 1: Apply lemma: a=bq+r.
Step 2: If r=0, HCF=b. If r≠0, apply lemma to b and r.
Step 3: Repeat until remainder=0. Last non-zero remainder=HCF.
Example: HCF(96,404). 404=96×4+20. 96=20×4+16. 20=16×1+4. 16=4×4+0. HCF=4.
FUNDAMENTAL THEOREM OF ARITHMETIC:
Every composite number can be expressed as product of primes in UNIQUE way (ignoring order).
Used to find HCF and LCM of large numbers.
HCF = product of SMALLEST powers of common prime factors.
LCM = product of GREATEST powers of all prime factors.
HCF × LCM = product of two numbers (for exactly TWO numbers).
PROVING IRRATIONALITY:
Standard method: assume rational p/q (lowest terms), reach contradiction.
Prove sqrt(3) irrational: assume sqrt(3)=p/q, HCF(p,q)=1.
3=p^2/q^2 → p^2=3q^2 → 3 divides p^2 → 3 divides p → p=3m.
9m^2=3q^2 → q^2=3m^2 → 3 divides q. Both divisible by 3 contradicts HCF=1.
Also: sqrt(2)+sqrt(3), 2-sqrt(5), 1/sqrt(2) are all irrational.
RATIONAL NUMBER DECIMAL EXPANSIONS:
Terminating: denominator (in simplest form) has only 2s and 5s as prime factors.
Non-terminating repeating: denominator has prime factors other than 2 and 5.
17/8=17/2^3: terminating (only 2s). 7/6=7/(2×3): non-terminating repeating (has 3).
SOLVED EXAMPLES:
Example 1: HCF(96,404) by Euclid's algorithm.
404=96×4+20. 96=20×4+16. 20=16×1+4. 16=4×4+0. HCF=4.
LCM=96×404/4=9696.
Example 2: Is 64/455 terminating?
455=5×7×13. Has factors 7 and 13 (not just 2,5). Non-terminating repeating.
COMMON MISTAKES:
HCF×LCM=product of numbers works for EXACTLY TWO numbers only.
For terminating decimal: simplify fraction FIRST then check denominator.""",
    metadata={"source": "ncert", "topic": "numbers", "class_level": "class_10", "chapter": "ch1", "difficulty": "intermediate"}),

    Document(page_content="""Class 10 | Ch2: Polynomials
ZEROES OF POLYNOMIAL:
Zero of polynomial p(x): value of x where p(x)=0.
Geometrically: x-coordinates where graph of y=p(x) crosses x-axis.
Linear polynomial (degree 1): has exactly 1 zero.
Quadratic polynomial (degree 2): has at most 2 zeroes.
Cubic polynomial (degree 3): has at most 3 zeroes.
RELATIONSHIP BETWEEN ZEROES AND COEFFICIENTS:
For quadratic p(x)=ax^2+bx+c with zeroes alpha and beta:
Sum of zeroes: alpha+beta = -b/a.
Product of zeroes: alpha×beta = c/a.
For cubic p(x)=ax^3+bx^2+cx+d with zeroes alpha, beta, gamma:
alpha+beta+gamma = -b/a.
alpha*beta+beta*gamma+gamma*alpha = c/a.
alpha*beta*gamma = -d/a.
FORMING POLYNOMIAL FROM ZEROES:
Quadratic with zeroes alpha, beta: p(x)=k[x^2-(alpha+beta)x+alpha*beta].
DIVISION ALGORITHM FOR POLYNOMIALS:
p(x) = g(x)×q(x) + r(x).
Degree of remainder < degree of divisor.
SOLVED EXAMPLES:
Example 1: Find zeroes of p(x)=6x^2-3-7x=6x^2-7x-3.
6x^2-7x-3=0. Split: 6x^2-9x+2x-3=3x(2x-3)+1(2x-3)=(3x+1)(2x-3).
Zeroes: x=-1/3 and x=3/2.
Verify: sum=-1/3+3/2=(-2+9)/6=7/6=-(-7)/6=b/a. Wait: -b/a=-(-7)/6=7/6. Correct.
Product=(-1/3)(3/2)=-1/2=c/a=-3/6=-1/2. Correct.
Example 2: Form quadratic with zeroes 2 and -3.
Sum=2+(-3)=-1. Product=2×(-3)=-6. p(x)=x^2-(-1)x+(-6)=x^2+x-6.
Example 3: Cubic zeroes 2,-1,-3.
Sum=2-1-3=-2=-b/a → b/a=2. Sum of products=2(-1)+(-1)(-3)+(-3)(2)=-2+3-6=-5=c/a.
Product=2×(-1)×(-3)=6=-d/a → d/a=-6. p(x)=x^3+2x^2-5x-6 (taking a=1).
COMMON MISTAKES:
Sum of zeroes=-b/a (NEGATIVE b over a, not b over a).
Product of zeroes=c/a (positive, not negative).
Zeroes of polynomial: solve p(x)=0 (set equal to zero, NOT to y).""",
    metadata={"source": "ncert", "topic": "algebra", "class_level": "class_10", "chapter": "ch2", "difficulty": "intermediate"}),

    Document(page_content="""Class 10 | Ch3: Pair of Linear Equations in Two Variables
STANDARD FORM: a1x+b1y+c1=0 and a2x+b2y+c2=0.
CONSISTENCY CONDITIONS:
Unique solution (consistent): a1/a2 ≠ b1/b2. Lines intersect.
Infinitely many solutions (consistent, dependent): a1/a2=b1/b2=c1/c2. Lines coincide.
No solution (inconsistent): a1/a2=b1/b2 ≠ c1/c2. Lines parallel.
METHODS OF SOLVING:
Graphical: plot both lines, find intersection point.
Substitution: express one variable in terms of other, substitute.
Elimination: multiply equations to make coefficients equal, add/subtract.
Cross-multiplication: x/((b1c2-b2c1))=y/((c1a2-c2a1))=1/((a1b2-a2b1)).
CROSS MULTIPLICATION FORMULA:
For a1x+b1y+c1=0 and a2x+b2y+c2=0:
x=(b1c2-b2c1)/(a1b2-a2b1), y=(c1a2-c2a1)/(a1b2-a2b1).
SOLVED EXAMPLES:
Example 1: Solve 2x+3y=11 and 2x-4y=-24 by elimination.
Subtract: 7y=35 → y=5. Substitute: 2x+15=11 → x=-2.
Solution: x=-2, y=5.
Example 2: Solve by cross-multiplication: 2x+3y-11=0 and 2x-4y+24=0.
x/(3×24-(-4)×(-11))=y/((-11)×2-24×2)=1/(2×(-4)-2×3).
x/(72-44)=y/(-22-48)=1/(-8-6).
x/28=y/(-70)=1/(-14).
x=28/(-14)=-2. y=-70/(-14)=5. Solution: (-2,5).
Example 3: Check 3x+2y=5 and 6x+4y=10.
a1/a2=3/6=1/2. b1/b2=2/4=1/2. c1/c2=5/10=1/2.
All ratios equal → infinitely many solutions (dependent).
COMMON MISTAKES:
Cross-multiplication: use the formula carefully with correct signs.
Check consistency BEFORE solving — if inconsistent, no solution exists.
Graphical method: use at least 3 points per line to verify.""",
    metadata={"source": "ncert", "topic": "algebra", "class_level": "class_10", "chapter": "ch3", "difficulty": "intermediate"}),

    Document(page_content="""Class 10 | Ch4: Quadratic Equations
STANDARD FORM: ax^2+bx+c=0 where a≠0.
METHODS OF SOLVING:
Method 1 - Factorisation:
Split middle term: find p,q such that p+q=b and p×q=a×c.
2x^2-7x+3=0. a×c=6. p+q=-7, p×q=6. p=-6,q=-1.
2x^2-6x-x+3=0 → 2x(x-3)-1(x-3)=0 → (2x-1)(x-3)=0.
x=1/2 or x=3.
Method 2 - Completing the Square:
ax^2+bx+c=0 → x^2+(b/a)x=-c/a → add (b/2a)^2 both sides.
(x+b/2a)^2=(b^2-4ac)/4a^2 → x=-b/2a ± sqrt(b^2-4ac)/2a.
Method 3 - Quadratic Formula:
x=(-b ± sqrt(b^2-4ac))/2a. (Derived from completing the square.)
DISCRIMINANT D=b^2-4ac:
D>0: two distinct real roots. D=0: two equal real roots (repeated). D<0: no real roots (complex).
NATURE OF ROOTS:
If D is perfect square: roots are rational. If D>0 but not perfect square: roots irrational.
RELATIONSHIP BETWEEN ROOTS:
Sum of roots=alpha+beta=-b/a. Product of roots=alpha×beta=c/a.
WORD PROBLEMS - STANDARD TYPES:
Number problems, age problems, speed-distance problems, area problems.
SOLVED EXAMPLES:
Example 1: 2x^2-7x+3=0 by factorisation.
a×c=6. Factors of 6 summing to -7: -6 and -1.
2x^2-6x-x+3=2x(x-3)-1(x-3)=(2x-1)(x-3)=0.
x=1/2 or x=3.
Example 2: Find nature of roots of 2x^2-6x+3=0.
D=36-24=12>0. Two distinct real roots (D not perfect square, so irrational).
Example 3: Sum of ages of father and son is 45. Five years ago product was 124.
Let son's age=x. Father's age=45-x.
(x-5)(45-x-5)=124 → (x-5)(40-x)=124.
40x-x^2-200+5x=124 → x^2-45x+324=0 → (x-9)(x-36)=0.
x=9 (son) or x=36 (check: son can't be 36 if sum is 45). Son=9, Father=36.
COMMON MISTAKES:
Discriminant: D=b^2-4ac NOT b^2+4ac.
If D=0: ONE repeated root (two equal roots, not no roots).
Quadratic formula: entire (-b±sqrt(D)) is over 2a.""",
    metadata={"source": "ncert", "topic": "algebra", "class_level": "class_10", "chapter": "ch4", "difficulty": "intermediate"}),

    Document(page_content="""Class 10 | Ch5: Arithmetic Progressions
ARITHMETIC PROGRESSION (AP): sequence where difference between consecutive terms is constant.
Common difference d=a2-a1=a3-a2=... (can be positive, negative, or zero).
General form: a, a+d, a+2d, a+3d, ...
nth TERM FORMULA: a_n = a + (n-1)d where a=first term, d=common difference.
SUM OF FIRST n TERMS:
S_n = n/2 × [2a + (n-1)d] = n/2 × [a + l] where l=last term=a_n.
FINDING NUMBER OF TERMS: use a_n=a+(n-1)d, solve for n.
PROPERTIES:
If a,b,c are in AP: b-a=c-b → 2b=a+c → b=(a+c)/2 (b is arithmetic mean).
Sum of AP from both ends: a1+a_n=a2+a_(n-1)=... (equidistant terms have equal sum).
THREE NUMBERS IN AP: take as a-d, a, a+d (sum=3a, simplifies problems).
FOUR NUMBERS IN AP: take as a-3d, a-d, a+d, a+3d.
SOLVED EXAMPLES:
Example 1: Sum of first 40 positive integers divisible by 6.
AP: 6,12,18,...,240. a=6, d=6, n=40.
S_40=40/2×[2(6)+(40-1)(6)]=20×[12+234]=20×246=4920.
Example 2: 7th term=34, 13th term=64. Find AP and S_20.
a+6d=34 ...(i). a+12d=64 ...(ii).
(ii)-(i): 6d=30 → d=5. From (i): a=34-30=4.
AP: 4,9,14,19,...
S_20=20/2×[2(4)+19(5)]=10×[8+95]=10×103=1030.
Example 3: How many terms of AP 3,5,7,... give sum 120?
S_n=n/2×[2(3)+(n-1)(2)]=n/2×[4n+2]=n(2n+1)... Wait: n/2[6+2n-2]=n/2[2n+4]=n(n+2)=120.
n^2+2n-120=0. (n+12)(n-10)=0. n=10.
COMMON MISTAKES:
nth term formula: a_n=a+(n-1)d NOT a+(n)d.
In sum formula S_n=n/2[2a+(n-1)d], the n inside brackets is (n-1) not n.
d can be negative (decreasing AP) or zero (constant sequence).""",
    metadata={"source": "ncert", "topic": "algebra", "class_level": "class_10", "chapter": "ch5", "difficulty": "intermediate"}),

    Document(page_content="""Class 10 | Ch6: Triangles (Similarity)
SIMILAR TRIANGLES: same shape, different size. Corresponding angles equal, corresponding sides proportional.
Symbol: triangle ABC ~ triangle DEF.
BASIC PROPORTIONALITY THEOREM (BPT / Thales Theorem):
If a line is drawn parallel to one side of triangle, it divides the other two sides proportionally.
If DE || BC in triangle ABC: AD/DB = AE/EC.
CONVERSE: If a line divides two sides of triangle proportionally, it is parallel to third side.
CRITERIA FOR SIMILARITY:
AAA (AA): Two angles equal → triangles similar.
SSS: All three sides proportional → triangles similar.
SAS: Two sides proportional and included angle equal → triangles similar.
AREAS OF SIMILAR TRIANGLES:
Ratio of areas = Square of ratio of corresponding sides.
If triangle ABC ~ triangle DEF: Area(ABC)/Area(DEF) = (AB/DE)^2 = (BC/EF)^2 = (CA/FD)^2.
PYTHAGORAS THEOREM:
In right triangle, square of hypotenuse = sum of squares of other two sides.
c^2=a^2+b^2. Proof using similar triangles (altitude on hypotenuse).
CONVERSE: If c^2=a^2+b^2, angle opposite c is 90°.
SOLVED EXAMPLES:
Example 1: In triangle ABC, DE||BC. AD=2cm, DB=3cm, AE=4cm. Find EC.
By BPT: AD/DB=AE/EC → 2/3=4/EC → EC=6cm.
Example 2: Triangle ABC ~ triangle DEF. AB=4,BC=5,CA=6. DE=8. Find EF and FD.
Ratio AB/DE=4/8=1/2. So all sides doubled.
EF=2×BC=10. FD=2×CA=12.
Example 3: Areas of two similar triangles are 25cm^2 and 100cm^2. If base of smaller=3cm, find base of larger.
Area ratio=25/100=1/4=(side ratio)^2. Side ratio=1/2. Larger base=2×3=6cm.
COMMON MISTAKES:
BPT: line must be PARALLEL to one side (not just any line).
Area ratio=(side ratio)^2 NOT side ratio directly.
AA criterion: only need 2 angles equal (third is automatic since sum=180°).""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_10", "chapter": "ch6", "difficulty": "intermediate"}),

    Document(page_content="""Class 10 | Ch7: Coordinate Geometry
DISTANCE FORMULA:
Distance between P(x1,y1) and Q(x2,y2) = sqrt((x2-x1)^2+(y2-y1)^2).
Distance from origin: OP=sqrt(x^2+y^2).
SECTION FORMULA:
Point P dividing AB (A(x1,y1), B(x2,y2)) in ratio m:n INTERNALLY:
P = ((mx2+nx1)/(m+n), (my2+ny1)/(m+n)).
MIDPOINT FORMULA (m=n=1):
M = ((x1+x2)/2, (y1+y2)/2).
EXTERNAL DIVISION:
P = ((mx2-nx1)/(m-n), (my2-ny1)/(m-n)).
AREA OF TRIANGLE:
Given A(x1,y1), B(x2,y2), C(x3,y3):
Area = (1/2)|x1(y2-y3)+x2(y3-y1)+x3(y1-y2)|.
If area=0, points are COLLINEAR.
CENTROID OF TRIANGLE:
G = ((x1+x2+x3)/3, (y1+y2+y3)/3). Divides each median in 2:1.
SOLVED EXAMPLES:
Example 1: Distance between A(2,3) and B(-1,0).
AB=sqrt((-1-2)^2+(0-3)^2)=sqrt(9+9)=sqrt(18)=3sqrt(2).
Example 2: Find point dividing (1,3) and (4,6) in ratio 2:1 internally.
P=((2×4+1×1)/(2+1),(2×6+1×3)/(2+1))=(9/3,15/3)=(3,5).
Example 3: Area of triangle A(2,3), B(-1,0), C(2,-4).
Area=(1/2)|2(0-(-4))+(-1)((-4)-3)+2(3-0)|=(1/2)|8+7+6|=(1/2)(21)=10.5 sq units.
Example 4: Show A(1,2), B(3,4), C(5,6) are collinear.
Area=(1/2)|1(4-6)+3(6-2)+5(2-4)|=(1/2)|(-2)+12+(-10)|=(1/2)(0)=0. Collinear.
COMMON MISTAKES:
Section formula: m corresponds to the second point B, n to first point A.
Area formula: use ABSOLUTE VALUE (modulus bars) — area cannot be negative.
Midpoint: average of BOTH x-coordinates and BOTH y-coordinates separately.""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_10", "chapter": "ch7", "difficulty": "intermediate"}),

    Document(page_content="""Class 10 | Ch8: Introduction to Trigonometry
TRIGONOMETRIC RATIOS (right triangle, angle theta):
sin(theta)=opposite/hypotenuse=P/H.
cos(theta)=adjacent/hypotenuse=B/H.
tan(theta)=opposite/adjacent=P/B=sin/cos.
cosec(theta)=1/sin=H/P. sec(theta)=1/cos=H/B. cot(theta)=1/tan=B/P.
STANDARD VALUES TABLE:
Angle:      0°    30°      45°       60°       90°
sin:        0     1/2      1/sqrt2   sqrt3/2   1
cos:        1     sqrt3/2  1/sqrt2   1/2       0
tan:        0     1/sqrt3  1         sqrt3     undefined
cosec:      undef 2        sqrt2     2/sqrt3   1
sec:        1     2/sqrt3  sqrt2     2         undef
cot:        undef sqrt3    1         1/sqrt3   0
TRIGONOMETRIC IDENTITIES:
sin^2(theta)+cos^2(theta)=1.
1+tan^2(theta)=sec^2(theta).
1+cot^2(theta)=cosec^2(theta).
COMPLEMENTARY ANGLES:
sin(90-A)=cos(A). cos(90-A)=sin(A). tan(90-A)=cot(A).
cosec(90-A)=sec(A). sec(90-A)=cosec(A). cot(90-A)=tan(A).
SOLVED EXAMPLES:
Example 1: If sin(theta)=3/5, find all trig ratios.
P=3, H=5, B=sqrt(25-9)=4.
cos=4/5, tan=3/4, cosec=5/3, sec=5/4, cot=4/3.
Example 2: Prove (sin^2(theta)/cos(theta)) + cos(theta) = sec(theta).
LHS=sin^2/cos+cos=(sin^2+cos^2)/cos=1/cos=sec. Proved.
Example 3: Evaluate 2tan^2(45°)+cos^2(30°)-sin^2(60°).
=2(1)^2+(sqrt3/2)^2-(sqrt3/2)^2=2+3/4-3/4=2.
Example 4: sin(theta)=cos(theta). Find theta.
tan(theta)=1. theta=45°.
COMMON MISTAKES:
sin^2+cos^2=1 (NOT sin+cos=1).
Values at 90°: sin=1, cos=0, tan=undefined (NOT 0).
Memorise table using: "Some People Have Curly Brown Hair Through Proper Brushing".""",
    metadata={"source": "ncert", "topic": "trigonometry", "class_level": "class_10", "chapter": "ch8", "difficulty": "intermediate"}),

    Document(page_content="""Class 10 | Ch9: Applications of Trigonometry (Heights and Distances)
KEY TERMS:
Angle of elevation: angle formed above horizontal when looking UP at an object.
Angle of depression: angle formed below horizontal when looking DOWN at an object.
Observer, object, horizontal line form a right triangle.
Line of sight: line from eye to object.
Note: Angle of elevation from A to B = Angle of depression from B to A (alternate interior angles).
STANDARD SETUP:
Draw a clear diagram. Identify right triangles. Assign variables.
Use appropriate trig ratio: tan for height/distance, sin/cos if hypotenuse involved.
STANDARD PROBLEM TYPES:
Type 1: Height of tower/building given angle of elevation and distance.
Type 2: Distance of boat/object given angle of depression from top.
Type 3: Two angles from same point (form two equations).
Type 4: Two observers at different points (system of equations).
USEFUL: tan(30°)=1/sqrt3, tan(45°)=1, tan(60°)=sqrt3.
SOLVED EXAMPLES:
Example 1: Tower 75m high. From base, angles of depression of two boats=30° and 45°.
Let boat A (30°) distance=x, boat B (45°) distance=y.
tan(30°)=75/x → x=75sqrt(3). tan(45°)=75/y → y=75.
Distance between boats=x-y=75sqrt(3)-75=75(sqrt3-1)=75(1.732-1)=54.9m.
Example 2: Boy 1.2m tall stands 30m from tower. Elevation angle=60°. Find tower height.
tan(60°)=(h-1.2)/30 → sqrt3=h-1.2)/30 → h=30sqrt3+1.2=51.96+1.2=53.16m.
Example 3: Kite string 150m, angle=60°. Find height of kite.
sin(60°)=h/150 → h=150×sqrt3/2=75sqrt3 metres.
COMMON MISTAKES:
Angle of depression = angle of elevation (they are alternate interior angles, not supplementary).
Height of observer must be considered in many problems.
Always draw diagram first — most errors come from not visualising correctly.""",
    metadata={"source": "ncert", "topic": "trigonometry", "class_level": "class_10", "chapter": "ch9", "difficulty": "intermediate"}),

    Document(page_content="""Class 10 | Ch10: Circles
KEY DEFINITIONS:
Tangent: line touching circle at exactly ONE point (point of tangency/contact).
Secant: line intersecting circle at TWO points.
A tangent is perpendicular to radius at point of contact.
THEOREMS:
Theorem 1: Tangent at any point of circle is perpendicular to radius through that point.
Proof: Any point on tangent other than contact point is outside circle (farther from centre).
So perpendicular from centre to tangent = shortest distance = radius. Hence radius ⊥ tangent.
Theorem 2: Lengths of tangents drawn from external point are EQUAL.
If PA and PB are tangents from P to circle with centre O:
In triangles OAP and OBP: OA=OB (radii), OP=OP (common), angle OAP=angle OBP=90°.
By RHS: triangles congruent → PA=PB (CPCT).
Also: OP bisects angle APB and angle AOB.
LENGTH OF TANGENT FROM EXTERNAL POINT:
If d=distance from external point to centre, r=radius:
Length of tangent=sqrt(d^2-r^2).
ANGLE IN ALTERNATE SEGMENT (Tangent-Chord angle):
Angle between tangent and chord = inscribed angle in alternate segment.
SOLVED EXAMPLES:
Example 1: Point P is 17cm from centre. Radius=8cm. Find tangent length.
Tangent=sqrt(17^2-8^2)=sqrt(289-64)=sqrt(225)=15cm.
Example 2: Two tangents PA=PB from external point P. PA=12cm, OA=5cm. Find OP.
OP^2=OA^2+PA^2=25+144=169. OP=13cm.
Example 3: Tangents from P touch circle at A and B. Angle APB=60°. Find angle AOB.
Since PA=PB, triangle PAB is isosceles. Angle OAP=90°.
In quadrilateral OAPB: angle AOB+angle OBP+angle APB+angle OAP=360°.
angle AOB+90°+60°+90°=360° → angle AOB=120°.
COMMON MISTAKES:
Tangent from EXTERNAL point has equal length — this fails for internal points.
Tangent ⊥ radius at POINT OF CONTACT (not at every point of tangent).
Length of tangent uses Pythagoras: sqrt(d^2-r^2), not d-r.""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_10", "chapter": "ch10", "difficulty": "intermediate"}),

    Document(page_content="""Class 10 | Ch11: Constructions
CONSTRUCTION 1: DIVIDE LINE SEGMENT IN GIVEN RATIO (m:n)
To divide AB in ratio 3:2:
Step 1: Draw ray AX at acute angle to AB.
Step 2: Mark 3+2=5 equal arcs on AX: A1,A2,A3,A4,A5.
Step 3: Join A5 to B.
Step 4: Draw line through A3 parallel to A5B (using corresponding angles).
Step 5: This line meets AB at P. AP:PB=3:2.
CONSTRUCTION 2: CONSTRUCT SIMILAR TRIANGLE (scale factor m/n)
To construct triangle similar to ABC with scale factor 3/4:
Case 1 (scale factor < 1, smaller triangle):
Step 1: Draw ray BX at acute angle to BC.
Step 2: Mark 4 equal points on BX: B1,B2,B3,B4.
Step 3: Join B4 to C. Draw B3C' parallel to B4C.
Step 4: Draw C'A' parallel to CA. Triangle A'BC' is required (3/4 times original).
Case 2 (scale factor > 1, larger triangle):
Mark more points (m points), join nth point to vertex.
CONSTRUCTION 3: TANGENTS FROM EXTERNAL POINT
To draw tangents from point P to circle with centre O:
Step 1: Find midpoint M of OP.
Step 2: Draw circle with centre M and radius MP(=MO).
Step 3: This circle intersects original circle at A and B.
Step 4: PA and PB are the required tangents.
Why: Angle OAP=90° (angle in semicircle on diameter OP).
CONSTRUCTION 4: TANGENT AT POINT ON CIRCLE
Draw radius to point. Tangent is perpendicular to radius at that point.
SOLVED EXAMPLES:
Example 1: Divide 7cm segment in ratio 3:2.
Draw 5 equal arcs. Join 5th to B. Through 3rd draw parallel. Done.
Example 2: Tangents from point 10cm from centre, radius 4cm.
Tangent length=sqrt(100-16)=sqrt(84)=2sqrt(21)≈9.17cm.
COMMON MISTAKES:
Scale factor 3/4: mark 4 points (denominator), use 3rd (numerator) for the construction.
Tangent construction: the second circle must have DIAMETER = OP (radius = OP/2).""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_10", "chapter": "ch11", "difficulty": "intermediate"}),

    Document(page_content="""Class 10 | Ch12: Areas Related to Circles
BASIC FORMULAS (r=radius):
Circumference=2*pi*r. Area of circle=pi*r^2.
ARC LENGTH AND SECTOR:
Arc length = (theta/360)×2*pi*r.
Area of sector = (theta/360)×pi*r^2.
Perimeter of sector = 2r + arc length = 2r + (theta/360)×2*pi*r.
SEGMENT:
Area of minor segment = Area of sector - Area of triangle.
Area of triangle in sector = (1/2)×r^2×sin(theta).
Area of minor segment = (theta/360)×pi*r^2 - (1/2)×r^2×sin(theta).
Area of major segment = Area of circle - Area of minor segment.
COMBINATIONS OF FIGURES:
Shaded regions often require adding or subtracting areas of different shapes.
SOLVED EXAMPLES:
Example 1: Sector r=14cm, theta=60°.
Arc length=(60/360)×2×(22/7)×14=(1/6)×88=14.67cm.
Area=(60/360)×(22/7)×196=(1/6)×616=102.67cm^2.
Example 2: Area of minor segment, r=12cm, theta=60°.
Sector area=(60/360)×pi×144=24pi cm^2.
Triangle area=(1/2)×12^2×sin60°=72×(sqrt3/2)=36sqrt3 cm^2.
Segment area=24pi-36sqrt3=(24×3.14)-(36×1.732)=75.36-62.35=13.01cm^2.
Example 3: Square inscribed in circle r=10cm. Area of shaded region outside square.
Diagonal of square=2r=20cm. Side=20/sqrt2=10sqrt2.
Area of square=200cm^2. Area of circle=pi×100=314cm^2.
Shaded area=314-200=114cm^2.
COMMON MISTAKES:
theta in formula must be in DEGREES not radians.
Area of sector=(theta/360)×pi*r^2 NOT (theta/360)×2*pi*r (that is arc length).
For segment: SUBTRACT triangle from sector (segment < sector always).""",
    metadata={"source": "ncert", "topic": "mensuration", "class_level": "class_10", "chapter": "ch12", "difficulty": "intermediate"}),

    Document(page_content="""Class 10 | Ch13: Surface Areas and Volumes
SURFACE AREA AND VOLUME FORMULAS (same as Class 9 plus combinations):
Cone: CSA=pi*r*l, TSA=pi*r(r+l), V=(1/3)*pi*r^2*h, l=sqrt(r^2+h^2).
Cylinder: CSA=2*pi*r*h, TSA=2*pi*r(r+h), V=pi*r^2*h.
Sphere: SA=4*pi*r^2, V=(4/3)*pi*r^3.
Hemisphere: CSA=2*pi*r^2, TSA=3*pi*r^2, V=(2/3)*pi*r^3.
COMBINATION OF SOLIDS:
Total surface area of combination: add all EXPOSED surfaces only (not hidden surfaces).
Volume of combination: simply add volumes.
CONVERSION OF SOLIDS:
When one solid melted and recast into another: VOLUME remains same.
Number of smaller solids = Volume of larger solid / Volume of one smaller solid.
FRUSTUM OF CONE (cone with top cut off):
Slant height: l=sqrt(h^2+(r1-r2)^2) where r1=bottom radius, r2=top radius, h=height.
CSA=pi×l×(r1+r2). TSA=pi×[l(r1+r2)+r1^2+r2^2]. V=(1/3)×pi×h×(r1^2+r2^2+r1×r2).
SOLVED EXAMPLES:
Example 1: Cone on hemisphere, both r=3.5cm, cone h=4cm. Find TSA and V.
Cone: l=sqrt(16+12.25)=sqrt(28.25)=5.31cm. CSA=pi×3.5×5.31=58.4cm^2.
Hemisphere CSA=2×pi×3.5^2=77cm^2. Total SA=58.4+77=135.4cm^2 (base circle is hidden).
Cone V=(1/3)×pi×12.25×4=51.3cm^3. Hemisphere V=(2/3)×pi×42.875=89.8cm^3.
Total V=141.1cm^3.
Example 2: Sphere r=9cm melted into cylinders r=3cm, h=9cm. How many?
V_sphere=(4/3)×pi×729=972pi. V_cylinder=pi×9×9=81pi.
Number=972pi/81pi=12 cylinders.
Example 3: Bucket (frustum): top r=20cm, bottom r=8cm, h=16cm.
l=sqrt(256+144)=sqrt(400)=20cm.
V=(pi/3)×16×(400+64+160)=(pi/3)×16×624=10449cm^3 approx.
COMMON MISTAKES:
TSA of combination: DO NOT add hidden surfaces.
Conversion: volume is conserved (not SA).
Frustum l uses (r1-r2) not (r1+r2).""",
    metadata={"source": "ncert", "topic": "mensuration", "class_level": "class_10", "chapter": "ch13", "difficulty": "intermediate"}),

    Document(page_content="""Class 10 | Ch14: Statistics
MEAN FOR GROUPED DATA:
Direct method: x_bar = sum(f*x)/sum(f). x=class mark=(upper+lower)/2.
Assumed mean method: x_bar = a + sum(f*d)/sum(f). d=x-a.
Step deviation method: x_bar = a + (sum(f*u)/sum(f))×h. u=(x-a)/h. Best when h is constant.
MEDIAN FOR GROUPED DATA:
Formula: M = L + ((n/2 - cf)/f) × h.
L=lower boundary of median class.
n=total frequency. cf=cumulative frequency of class BEFORE median class.
f=frequency of median class. h=class width.
Median class: class where cumulative frequency first exceeds n/2.
MODE FOR GROUPED DATA:
Modal class=class with highest frequency.
Mode = L + ((f1-f0)/(2f1-f0-f2)) × h.
L=lower boundary of modal class. f1=frequency of modal class.
f0=frequency of class BEFORE modal class. f2=frequency of class AFTER modal class.
EMPIRICAL RELATIONSHIP: Mode = 3×Median - 2×Mean (approximately true).
OGIVE (CUMULATIVE FREQUENCY CURVE):
Less than ogive: plot (upper class boundary, cumulative frequency).
More than ogive: plot (lower class boundary, more than cumulative frequency).
Median from ogive: find n/2 on y-axis, draw horizontal to curve, then vertical to x-axis.
SOLVED EXAMPLES:
Example 1: Mean by step deviation. Classes 10-20,20-30,...50-60. Frequencies 4,6,8,5,3. a=30, h=10.
Class marks: 15,25,35,45,55. u=(-2,-1,0,1,2). f×u=-8,-6,0,5,6.
sum(f)=26. sum(f×u)=-3. Mean=30+(-3/26)×10=30-1.15=28.85.
Example 2: Find median. n=26, n/2=13. cf values: 4,10,18,23,26. 13 falls in class 30-40 (cf=10, f=8).
Median=30+((13-10)/8)×10=30+3.75=33.75.
COMMON MISTAKES:
For median formula: cf is cumulative frequency of class BEFORE (not including) median class.
Class mark is MIDPOINT: for class 10-20, mark=15 (not 10 or 20).
Modal class: highest frequency (not highest class mark).""",
    metadata={"source": "ncert", "topic": "statistics", "class_level": "class_10", "chapter": "ch14", "difficulty": "intermediate"}),

    Document(page_content="""Class 10 | Ch15: Probability
CLASSICAL DEFINITION:
P(E) = Number of favourable outcomes / Total number of equally likely outcomes.
Range: 0 <= P(E) <= 1. P(E)+P(not E)=1.
P(certain event)=1. P(impossible event)=0.
SAMPLE SPACES:
One coin: S={H,T}, n(S)=2.
Two coins: S={HH,HT,TH,TT}, n(S)=4.
One die: S={1,2,3,4,5,6}, n(S)=6.
Two dice: n(S)=36 (all ordered pairs).
Deck of cards: n(S)=52. (4 suits × 13 cards each. Face cards=12. Aces=4.)
CARD PROBLEMS:
Red cards=26 (hearts+diamonds). Black=26 (clubs+spades).
Face cards=12 (J,Q,K of each suit). Aces=4.
King of red=2. Face card AND red=6.
TWO DICE PROBLEMS:
Sum=2: (1,1)=1 way. Sum=3: 2 ways. Sum=7: 6 ways (most common).
Sum=12: (6,6)=1 way.
P(sum=7)=6/36=1/6. P(sum=2 or 12)=2/36=1/18.
SOLVED EXAMPLES:
Example 1: Two dice. P(sum=8).
Pairs: (2,6),(3,5),(4,4),(5,3),(6,2)=5. P=5/36.
Example 2: Cards. P(king or red).
P(king)=4/52. P(red)=26/52. P(king AND red)=2/52.
P(king or red)=4/52+26/52-2/52=28/52=7/13.
Example 3: Bag: 5 red, 3 blue, 2 green. P(not red)?
P(not red)=(3+2)/10=5/10=1/2.
Example 4: Two dice. P(same number on both).
Pairs: (1,1),(2,2),(3,3),(4,4),(5,5),(6,6)=6. P=6/36=1/6.
COMMON MISTAKES:
Two coins: 3 outcomes (0H,1H,2H) are NOT equally likely. Use 4 outcomes (HH,HT,TH,TT).
P(A or B) = P(A)+P(B)-P(A and B). Don't forget the intersection.
For two dice: total outcomes=36 not 12 (order matters: (1,2)≠(2,1)).""",
    metadata={"source": "ncert", "topic": "probability", "class_level": "class_10", "chapter": "ch15", "difficulty": "intermediate"}),


    # ── CLASS 11 — All 16 Chapters ──────────────────────────────────

    Document(page_content="""Class 11 | Ch1: Sets
SET: well-defined collection of distinct objects.
Representation: Roster (list) {1,2,3} or Set-builder {x: condition}.
TYPES OF SETS:
Empty/Null set: no elements. phi or {}.
Singleton: exactly one element.
Finite set: countable elements. Infinite set: uncountable.
Universal set U: contains all elements under consideration.
Subset: A is subset of B if every element of A is in B. A⊆B.
Proper subset: A⊂B means A⊆B and A≠B.
Power set P(A): set of ALL subsets of A. If n(A)=k, then n(P(A))=2^k.
SET OPERATIONS:
Union A∪B: elements in A OR B (or both).
Intersection A∩B: elements in BOTH A and B.
Difference A-B: elements in A but NOT in B.
Complement A': elements in U but NOT in A. A'=U-A.
Symmetric difference A△B = (A-B)∪(B-A).
LAWS (De Morgan's):
(A∪B)'=A'∩B'. (A∩B)'=A'∪B'.
VENN DIAGRAMS: circles inside rectangle (universal set).
CARDINAL NUMBER FORMULA:
n(A∪B)=n(A)+n(B)-n(A∩B).
n(A∪B∪C)=n(A)+n(B)+n(C)-n(A∩B)-n(B∩C)-n(A∩C)+n(A∩B∩C).
SOLVED EXAMPLES:
Example 1: A={1,2,3,4,5}, B={2,4,6,8}.
A∪B={1,2,3,4,5,6,8}. A∩B={2,4}. A-B={1,3,5}. B-A={6,8}.
n(A∪B)=5+4-2=7. Verified: 7 elements in A∪B.
Example 2: n(A)=20, n(B)=25, n(A∪B)=40. Find n(A∩B).
n(A∩B)=20+25-40=5.
Example 3: P({a,b})={{},{a},{b},{a,b}}. n=4=2^2.
COMMON MISTAKES:
{0} and {} are DIFFERENT. {0} has one element (zero). {} is empty.
Empty set {} is subset of EVERY set.
A⊆A always (every set is subset of itself).""",
    metadata={"source": "ncert", "topic": "sets", "class_level": "class_11", "chapter": "ch1", "difficulty": "intermediate"}),

    Document(page_content="""Class 11 | Ch2: Relations and Functions
CARTESIAN PRODUCT: A×B = {(a,b): a∈A, b∈B}.
n(A×B)=n(A)×n(B). A×B≠B×A (unless A=B).
RELATION: any subset of A×B. Domain=set of first elements. Range=set of second elements.
FUNCTION: relation where every element of domain has EXACTLY ONE image.
One-one (injective): different inputs → different outputs. f(a)=f(b) → a=b.
Onto (surjective): every element of codomain has a pre-image.
Bijective: both one-one AND onto. Inverse exists iff bijective.
DOMAIN AND RANGE:
For f(x)=sqrt(9-x^2): need 9-x^2>=0 → x^2<=9 → -3<=x<=3. Domain=[-3,3]. Range=[0,3].
For f(x)=1/(x-2): need x≠2. Domain=R-{2}.
For f(x)=sqrt(x-1)+sqrt(5-x): need x>=1 AND x<=5. Domain=[1,5].
COMPOSITION OF FUNCTIONS:
(fog)(x)=f(g(x)). Apply g first, then f.
(gof)(x)=g(f(x)). Apply f first, then g.
fog≠gof in general.
INVERSE FUNCTION:
f^(-1) exists iff f is bijective.
If f(x)=y then f^(-1)(y)=x.
To find: replace f(x) with y, solve for x, then replace x with f^(-1)(y).
SOLVED EXAMPLES:
Example 1: f(x)=2x+1, g(x)=x^2-1.
fog(x)=f(g(x))=f(x^2-1)=2(x^2-1)+1=2x^2-1.
gof(x)=g(f(x))=g(2x+1)=(2x+1)^2-1=4x^2+4x.
Example 2: Domain of f(x)=sqrt(9-x^2).
9-x^2>=0 → (3-x)(3+x)>=0 → -3<=x<=3. Domain=[-3,3].
Example 3: Is f(x)=2x+3 bijective? Find inverse.
One-one: f(a)=f(b) → 2a+3=2b+3 → a=b. Yes.
Onto: for any y, x=(y-3)/2 exists. Yes. Bijective.
Inverse: y=2x+3 → x=(y-3)/2. So f^(-1)(x)=(x-3)/2.
COMMON MISTAKES:
Domain: find values where function is DEFINED (not where it equals zero).
fog means f applied AFTER g (right to left). fog(x)=f(g(x)).
Every function is a relation but NOT every relation is a function.""",
    metadata={"source": "ncert", "topic": "functions", "class_level": "class_11", "chapter": "ch2", "difficulty": "intermediate"}),

    Document(page_content="""Class 11 | Ch3: Trigonometric Functions
RADIAN MEASURE: pi radians=180°. 1 radian=180°/pi≈57.3°.
Arc length l=r×theta (theta in radians). Area of sector=(1/2)r^2×theta.
SIGN OF TRIG FUNCTIONS BY QUADRANT (ASTC rule: All Students Take Calculus):
Q1: all positive. Q2: sin,cosec positive. Q3: tan,cot positive. Q4: cos,sec positive.
TRIG VALUES FOR STANDARD ANGLES: (same as Class 10 table).
TRIG FUNCTIONS OF ALLIED ANGLES:
sin(pi-x)=sin(x). cos(pi-x)=-cos(x). tan(pi-x)=-tan(x).
sin(pi+x)=-sin(x). cos(pi+x)=-cos(x). tan(pi+x)=tan(x).
sin(2pi-x)=-sin(x). cos(2pi-x)=cos(x).
sin(-x)=-sin(x) (odd). cos(-x)=cos(x) (even).
SUM AND DIFFERENCE FORMULAS:
sin(A+B)=sinA cosB+cosA sinB. sin(A-B)=sinA cosB-cosA sinB.
cos(A+B)=cosA cosB-sinA sinB. cos(A-B)=cosA cosB+sinA sinB.
tan(A+B)=(tanA+tanB)/(1-tanA tanB). tan(A-B)=(tanA-tanB)/(1+tanA tanB).
DOUBLE ANGLE FORMULAS:
sin2A=2sinA cosA. cos2A=cos^2A-sin^2A=1-2sin^2A=2cos^2A-1.
tan2A=2tanA/(1-tan^2A).
HALF ANGLE: sin^2(A/2)=(1-cosA)/2. cos^2(A/2)=(1+cosA)/2.
PRODUCT TO SUM:
sinA cosB=(1/2)[sin(A+B)+sin(A-B)].
cosA cosB=(1/2)[cos(A+B)+cos(A-B)].
GENERAL SOLUTION:
sinx=sina → x=n*pi+(-1)^n*a. cosx=cosa → x=2n*pi±a. tanx=tana → x=n*pi+a.
SOLVED EXAMPLES:
Example 1: Prove sin(A+B)sin(A-B)=sin^2A-sin^2B.
LHS=(sinA cosB+cosA sinB)(sinA cosB-cosA sinB)=sin^2A cos^2B-cos^2A sin^2B.
=sin^2A(1-sin^2B)-(1-sin^2A)sin^2B=sin^2A-sin^2A sin^2B-sin^2B+sin^2A sin^2B=sin^2A-sin^2B. Proved.
Example 2: Solve 2cos^2x-3cosx+1=0 for x in [0,2pi].
Let c=cosx: 2c^2-3c+1=0 → (2c-1)(c-1)=0 → c=1/2 or c=1.
cosx=1/2 → x=pi/3 or 5pi/3. cosx=1 → x=0. Solutions: {0, pi/3, 5pi/3}.
COMMON MISTAKES:
sinx=sin(a) general solution: x=n*pi+(-1)^n*a (alternating sign, NOT just ±a).
sin(A+B)≠sinA+sinB. Must use the formula.""",
    metadata={"source": "ncert", "topic": "trigonometry", "class_level": "class_11", "chapter": "ch3", "difficulty": "intermediate"}),

    Document(page_content="""Class 11 | Ch4: Principle of Mathematical Induction
PMI METHOD:
Step 1 (Base case): Verify statement P(n) is true for n=1 (or starting value).
Step 2 (Inductive step): Assume P(k) is true. Prove P(k+1) is true.
Conclusion: By PMI, P(n) is true for all n>=1.
KEY: The inductive step uses P(k) (called inductive hypothesis) to prove P(k+1).
STANDARD RESULTS TO PROVE:
Sum of natural numbers: 1+2+3+...+n=n(n+1)/2.
Sum of squares: 1^2+2^2+...+n^2=n(n+1)(2n+1)/6.
Sum of cubes: 1^3+2^3+...+n^3=[n(n+1)/2]^2.
Geometric sum: a+ar+ar^2+...+ar^(n-1)=a(r^n-1)/(r-1).
SOLVED EXAMPLES:
Example 1: Prove 1+2+3+...+n=n(n+1)/2 by PMI.
Base: n=1. LHS=1. RHS=1(2)/2=1. True.
Assume true for n=k: 1+2+...+k=k(k+1)/2.
Prove for n=k+1: 1+2+...+k+(k+1)=k(k+1)/2+(k+1)=(k+1)(k/2+1)=(k+1)(k+2)/2.
This is (k+1)(k+2)/2 which is the formula for n=k+1. Proved.
Example 2: Prove 2^n>n for all n>=1.
Base: n=1. 2^1=2>1. True.
Assume 2^k>k. Prove 2^(k+1)>k+1.
2^(k+1)=2×2^k>2k (using hypothesis). 2k=k+k>=k+1 (since k>=1).
So 2^(k+1)>k+1. Proved.
Example 3: Prove 4^n-1 divisible by 3.
Base: 4^1-1=3. Divisible by 3. True.
Assume 4^k-1=3m for some integer m.
4^(k+1)-1=4×4^k-1=4(3m+1)-1=12m+4-1=12m+3=3(4m+1). Divisible by 3. Proved.
COMMON MISTAKES:
BOTH steps are necessary. Proving only base case is not enough.
In inductive step: assume P(k), then DERIVE P(k+1) (not assume P(k+1)).
The technique works by domino effect: if each domino knocks next, all fall.""",
    metadata={"source": "ncert", "topic": "algebra", "class_level": "class_11", "chapter": "ch4", "difficulty": "intermediate"}),

    Document(page_content="""Class 11 | Ch5: Complex Numbers and Quadratic Equations
COMPLEX NUMBER: z=a+ib where a=real part, b=imaginary part, i=sqrt(-1).
i^1=i, i^2=-1, i^3=-i, i^4=1. Pattern repeats every 4.
i^n: divide n by 4, use remainder (0→1, 1→i, 2→-1, 3→-i).
ALGEBRA OF COMPLEX NUMBERS:
Addition: (a+ib)+(c+id)=(a+c)+i(b+d).
Multiplication: (a+ib)(c+id)=(ac-bd)+i(ad+bc).
Conjugate of z=a+ib is z_bar=a-ib.
|z|=sqrt(a^2+b^2) (modulus/absolute value).
z×z_bar=|z|^2=a^2+b^2.
Division: z1/z2=z1×z2_bar/|z2|^2.
ARGAND PLANE: Complex number a+ib plotted as point (a,b).
POLAR FORM: z=r(cos(theta)+i sin(theta)) where r=|z|, theta=arg(z).
arg(z)=tan^(-1)(b/a) (adjust for quadrant).
DE MOIVRE'S THEOREM: (cos(theta)+i sin(theta))^n=cos(n*theta)+i sin(n*theta).
CUBE ROOTS OF UNITY:
x^3=1. Solutions: 1, omega, omega^2 where omega=(-1+i*sqrt3)/2.
Properties: 1+omega+omega^2=0. omega^3=1. omega_bar=omega^2.
QUADRATIC WITH COMPLEX ROOTS:
ax^2+bx+c=0, D=b^2-4ac<0: roots=(-b±i*sqrt(-D))/2a. Roots are conjugates.
SOLVED EXAMPLES:
Example 1: Modulus and argument of z=-1+i*sqrt3.
|z|=sqrt(1+3)=2. tan(alpha)=sqrt3/1=sqrt3 → alpha=pi/3.
z is in Q2 (real negative, imag positive). arg(z)=pi-pi/3=2pi/3.
Polar form: z=2(cos(2pi/3)+i sin(2pi/3)).
Example 2: Find (1+i)^10 using De Moivre.
1+i=sqrt2(cos(pi/4)+i sin(pi/4)).
(1+i)^10=(sqrt2)^10(cos(10pi/4)+i sin(10pi/4))=32(cos(5pi/2)+i sin(5pi/2))=32(0+i)=32i.
Example 3: Cube roots of unity. 1+omega+omega^2=0. omega^3=1.
If 1,omega,omega^2 are roots: sum=0=-b/a → b=0. Product=1=c/a → c=a. Equation: x^3-1=0.
COMMON MISTAKES:
i^2=-1, NOT +1. i^0=1 (not i).
Conjugate changes sign of imaginary part only: conjugate of (3-2i) is (3+2i).
|z|^2=a^2+b^2 (always positive real number).""",
    metadata={"source": "ncert", "topic": "algebra", "class_level": "class_11", "chapter": "ch5", "difficulty": "intermediate"}),

    Document(page_content="""Class 11 | Ch6: Linear Inequalities
RULES FOR INEQUALITIES:
Adding/subtracting same quantity: inequality sign UNCHANGED.
Multiplying/dividing by POSITIVE number: sign UNCHANGED.
Multiplying/dividing by NEGATIVE number: sign REVERSED.
SOLVING LINEAR INEQUALITIES IN ONE VARIABLE:
Solve like equation but reverse sign when multiplying/dividing by negative.
3x-2>2x+1 → x>3. Solution: (3,infinity). On number line: open circle at 3, arrow right.
GRAPHICAL METHOD FOR TWO VARIABLES:
ax+by<c: boundary line ax+by=c (dashed for < or >, solid for <= or >=).
Test point (usually origin) to determine which side.
SYSTEM OF INEQUALITIES:
Find region satisfying ALL inequalities simultaneously (feasible region).
SOLVED EXAMPLES:
Example 1: Solve 3x-2>2x+1.
3x-2x>1+2 → x>3. Solution set: (3,∞).
Example 2: Solve -3<(4x-1)/5<3.
Multiply by 5: -15<4x-1<15 → -14<4x<16 → -7/2<x<4.
Solution: (-3.5,4).
Example 3: Solve system x+y<=10, x+3y<=15, x>=0, y>=0.
Draw lines x+y=10 and x+3y=15. Find intersection: subtract to get 2y=5, y=2.5, x=7.5.
Feasible region: bounded by vertices (0,0),(10,0),(7.5,2.5),(0,5).
Example 4: IQ score: 62+4x/2<72 where x=age in months over 100.
124+4x<144 → 4x<20 → x<5. So age < 105 months.
COMMON MISTAKES:
MUST reverse inequality when multiplying/dividing by NEGATIVE number.
For absolute value: |x|<a means -a<x<a (two conditions combined).
Dashed line for strict inequality (<,>). Solid line for (<=,>=).""",
    metadata={"source": "ncert", "topic": "algebra", "class_level": "class_11", "chapter": "ch6", "difficulty": "intermediate"}),

    Document(page_content="""Class 11 | Ch7: Permutations and Combinations
FUNDAMENTAL COUNTING PRINCIPLE:
If task A can be done in m ways and task B in n ways, both together: m×n ways.
FACTORIAL: n!=n×(n-1)×(n-2)×...×2×1. 0!=1. 1!=1.
PERMUTATIONS (ordered arrangements):
nPr = n!/(n-r)! = n×(n-1)×...×(n-r+1). (r items from n, order matters.)
Permutations of n items = n!
Permutations with repetition: n^r (r items from n with repetition).
Permutations with identical items: n!/p!q!r!... (p identical of one type, q of another etc.)
CIRCULAR PERMUTATIONS: (n-1)! for n distinct items in circle.
COMBINATIONS (unordered selections):
nCr = n!/(r!(n-r)!) = nPr/r!. (r items from n, order does not matter.)
nCr = nC(n-r). nC0=nCn=1. nC1=n.
PASCAL'S IDENTITY: nCr + nCr-1 = (n+1)Cr.
SOLVED EXAMPLES:
Example 1: 5 boys and 3 girls sit in row, girls always together.
Treat 3 girls as 1 unit. Total units=6. Arrange 6 units: 6! ways. Girls arrange among themselves: 3! ways.
Total=6!×3!=720×6=4320.
Example 2: Find 7C3.
7C3=7!/(3!×4!)=7×6×5/(3×2×1)=210.
Example 3: Prove nCr+nCr-1=(n+1)Cr.
nCr+nCr-1=n!/(r!(n-r)!)+n!/((r-1)!(n-r+1)!)
=n!/((r-1)!(n-r)!) × [1/r+1/(n-r+1)]
=n!/((r-1)!(n-r)!) × (n+1)/(r(n-r+1))
=(n+1)!/(r!(n-r+1)!)=(n+1)Cr. Proved.
Example 4: How many ways to choose 3 from 7 if 2 specific must be included?
2 fixed. Choose 1 from remaining 5: 5C1=5 ways.
COMMON MISTAKES:
Permutation: ORDER matters (abc≠bac). Combination: order does NOT matter.
Circular: fix one position, arrange remaining (n-1)!.
nCr = nC(n-r): 10C3=10C7=120.""",
    metadata={"source": "ncert", "topic": "combinatorics", "class_level": "class_11", "chapter": "ch7", "difficulty": "intermediate"}),

    Document(page_content="""Class 11 | Ch8: Binomial Theorem
BINOMIAL THEOREM: (a+b)^n = sum(r=0 to n) nCr × a^(n-r) × b^r.
General term: T(r+1) = nCr × a^(n-r) × b^r. (r starts from 0.)
PROPERTIES:
Number of terms = n+1.
Sum of binomial coefficients = 2^n (put a=b=1).
Sum of odd-position coefficients = Sum of even-position = 2^(n-1).
Binomial coefficients: nC0,nC1,...,nCn form Pascal's triangle.
MIDDLE TERM:
If n is even: middle term is T(n/2+1). One middle term.
If n is odd: two middle terms T((n+1)/2) and T((n+3)/2).
TERM INDEPENDENT OF x: find r such that power of x in T(r+1) = 0.
GREATEST TERM: find r such that T(r+1)/T(r) >= 1.
SOLVED EXAMPLES:
Example 1: Expand (2x-3y)^4.
T(r+1)=4Cr×(2x)^(4-r)×(-3y)^r.
r=0: 4C0×16x^4=16x^4. r=1: 4C1×8x^3×(-3y)=-96x^3y.
r=2: 4C2×4x^2×9y^2=216x^2y^2. r=3: 4C3×2x×(-27y^3)=-216xy^3.
r=4: 4C4×81y^4=81y^4.
Expansion: 16x^4-96x^3y+216x^2y^2-216xy^3+81y^4.
Example 2: Find 5th term in (x+2)^8.
T5=T(4+1): r=4. T5=8C4×x^4×2^4=70×x^4×16=1120x^4.
Example 3: Term independent of x in (x+1/x)^10.
T(r+1)=10Cr×x^(10-r)×(1/x)^r=10Cr×x^(10-2r).
For independent of x: 10-2r=0 → r=5. T6=10C5=252.
COMMON MISTAKES:
General term T(r+1) has r starting from 0, NOT 1.
For "5th term": r=4 (since T(r+1)=T5 means r+1=5, r=4).
In (a-b)^n: alternate signs. T(r+1)=nCr×a^(n-r)×(-b)^r.""",
    metadata={"source": "ncert", "topic": "algebra", "class_level": "class_11", "chapter": "ch8", "difficulty": "intermediate"}),

    Document(page_content="""Class 11 | Ch9: Sequences and Series
ARITHMETIC PROGRESSION: a, a+d, a+2d,...
a_n=a+(n-1)d. S_n=n/2[2a+(n-1)d]=n/2[a+l].
Arithmetic Mean AM=(a+b)/2. AM between a and b.
GEOMETRIC PROGRESSION: a, ar, ar^2,...
a_n=ar^(n-1). S_n=a(r^n-1)/(r-1) for r≠1. S_n=na for r=1.
Sum of infinite GP: S_inf=a/(1-r) for |r|<1.
Geometric Mean GM=sqrt(ab). GM between a and b.
RELATIONSHIP: AM>=GM (equality when a=b).
HARMONIC PROGRESSION: reciprocals form AP. HM=2ab/(a+b).
AM>=GM>=HM (with equality when a=b).
SPECIAL SERIES:
Sum of n natural numbers: n(n+1)/2.
Sum of squares: n(n+1)(2n+1)/6.
Sum of cubes: [n(n+1)/2]^2.
SOLVED EXAMPLES:
Example 1: GP 1+3+9+...+2187.
a=1, r=3. 2187=3^7, so n=8. S8=1×(3^8-1)/(3-1)=(6561-1)/2=3280.
Example 2: AM=10, GM=8. Find numbers.
(a+b)/2=10 → a+b=20. sqrt(ab)=8 → ab=64.
a and b are roots of x^2-20x+64=0 → (x-16)(x-4)=0. Numbers: 4 and 16.
Example 3: Sum(2k+1) for k=1 to 20.
=sum(2k)+sum(1)=2×sum(k)+20=2×(20×21/2)+20=420+20=440.
Example 4: Sum 1/2+1/4+1/8+... (infinite GP).
a=1/2, r=1/2. S=a/(1-r)=(1/2)/(1/2)=1.
COMMON MISTAKES:
Infinite GP sum only valid when |r|<1.
AM>=GM: equality holds only when both numbers are equal.
Sum of cubes=[sum of natural numbers]^2.""",
    metadata={"source": "ncert", "topic": "algebra", "class_level": "class_11", "chapter": "ch9", "difficulty": "intermediate"}),

    Document(page_content="""Class 11 | Ch10: Straight Lines
SLOPE: m=tan(theta)=(y2-y1)/(x2-x1). Horizontal line: m=0. Vertical line: undefined.
Parallel lines: m1=m2. Perpendicular lines: m1×m2=-1.
EQUATIONS OF LINES:
Slope-intercept: y=mx+c (m=slope, c=y-intercept).
Point-slope: y-y1=m(x-x1).
Two-point form: (y-y1)/(y2-y1)=(x-x1)/(x2-x1).
Intercept form: x/a+y/b=1 (a=x-intercept, b=y-intercept).
Normal form: x cos(alpha)+y sin(alpha)=p (p=perpendicular distance from origin, alpha=angle).
General form: ax+by+c=0.
DISTANCE FORMULAS:
Distance from point (x1,y1) to line ax+by+c=0: d=|ax1+by1+c|/sqrt(a^2+b^2).
Distance between parallel lines ax+by+c1=0 and ax+by+c2=0: |c1-c2|/sqrt(a^2+b^2).
ANGLE BETWEEN LINES:
tan(theta)=|(m1-m2)/(1+m1m2)|.
SOLVED EXAMPLES:
Example 1: Line through (2,-3) perpendicular to 3x-4y+5=0.
Slope of given line=3/4. Perpendicular slope=-4/3.
Line: y-(-3)=(-4/3)(x-2) → 3y+9=-4x+8 → 4x+3y+1=0.
Example 2: Distance between 3x+4y-5=0 and 3x+4y+15=0.
d=|(-5)-(15)|/sqrt(9+16)=20/5=4 units.
Example 3: Find foot of perpendicular from (1,2) to line 2x-3y+4=0.
Use formula: (x-x1)/a=(y-y1)/b=-(ax1+by1+c)/(a^2+b^2).
=(x-1)/2=(y-2)/(-3)=-(2-6+4)/(4+9)=0/13=0.
So x=1, y=2. Point itself lies on line. (Check: 2-6+4=0. Yes.)
COMMON MISTAKES:
Perpendicular lines: m1×m2=-1 (product is -1, not sum).
Distance formula: divide by sqrt(a^2+b^2) NOT (a^2+b^2).
Parallel lines have SAME slope. Perpendicular lines: slopes are NEGATIVE RECIPROCALS.""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_11", "chapter": "ch10", "difficulty": "intermediate"}),

    Document(page_content="""Class 11 | Ch11: Conic Sections
CIRCLE: (x-h)^2+(y-k)^2=r^2. Centre (h,k), radius r.
General: x^2+y^2+2gx+2fy+c=0. Centre (-g,-f), radius=sqrt(g^2+f^2-c).
PARABOLA (standard forms):
y^2=4ax: opens right. Focus (a,0). Directrix x=-a. Vertex (0,0). Axis=x-axis.
y^2=-4ax: opens left. Focus (-a,0). Directrix x=a.
x^2=4ay: opens up. Focus (0,a). Directrix y=-a. Axis=y-axis.
x^2=-4ay: opens down. Focus (0,-a). Directrix y=a.
Latus rectum: chord through focus perpendicular to axis. Length=4a.
ELLIPSE: x^2/a^2+y^2/b^2=1 (a>b>0).
Centre (0,0). Vertices (±a,0). Co-vertices (0,±b).
Foci (±c,0) where c^2=a^2-b^2. Eccentricity e=c/a<1.
Length of major axis=2a. Minor axis=2b. Latus rectum=2b^2/a.
HYPERBOLA: x^2/a^2-y^2/b^2=1.
Foci (±c,0) where c^2=a^2+b^2. Eccentricity e=c/a>1.
Asymptotes: y=±(b/a)x. Latus rectum=2b^2/a.
SOLVED EXAMPLES:
Example 1: Parabola y^2=12x. Find focus, directrix, latus rectum.
4a=12 → a=3. Focus (3,0). Directrix x=-3. Latus rectum=12.
Example 2: Ellipse, foci (±3,0), semi-major axis a=5.
c=3, a=5. b^2=a^2-c^2=25-9=16. b=4.
Equation: x^2/25+y^2/16=1.
Example 3: Find equation of circle with centre (2,-3) and radius 5.
(x-2)^2+(y+3)^2=25. Expanded: x^2+y^2-4x+6y-12=0.
COMMON MISTAKES:
Ellipse: c^2=a^2-b^2 (c<a). Hyperbola: c^2=a^2+b^2 (c>a).
For parabola y^2=4ax: COMPARE with standard form to find a (4a=coefficient).
Eccentricity: circle e=0, ellipse 0<e<1, parabola e=1, hyperbola e>1.""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_11", "chapter": "ch11", "difficulty": "intermediate"}),

    Document(page_content="""Class 11 | Ch12: Introduction to Three Dimensional Geometry
COORDINATES IN 3D: Point P=(x,y,z). Three mutually perpendicular axes: x,y,z.
OCTANTS: 3D space divided into 8 octants by coordinate planes.
DISTANCE FORMULA:
Distance between P(x1,y1,z1) and Q(x2,y2,z2):
PQ=sqrt((x2-x1)^2+(y2-y1)^2+(z2-z1)^2).
Distance from origin: OP=sqrt(x^2+y^2+z^2).
SECTION FORMULA (Internal Division):
Point dividing PQ in ratio m:n internally:
R=((mx2+nx1)/(m+n), (my2+ny1)/(m+n), (mz2+nz1)/(m+n)).
MIDPOINT: M=((x1+x2)/2, (y1+y2)/2, (z1+z2)/2).
CENTROID OF TRIANGLE:
G=((x1+x2+x3)/3, (y1+y2+y3)/3, (z1+z2+z3)/3).
COORDINATE PLANES:
xy-plane: z=0. yz-plane: x=0. xz-plane: y=0.
Distance from xy-plane: |z|. From yz-plane: |x|. From xz-plane: |y|.
SOLVED EXAMPLES:
Example 1: Distance between A(1,2,3) and B(4,-2,6).
AB=sqrt((4-1)^2+(-2-2)^2+(6-3)^2)=sqrt(9+16+9)=sqrt(34).
Example 2: Find point dividing A(2,1,3) and B(5,4,6) in ratio 2:1.
P=((2×5+1×2)/3,(2×4+1×1)/3,(2×6+1×3)/3)=(12/3,9/3,15/3)=(4,3,5).
Example 3: Show A(0,7,-10), B(1,6,-6), C(4,9,-6) form a right triangle.
AB=sqrt(1+1+16)=sqrt(18). BC=sqrt(9+9+0)=sqrt(18). AC=sqrt(16+4+16)=sqrt(36)=6.
AB^2+BC^2=18+18=36=AC^2. Right angle at B.
COMMON MISTAKES:
3D distance has THREE terms under square root (not two).
Section formula extends naturally from 2D — same structure but three coordinates.
Midpoint: average each coordinate SEPARATELY.""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_11", "chapter": "ch12", "difficulty": "intermediate"}),

    Document(page_content="""Class 11 | Ch13: Limits and Derivatives
LIMIT: lim(x→a) f(x) = L means f(x) approaches L as x approaches a.
Left limit: lim(x→a-) f(x). Right limit: lim(x→a+) f(x).
Limit exists iff left limit = right limit.
STANDARD LIMITS:
lim(x→0) sin(x)/x = 1. lim(x→0) (1-cos(x))/x = 0.
lim(x→0) tan(x)/x = 1. lim(x→0) (e^x-1)/x = 1.
lim(x→0) (a^x-1)/x = ln(a). lim(x→a) (x^n-a^n)/(x-a) = na^(n-1).
ALGEBRA OF LIMITS:
lim(f±g)=lim f ± lim g. lim(fg)=lim f × lim g. lim(f/g)=lim f/lim g (if lim g≠0).
lim(cf)=c×lim f. lim(f^n)=(lim f)^n.
DERIVATIVES (FIRST PRINCIPLES):
f'(x)=lim(h→0) [f(x+h)-f(x)]/h.
STANDARD DERIVATIVES:
d/dx[x^n]=nx^(n-1). d/dx[sin x]=cos x. d/dx[cos x]=-sin x.
d/dx[tan x]=sec^2 x. d/dx[e^x]=e^x. d/dx[ln x]=1/x.
d/dx[constant]=0. d/dx[cf(x)]=cf'(x). d/dx[f±g]=f'±g'.
PRODUCT RULE: d/dx[fg]=f'g+fg'.
QUOTIENT RULE: d/dx[f/g]=(f'g-fg')/g^2.
SOLVED EXAMPLES:
Example 1: lim(x→0) sin(3x)/x=3×lim(x→0) sin(3x)/(3x)=3×1=3.
Example 2: Derivative of x^3 sin x.
d/dx[x^3 sin x]=3x^2 sin x+x^3 cos x (product rule).
Example 3: Derivative of (x^2+1)/(x^2-1).
Using quotient rule: [(2x)(x^2-1)-(x^2+1)(2x)]/(x^2-1)^2.
=[2x^3-2x-2x^3-2x]/(x^2-1)^2=(-4x)/(x^2-1)^2.
Example 4: lim(x→2) (x^3-8)/(x-2)=lim(x→2) (x^2+2x+4)=4+4+4=12.
Using formula: na^(n-1)=3×2^2=12. Confirmed.
COMMON MISTAKES:
lim(x→0) sin(x)/x=1 only when angle is in RADIANS.
Product rule: d/dx[fg]=f'g+fg' NOT f'g'.
Quotient rule: numerator is f'g-fg' (not fg'-f'g).""",
    metadata={"source": "ncert", "topic": "calculus", "class_level": "class_11", "chapter": "ch13", "difficulty": "intermediate"}),

    Document(page_content="""Class 11 | Ch14: Mathematical Reasoning
STATEMENTS: declarative sentence that is either TRUE or FALSE (not both).
Not a statement: questions, exclamations, commands, ambiguous sentences.
CONNECTIVES:
AND (conjunction ∧): p∧q true only when BOTH p and q are true.
OR (disjunction ∨): p∨q true when AT LEAST ONE is true.
NOT (negation ¬): ¬p is opposite truth value.
IMPLICATION: p→q (if p then q). False only when p true and q false.
BICONDITIONAL: p↔q (p if and only if q). True when both same truth value.
TRUTH TABLES: systematic listing of all truth value combinations.
CONDITIONAL STATEMENTS:
Converse of p→q: q→p.
Inverse of p→q: ¬p→¬q.
Contrapositive of p→q: ¬q→¬p. (Contrapositive is LOGICALLY EQUIVALENT to original.)
QUANTIFIERS:
Universal: "For all" (∀). Existential: "There exists" (∃).
Negation of "For all x, P(x)": "There exists x such that NOT P(x)".
Negation of "There exists x, P(x)": "For all x, NOT P(x)".
METHODS OF PROOF:
Direct proof: assume hypothesis, derive conclusion.
Contrapositive: prove ¬q→¬p (equivalent to p→q).
Contradiction: assume statement false, derive contradiction.
By example (existence): give one example.
By counter-example (disproof): give one counter-example.
SOLVED EXAMPLES:
Example 1: Negation of "All primes are odd."
"There exists a prime that is NOT odd." (2 is a prime that is even — counter-example.)
Example 2: Converse, inverse, contrapositive of "If x>5 then x^2>25."
Converse: If x^2>25 then x>5. (FALSE: x=-6 gives x^2=36>25 but x<5.)
Inverse: If x≤5 then x^2≤25. (FALSE: x=-6.)
Contrapositive: If x^2≤25 then x≤5. (TRUE, equivalent to original.)
Example 3: Check "If n is odd then n^2 is odd" by contrapositive.
Contrapositive: If n^2 is even then n is even.
If n^2=2k then n=2m (provable). Contrapositive true → original true.
COMMON MISTAKES:
Converse is NOT always equivalent to original statement.
Contrapositive IS always equivalent to original.
To DISPROVE: one counter-example suffices. To PROVE universal: cannot use examples.""",
    metadata={"source": "ncert", "topic": "logic", "class_level": "class_11", "chapter": "ch14", "difficulty": "intermediate"}),

    Document(page_content="""Class 11 | Ch15: Statistics
MEASURES OF DISPERSION (how spread out data is):
Range = Maximum - Minimum.
MEAN DEVIATION:
Mean deviation about mean: MD(x_bar)=sum(|xi-x_bar|)/n.
Mean deviation about median: MD(M)=sum(|xi-M|)/n.
For grouped data: MD=sum(f|xi-x_bar|)/sum(f).
VARIANCE AND STANDARD DEVIATION:
Variance: sigma^2=sum((xi-x_bar)^2)/n (ungrouped).
For grouped: sigma^2=sum(f(xi-x_bar)^2)/sum(f).
Shortcut: sigma^2=(sum(xi^2)/n)-(x_bar)^2 = (sum(fi*xi^2)/sum(fi))-(x_bar)^2.
Standard Deviation sigma=sqrt(Variance).
COEFFICIENT OF VARIATION: CV=(sigma/x_bar)×100.
Used to compare variability of two distributions with different means.
Higher CV = more variable/inconsistent.
For comparing: data with higher CV is more variable.
ANALYSIS OF FREQUENCY DISTRIBUTIONS:
Two distributions compared by CV when means are different.
Two distributions compared directly by sigma when means are same.
SOLVED EXAMPLES:
Example 1: Find variance and SD of 6,8,10,12,14.
Mean=50/5=10.
Deviations from mean: -4,-2,0,2,4. Squared: 16,4,0,4,16.
Variance=40/5=8. SD=sqrt(8)=2sqrt(2)≈2.83.
Example 2: Two distributions: A has mean=25, SD=5. B has mean=10, SD=4.
CV(A)=(5/25)×100=20%. CV(B)=(4/10)×100=40%.
B is more variable (higher CV).
Example 3: Find MD about mean for 2,4,6,8,10.
Mean=6. |deviations|=4,2,0,2,4. MD=12/5=2.4.
COMMON MISTAKES:
Variance is always non-negative (it's sum of SQUARES divided by n).
SD=sqrt(Variance), NOT Variance=SD^2 (both are true, don't confuse direction).
CV is in PERCENTAGE: multiply by 100.""",
    metadata={"source": "ncert", "topic": "statistics", "class_level": "class_11", "chapter": "ch15", "difficulty": "intermediate"}),

    Document(page_content="""Class 11 | Ch16: Probability
RANDOM EXPERIMENT: outcome cannot be predicted with certainty.
SAMPLE SPACE S: set of all possible outcomes.
EVENT: subset of sample space. Simple event: one outcome. Compound: multiple outcomes.
ALGEBRA OF EVENTS:
Complement of A: A'=S-A. A∪A'=S. A∩A'=phi.
Mutually exclusive: A∩B=phi (cannot occur together).
Exhaustive: A∪B=S (together cover all outcomes).
AXIOMATIC APPROACH TO PROBABILITY:
P(S)=1. 0<=P(A)<=1. P(A∪B)=P(A)+P(B) if A,B mutually exclusive.
ADDITION THEOREM:
P(A∪B)=P(A)+P(B)-P(A∩B).
P(A∪B∪C)=P(A)+P(B)+P(C)-P(A∩B)-P(B∩C)-P(A∩C)+P(A∩B∩C).
CONDITIONAL PROBABILITY:
P(A|B)=P(A∩B)/P(B). (Probability of A given B has occurred.)
INDEPENDENT EVENTS:
A and B independent if P(A∩B)=P(A)×P(B).
Equivalent: P(A|B)=P(A). (Occurrence of B doesn't affect A.)
MULTIPLICATION THEOREM:
P(A∩B)=P(A)×P(B|A)=P(B)×P(A|B).
SOLVED EXAMPLES:
Example 1: P(A)=0.4, P(B)=0.5, P(A∩B)=0.2.
P(A∪B)=0.4+0.5-0.2=0.7.
P(A|B)=P(A∩B)/P(B)=0.2/0.5=0.4.
(Note: P(A|B)=P(A)=0.4, so A and B are INDEPENDENT.)
Example 2: Card drawn. P(red or king).
P(red)=26/52. P(king)=4/52. P(red king)=2/52.
P(red or king)=26/52+4/52-2/52=28/52=7/13.
Example 3: Two dice. Find P(sum>9).
Favourable: (4,6),(5,5),(5,6),(6,4),(6,5),(6,6)=6 outcomes.
P=6/36=1/6.
Example 4: P(A)=1/4, P(B)=1/3. A,B independent. Find P(A or B).
P(A∩B)=1/4×1/3=1/12.
P(A∪B)=1/4+1/3-1/12=3/12+4/12-1/12=6/12=1/2.
COMMON MISTAKES:
Mutually exclusive: P(A∩B)=0. Independent: P(A∩B)=P(A)×P(B). DIFFERENT concepts.
Mutually exclusive events with nonzero probabilities are NOT independent.
P(A|B) is NOT the same as P(B|A).""",
    metadata={"source": "ncert", "topic": "probability", "class_level": "class_11", "chapter": "ch16", "difficulty": "intermediate"}),


    # ── CLASS 12 — All 13 Chapters ──────────────────────────────────

    Document(page_content="""Class 12 | Ch1: Relations and Functions
TYPES OF RELATIONS:
Empty relation: no element of A related to any element. R=phi.
Universal relation: every element related to every element. R=A×A.
Reflexive: (a,a) in R for all a in A.
Symmetric: if (a,b) in R then (b,a) in R.
Transitive: if (a,b) and (b,c) in R then (a,c) in R.
Equivalence relation: reflexive + symmetric + transitive.
EQUIVALENCE CLASSES: set of all elements related to a given element.
TYPES OF FUNCTIONS:
One-one (injective): f(a)=f(b) implies a=b. No two inputs give same output.
Onto (surjective): range=codomain. Every element of codomain has pre-image.
Bijective: one-one AND onto. Inverse function exists.
COMPOSITION: (fog)(x)=f(g(x)). gof≠fog generally.
If f and g are one-one then fog is one-one. If f and g are onto then fog is onto.
INVERTIBLE FUNCTIONS:
f is invertible iff f is bijective.
(f^(-1) o f)(x)=x and (f o f^(-1))(x)=x.
BINARY OPERATIONS: * on set A: A×A→A.
Commutative: a*b=b*a. Associative: (a*b)*c=a*(b*c).
Identity element e: a*e=e*a=a. Inverse of a: a*a^(-1)=e.
SOLVED EXAMPLES:
Example 1: R={(a,b): |a-b| divisible by 5} on integers. Is it equivalence?
Reflexive: |a-a|=0 divisible by 5. Yes.
Symmetric: |a-b| div by 5 → |b-a|=|a-b| div by 5. Yes.
Transitive: |a-b|=5k, |b-c|=5m → |a-c|<=|a-b|+|b-c|=5(k+m). Yes.
Equivalence relation confirmed.
Example 2: f:R→R, f(x)=2x+3. Show bijective and find inverse.
One-one: f(a)=f(b) → 2a+3=2b+3 → a=b. Yes.
Onto: for any y, x=(y-3)/2 in R. Yes. Bijective.
f^(-1)(x)=(x-3)/2.
COMMON MISTAKES:
Equivalence class [a]={b in A: (a,b) in R}. Different elements may have same class.
A function must be bijective for inverse to exist (not just one-one or just onto).
fog means g applied FIRST then f.""",
    metadata={"source": "ncert", "topic": "functions", "class_level": "class_12", "chapter": "ch1", "difficulty": "advanced"}),

    Document(page_content="""Class 12 | Ch2: Inverse Trigonometric Functions
DOMAINS AND RANGES (Principal Value Branch):
sin^(-1): domain [-1,1], range [-pi/2, pi/2].
cos^(-1): domain [-1,1], range [0, pi].
tan^(-1): domain R, range (-pi/2, pi/2).
cosec^(-1): domain R-(-1,1), range [-pi/2,pi/2]-{0}.
sec^(-1): domain R-(-1,1), range [0,pi]-{pi/2}.
cot^(-1): domain R, range (0,pi).
KEY PROPERTIES:
sin^(-1)(x)+cos^(-1)(x)=pi/2 for x in [-1,1].
tan^(-1)(x)+cot^(-1)(x)=pi/2 for all x.
sec^(-1)(x)+cosec^(-1)(x)=pi/2 for |x|>=1.
sin^(-1)(-x)=-sin^(-1)(x). cos^(-1)(-x)=pi-cos^(-1)(x).
tan^(-1)(-x)=-tan^(-1)(x).
sin^(-1)(1/x)=cosec^(-1)(x) for |x|>=1.
cos^(-1)(1/x)=sec^(-1)(x) for |x|>=1.
tan^(-1)(1/x)=cot^(-1)(x) for x>0.
ADDITION FORMULAS:
tan^(-1)(x)+tan^(-1)(y)=tan^(-1)((x+y)/(1-xy)) if xy<1.
tan^(-1)(x)+tan^(-1)(y)=pi+tan^(-1)((x+y)/(1-xy)) if xy>1 and x>0.
2 tan^(-1)(x)=sin^(-1)(2x/(1+x^2))=cos^(-1)((1-x^2)/(1+x^2))=tan^(-1)(2x/(1-x^2)).
SOLVED EXAMPLES:
Example 1: Find principal value of sin^(-1)(-1/2).
sin^(-1)(1/2)=pi/6. sin^(-1)(-1/2)=-pi/6. (In range [-pi/2,pi/2]).
Example 2: Find principal value of cos^(-1)(-sqrt3/2).
cos^(-1)(sqrt3/2)=pi/6. cos^(-1)(-sqrt3/2)=pi-pi/6=5pi/6. (In range [0,pi]).
Example 3: Simplify tan^(-1)(cosx-sinx)/(cosx+sinx).
Divide by cosx: tan^(-1)((1-tanx)/(1+tanx))=tan^(-1)(tan(pi/4-x))=pi/4-x.
(Valid when pi/4-x is in range (-pi/2,pi/2).)
Example 4: Prove sin^(-1)x+cos^(-1)x=pi/2.
Let sin^(-1)x=theta. Then x=sin(theta). cos^(-1)x=cos^(-1)(sin theta)=cos^(-1)(cos(pi/2-theta))=pi/2-theta.
Sum=theta+pi/2-theta=pi/2. Proved.
COMMON MISTAKES:
sin^(-1)(x) is NOT 1/sin(x). It is the inverse FUNCTION.
Principal value of cos^(-1): range is [0,pi], NOT [-pi/2,pi/2].
cos^(-1)(-x)=pi-cos^(-1)(x) (NOT -cos^(-1)(x) like sine).""",
    metadata={"source": "ncert", "topic": "trigonometry", "class_level": "class_12", "chapter": "ch2", "difficulty": "advanced"}),

    Document(page_content="""Class 12 | Ch3: Matrices
MATRIX: rectangular array of numbers in rows and columns. Order: m×n (m rows, n cols).
TYPES: Row(1×n), Column(m×1), Square(n×n), Zero/Null, Identity(diagonal=1, rest=0), Diagonal, Scalar.
OPERATIONS:
Addition: (A+B)_ij=a_ij+b_ij. Same order required.
Scalar multiplication: (kA)_ij=k×a_ij.
Multiplication: (AB)_ij=sum over k of a_ik×b_kj. Order: (m×n)(n×p)=(m×p).
AB is defined iff columns of A=rows of B. AB≠BA generally.
TRANSPOSE: A^T: rows become columns. (A^T)_ij=A_ji.
(A+B)^T=A^T+B^T. (AB)^T=B^T A^T. (A^T)^T=A.
SYMMETRIC: A^T=A (a_ij=a_ji). SKEW-SYMMETRIC: A^T=-A (a_ij=-a_ji, diagonal=0).
ANY SQUARE MATRIX = Symmetric part + Skew-symmetric part.
A=(A+A^T)/2 + (A-A^T)/2. First part symmetric, second skew-symmetric.
ELEMENTARY OPERATIONS (Row/Column):
Ri↔Rj (interchange). Ri→kRi (multiply by scalar). Ri→Ri+kRj (add multiple of another row).
Used in finding inverse by row reduction.
SOLVED EXAMPLES:
Example 1: A=[[1,2],[3,4]]. Find A+A^T and show symmetric.
A^T=[[1,3],[2,4]]. A+A^T=[[2,5],[5,8]]. (A+A^T)^T=[[2,5],[5,8]]=A+A^T. Symmetric.
Example 2: Express A=[[1,2],[3,4]] as sum of symmetric and skew-symmetric.
Symmetric=(A+A^T)/2=[[1,2.5],[2.5,4]].
Skew-symmetric=(A-A^T)/2=[[0,-0.5],[0.5,0]].
Example 3: If A=[[1,2],[3,4]] and B=[[5,6],[7,8]], find AB.
AB=[[1×5+2×7, 1×6+2×8],[3×5+4×7, 3×6+4×8]]=[[19,22],[43,50]].
COMMON MISTAKES:
AB≠BA in general (matrix multiplication is NOT commutative).
(AB)^T=B^T A^T (ORDER REVERSES, not A^T B^T).
Dimensions: (m×n)(n×p)→(m×p). Inner dimensions must match.""",
    metadata={"source": "ncert", "topic": "algebra", "class_level": "class_12", "chapter": "ch3", "difficulty": "advanced"}),

    Document(page_content="""Class 12 | Ch4: Determinants
DETERMINANT: scalar value computed from square matrix.
det(2×2): |a b; c d|=ad-bc.
det(3×3) by expansion along row 1:
|a1 b1 c1; a2 b2 c2; a3 b3 c3|=a1(b2c3-b3c2)-b1(a2c3-a3c2)+c1(a2b3-a3b2).
PROPERTIES OF DETERMINANTS:
1. Rows and columns can be interchanged: det(A)=det(A^T).
2. Interchange two rows: determinant changes sign.
3. Two identical rows: det=0.
4. Multiply row by k: det multiplied by k.
5. Add multiple of one row to another: det unchanged.
6. det(AB)=det(A)×det(B). det(kA)=k^n×det(A) for n×n matrix.
MINORS AND COFACTORS:
Minor M_ij: determinant of matrix obtained by deleting row i and column j.
Cofactor C_ij=(-1)^(i+j) × M_ij.
ADJOINT: adj(A)=transpose of cofactor matrix.
INVERSE: A^(-1)=adj(A)/det(A). Exists iff det(A)≠0.
AREA OF TRIANGLE: (1/2)|x1(y2-y3)+x2(y3-y1)+x3(y1-y2)|.
Using determinant: (1/2)|det([[x1,y1,1],[x2,y2,1],[x3,y3,1]])|.
CRAMER'S RULE for ax+by=e, cx+dy=f:
D=|a b; c d|=ad-bc. D_x=|e b; f d|. D_y=|a e; c f|.
x=D_x/D, y=D_y/D (only if D≠0).
SOLVED EXAMPLES:
Example 1: Find det([[2,3],[-1,4]])=2×4-3×(-1)=8+3=11.
Example 2: Solve x+y+z=6, 2x-y+z=3, x+2y-z=2 by Cramer's rule.
D=det([[1,1,1],[2,-1,1],[1,2,-1]])=1(1-2)-1(-2-1)+1(4+1)=-1+3+5=7.
D_x=det([[6,1,1],[3,-1,1],[2,2,-1]])=6(1-2)-1(-3-2)+1(6+2)=-6+5+8=7.
x=D_x/D=7/7=1. Similarly y=2, z=3.
Example 3: A=[[1,2],[3,4]]. Find A^(-1).
det(A)=4-6=-2. Cofactor matrix=[[4,-3],[-2,1]]. adj(A)=[[4,-2],[-3,1]].
A^(-1)=(1/-2)[[4,-2],[-3,1]]=[[-2,1],[3/2,-1/2]].
COMMON MISTAKES:
Cofactor includes the sign (-1)^(i+j). Minor does NOT include the sign.
det(kA)=k^n×det(A) for n×n matrix (NOT just k×det(A)).
A^(-1) exists only when det(A)≠0 (non-singular matrix).""",
    metadata={"source": "ncert", "topic": "algebra", "class_level": "class_12", "chapter": "ch4", "difficulty": "advanced"}),

    Document(page_content="""Class 12 | Ch5: Continuity and Differentiability
CONTINUITY at x=a: lim(x→a) f(x) = f(a).
Three conditions: f(a) defined, limit exists, limit equals f(a).
Continuous function: continuous at every point in domain.
Sum, difference, product of continuous functions is continuous.
Composite of continuous functions is continuous.
DIFFERENTIABILITY: f'(a)=lim(h→0) [f(a+h)-f(a)]/h exists.
Differentiable → Continuous. Continuous does NOT imply differentiable.
|x| is continuous everywhere but NOT differentiable at x=0.
CHAIN RULE: d/dx[f(g(x))]=f'(g(x))×g'(x). dy/dx=(dy/du)×(du/dx).
IMPLICIT DIFFERENTIATION: differentiate both sides w.r.t. x, treat y as function of x.
d/dx[f(y)]=f'(y)×dy/dx.
PARAMETRIC DIFFERENTIATION: x=f(t), y=g(t). dy/dx=(dy/dt)/(dx/dt)=g'(t)/f'(t).
LOGARITHMIC DIFFERENTIATION: for y=x^x or y=f(x)^g(x). Take log both sides, differentiate.
SECOND ORDER DERIVATIVE: d^2y/dx^2=d/dx[dy/dx].
STANDARD DERIVATIVES:
d/dx[x^n]=nx^(n-1). d/dx[e^x]=e^x. d/dx[a^x]=a^x ln(a).
d/dx[ln x]=1/x. d/dx[log_a x]=1/(x ln a).
d/dx[sin x]=cos x. d/dx[cos x]=-sin x. d/dx[tan x]=sec^2 x.
d/dx[sin^(-1)x]=1/sqrt(1-x^2). d/dx[cos^(-1)x]=-1/sqrt(1-x^2).
d/dx[tan^(-1)x]=1/(1+x^2).
ROLLE'S THEOREM: if f continuous on [a,b], differentiable on (a,b), f(a)=f(b), then there exists c in (a,b) where f'(c)=0.
MEAN VALUE THEOREM (MVT/Lagrange): if f continuous on [a,b], differentiable on (a,b), then there exists c where f'(c)=[f(b)-f(a)]/(b-a).
SOLVED EXAMPLES:
Example 1: Differentiate x^x.
y=x^x → ln y=x ln x → (1/y)(dy/dx)=ln x+1 → dy/dx=x^x(1+ln x).
Example 2: If x=at^2, y=2at, find dy/dx.
dx/dt=2at, dy/dt=2a. dy/dx=2a/2at=1/t.
Example 3: Check continuity of |x-3| at x=3.
LHL=lim(x→3-)|x-3|=lim(x→3-)(3-x)=0. RHL=lim(x→3+)(x-3)=0. f(3)=0. Continuous.
But not differentiable at x=3 (left derivative=-1, right=+1, unequal).
COMMON MISTAKES:
Continuous does NOT mean differentiable. |x| is the standard counter-example.
Chain rule: derivative of OUTER function × derivative of INNER function.
In parametric: dy/dx=(dy/dt)/(dx/dt), NOT (dx/dt)/(dy/dt).""",
    metadata={"source": "ncert", "topic": "calculus", "class_level": "class_12", "chapter": "ch5", "difficulty": "advanced"}),

    Document(page_content="""Class 12 | Ch6: Applications of Derivatives
RATE OF CHANGE: dy/dx represents rate of change of y w.r.t. x.
If x and y both functions of t: use chain rule. dy/dt=(dy/dx)×(dx/dt).
TANGENT AND NORMAL:
Slope of tangent at (x1,y1): m=dy/dx|(x1,y1).
Equation of tangent: y-y1=m(x-x1).
Slope of normal=-1/m. Equation of normal: y-y1=(-1/m)(x-x1).
INCREASING AND DECREASING FUNCTIONS:
f increasing on (a,b) if f'(x)>0 for all x in (a,b).
f decreasing on (a,b) if f'(x)<0 for all x in (a,b).
MAXIMA AND MINIMA:
Critical points: where f'(x)=0 or f'(x) undefined.
First Derivative Test:
f'changes + to -: local maximum. f' changes - to +: local minimum. No change: neither.
Second Derivative Test:
f''(c)<0: local maximum. f''(c)>0: local minimum. f''(c)=0: test fails.
ABSOLUTE MAXIMA/MINIMA on [a,b]:
Evaluate f at all critical points AND endpoints. Largest=absolute max, smallest=absolute min.
APPROXIMATIONS: f(x+deltax)≈f(x)+f'(x)×deltax.
SOLVED EXAMPLES:
Example 1: Find intervals where f(x)=2x^3-9x^2+12x-5 is increasing/decreasing.
f'(x)=6x^2-18x+12=6(x^2-3x+2)=6(x-1)(x-2).
f'(x)>0 when x<1 or x>2: increasing on (-inf,1) and (2,inf).
f'(x)<0 when 1<x<2: decreasing on (1,2).
Example 2: Local maxima/minima of f above.
f'(1)=0 and f' changes + to -: local max at x=1. f(1)=2-9+12-5=0.
f'(2)=0 and f' changes - to +: local min at x=2. f(2)=16-36+24-5=-1.
Example 3: Two numbers with sum 24 and maximum product.
Let numbers be x and 24-x. P=x(24-x)=24x-x^2.
P'=24-2x=0 → x=12. P''=-2<0: maximum. Numbers: 12 and 12.
Example 4: Rate: balloon volume V=(4/3)pi*r^3. Find dV/dt when r=5, dr/dt=2.
dV/dt=4pi*r^2*(dr/dt)=4pi×25×2=200pi cm^3/s.
COMMON MISTAKES:
Critical points where f'=0 need NOT be maxima or minima (inflection points possible).
Second derivative test FAILS when f''=0 (use first derivative test instead).
For max product/area problems: always verify using second derivative test.""",
    metadata={"source": "ncert", "topic": "calculus", "class_level": "class_12", "chapter": "ch6", "difficulty": "advanced"}),

    Document(page_content="""Class 12 | Ch7: Integrals
INDEFINITE INTEGRALS:
integral(x^n dx)=x^(n+1)/(n+1)+C (n≠-1). integral(1/x dx)=ln|x|+C.
integral(e^x dx)=e^x+C. integral(a^x dx)=a^x/ln(a)+C.
integral(sin x dx)=-cos x+C. integral(cos x dx)=sin x+C.
integral(tan x dx)=ln|sec x|+C. integral(cot x dx)=ln|sin x|+C.
integral(sec x dx)=ln|sec x+tan x|+C. integral(cosec x dx)=-ln|cosec x+cot x|+C.
integral(sec^2 x dx)=tan x+C. integral(cosec^2 x dx)=-cot x+C.
integral(1/(x^2+a^2) dx)=(1/a)tan^(-1)(x/a)+C.
integral(1/sqrt(a^2-x^2) dx)=sin^(-1)(x/a)+C.
integral(1/sqrt(x^2+a^2) dx)=ln|x+sqrt(x^2+a^2)|+C.
METHODS OF INTEGRATION:
METHOD 1 - Substitution: let u=g(x), du=g'(x)dx.
integral(2x/(x^2+1) dx): let u=x^2+1, du=2x dx → integral(1/u du)=ln|u|+C=ln|x^2+1|+C.
METHOD 2 - Integration by Parts (ILATE rule):
integral(u dv)=uv-integral(v du).
ILATE order for u: Inverse trig, Logarithm, Algebraic, Trigonometric, Exponential.
integral(x e^x dx): u=x, dv=e^x dx. =xe^x-integral(e^x dx)=xe^x-e^x+C=e^x(x-1)+C.
integral(x^2 e^x dx): apply by parts TWICE.
METHOD 3 - Partial Fractions (for rational functions):
(2x+3)/((x-1)(x+2))=A/(x-1)+B/(x+2). Solve for A and B.
For repeated factor (x-1)^2: A/(x-1)+B/(x-1)^2+C/(x+2).
METHOD 4 - Special Integrals:
integral(sin^n x dx) and integral(cos^n x dx): use reduction formulas.
integral(sin^2 x dx)=x/2-sin(2x)/4+C. integral(cos^2 x dx)=x/2+sin(2x)/4+C.
DEFINITE INTEGRALS:
integral[a to b] f(x) dx=F(b)-F(a) (Fundamental Theorem).
PROPERTIES:
integral[a to b]=- integral[b to a].
integral[a to b] f(x) dx=integral[a to c] f(x) dx+integral[c to b] f(x) dx.
integral[0 to a] f(x) dx=integral[0 to a] f(a-x) dx (King's rule).
SOLVED EXAMPLES:
Example 1: integral(x^2 e^x dx).
u=x^2, dv=e^x dx: x^2 e^x-integral(2x e^x dx).
Apply by parts again on integral(2x e^x dx): 2[xe^x-e^x].
Answer: x^2 e^x-2xe^x+2e^x+C=e^x(x^2-2x+2)+C.
Example 2: integral(dx/(x^2-4))=integral(dx/((x-2)(x+2))).
Partial fractions: 1/((x-2)(x+2))=(1/4)(1/(x-2)-1/(x+2)).
Answer=(1/4)ln|(x-2)/(x+2)|+C.
Example 3: integral(sin^3 x dx)=integral(sin x(1-cos^2 x) dx).
Let u=cos x: -integral((1-u^2) du)=-u+u^3/3+C=-cos x+cos^3 x/3+C.
COMMON MISTAKES:
ILATE: u should be chosen by ILATE order (leftmost=u).
Integration by parts may need to be applied multiple times.
King's rule: replace x with (a-x) inside integral, keep limits same.""",
    metadata={"source": "ncert", "topic": "calculus", "class_level": "class_12", "chapter": "ch7", "difficulty": "advanced"}),

    Document(page_content="""Class 12 | Ch8: Application of Integrals
AREA BETWEEN CURVE AND X-AXIS:
Area = integral[a to b] |f(x)| dx.
If f(x)>=0 on [a,b]: Area=integral[a to b] f(x) dx.
If f(x)<=0 on [a,b]: Area=|integral[a to b] f(x) dx|=-integral[a to b] f(x) dx.
If f changes sign: split at zeros, add absolute values of each part.
AREA BETWEEN TWO CURVES:
If f(x)>=g(x) on [a,b]: Area=integral[a to b] [f(x)-g(x)] dx.
Always integrate UPPER curve minus LOWER curve.
AREA USING Y-AXIS:
Area=integral[c to d] |g(y)| dy where x=g(y) is curve expressed in terms of y.
STANDARD AREAS:
Circle x^2+y^2=r^2: total area=pi*r^2. Using integration: 4×integral[0 to r] sqrt(r^2-x^2) dx.
Ellipse x^2/a^2+y^2/b^2=1: area=pi*a*b.
Parabola y^2=4ax and line x=h: area=(4/3)h*sqrt(ah) [to vertex from x=0 to x=h side].
SOLVED EXAMPLES:
Example 1: Area bounded by y=x^2 and y=x+2.
Intersection: x^2=x+2 → x^2-x-2=0 → (x-2)(x+1)=0 → x=-1,2.
Area=integral[-1 to 2] (x+2-x^2) dx=[x^2/2+2x-x^3/3] from -1 to 2.
=(2+4-8/3)-(-1/2-2+1/3... wait:
At x=2: 4/2+4-8/3=2+4-8/3=6-8/3=10/3.
At x=-1: 1/2-2+1/3=-7/6.
Area=10/3-(-7/6)=10/3+7/6=20/6+7/6=27/6=9/2 sq units.
Example 2: Area of circle x^2+y^2=16.
Area=4×integral[0 to 4] sqrt(16-x^2) dx=4×[x/2*sqrt(16-x^2)+8*sin^(-1)(x/4)] from 0 to 4.
=4×[0+8*pi/2-0]=4×4pi=16pi sq units. (Confirms pi*r^2=pi*16.)
Example 3: Area between y=x^2 and y=sqrt(x).
Intersection: x^2=sqrt(x) → x^4=x → x(x^3-1)=0 → x=0,1.
sqrt(x)>=x^2 on [0,1]. Area=integral[0 to 1](sqrt(x)-x^2)dx=[2x^(3/2)/3-x^3/3] from 0 to 1=2/3-1/3=1/3.
COMMON MISTAKES:
Always integrate UPPER minus LOWER (not absolute value of each separately).
Find intersection points by setting curves equal.
Area is always POSITIVE (use absolute values if needed).""",
    metadata={"source": "ncert", "topic": "calculus", "class_level": "class_12", "chapter": "ch8", "difficulty": "advanced"}),

    Document(page_content="""Class 12 | Ch9: Differential Equations
ORDER: order of highest derivative. DEGREE: power of highest derivative (after clearing fractions/roots).
FORMATION: differentiate given equation to eliminate arbitrary constants (number of constants=order).
METHODS OF SOLVING:
METHOD 1 - Variable Separable: f(x)dx=g(y)dy. Integrate both sides separately.
dy/dx=e^(x+y)=e^x*e^y → e^(-y)dy=e^x dx → -e^(-y)=e^x+C.
METHOD 2 - Homogeneous Equations: dy/dx=f(y/x). Substitute v=y/x, y=vx.
dy/dx=v+x*dv/dx. Equation becomes separable.
Identify homogeneous: if f(kx,ky)=k^n*f(x,y) (all terms same degree).
METHOD 3 - Linear DE: dy/dx+P(x)*y=Q(x).
Integrating factor IF=e^(integral P dx).
Solution: y*IF=integral(Q*IF dx)+C.
For dx/dy+P(y)*x=Q(y): IF=e^(integral P dy). x*IF=integral(Q*IF dy)+C.
STANDARD FORMS:
Variable separable: dy/dx=f(x)*g(y) → dy/g(y)=f(x)dx.
SOLVED EXAMPLES:
Example 1: Solve dy/dx=e^(x+y).
e^(-y)dy=e^x dx → -e^(-y)=e^x+C → e^x+e^(-y)=C1.
Example 2: Solve (x^2+y^2)dx=2xy dy (homogeneous).
dy/dx=(x^2+y^2)/(2xy). Put y=vx: v+x*dv/dx=(1+v^2)/(2v).
x*dv/dx=(1+v^2)/(2v)-v=(1-v^2)/(2v). 2v/(1-v^2)dv=dx/x.
-ln|1-v^2|=ln|x|+C1 → ln|x(1-v^2)|=-C1 → x(1-y^2/x^2)=C → x^2-y^2=Cx.
Example 3: Solve dy/dx+2y/x=x^2 (linear).
P=2/x, Q=x^2. IF=e^(integral 2/x dx)=e^(2ln x)=x^2.
y*x^2=integral(x^2*x^2 dx)=integral(x^4 dx)=x^5/5+C.
y=x^3/5+C/x^2.
COMMON MISTAKES:
Degree: power of HIGHEST ORDER derivative (after removing radicals).
Homogeneous: all terms must have SAME total degree.
Linear DE: coefficient of dy/dx must be 1 (divide through if needed).""",
    metadata={"source": "ncert", "topic": "calculus", "class_level": "class_12", "chapter": "ch9", "difficulty": "advanced"}),

    Document(page_content="""Class 12 | Ch10: Vector Algebra
VECTOR: quantity with magnitude and direction. Notation: a (bold) or a with arrow.
Unit vector: magnitude=1. a_hat=a/|a|.
TYPES: Zero vector, Unit vector, Coinitial, Collinear/Parallel, Equal vectors.
POSITION VECTOR: of point P(x,y,z): OP=xi+yj+zk. |OP|=sqrt(x^2+y^2+z^2).
OPERATIONS:
Addition: (a1i+a2j+a3k)+(b1i+b2j+b3k)=(a1+b1)i+(a2+b2)j+(a3+b3)k.
Scalar multiplication: k(ai+bj+ck)=kai+kbj+ckk.
DOT PRODUCT (Scalar product):
a.b=|a||b|cos(theta). a.b=a1b1+a2b2+a3b3.
a.b=0 iff perpendicular (or one is zero vector).
a.a=|a|^2. i.i=j.j=k.k=1. i.j=j.k=k.i=0.
CROSS PRODUCT (Vector product):
|a×b|=|a||b|sin(theta). Direction: right-hand rule.
a×b=det([[i,j,k],[a1,a2,a3],[b1,b2,b3]]).
=(a2b3-a3b2)i-(a1b3-a3b1)j+(a1b2-a2b1)k.
a×b=0 iff parallel. a×a=0. i×j=k, j×k=i, k×i=j. j×i=-k.
|a×b|=area of parallelogram with sides a and b.
(1/2)|a×b|=area of triangle.
SCALAR TRIPLE PRODUCT: [a b c]=a.(b×c). Volume of parallelepiped.
[a b c]=0 iff coplanar.
SOLVED EXAMPLES:
Example 1: a=2i+3j-k, b=i-2j+3k.
a.b=2(1)+3(-2)+(-1)(3)=2-6-3=-7.
|a|=sqrt(4+9+1)=sqrt(14). |b|=sqrt(1+4+9)=sqrt(14).
cos(theta)=-7/14=-1/2. theta=120°.
Example 2: a×b=det([[i,j,k],[2,3,-1],[1,-2,3]]).
=i(9-2)-j(6+1)+k(-4-3)=7i-7j-7k=7(i-j-k).
|a×b|=7sqrt(3). Area of parallelogram=7sqrt(3).
Example 3: Unit vector along 2i+3j+6k.
|v|=sqrt(4+9+36)=sqrt(49)=7. Unit vector=(2i+3j+6k)/7.
COMMON MISTAKES:
a.b is SCALAR. a×b is VECTOR.
i×j=k but j×i=-k (cross product NOT commutative).
a×b=0 means PARALLEL (not perpendicular). a.b=0 means PERPENDICULAR.""",
    metadata={"source": "ncert", "topic": "vectors", "class_level": "class_12", "chapter": "ch10", "difficulty": "advanced"}),

    Document(page_content="""Class 12 | Ch11: Three Dimensional Geometry
DIRECTION COSINES: cos(alpha), cos(beta), cos(gamma) where alpha,beta,gamma are angles line makes with x,y,z axes.
l=cos(alpha), m=cos(beta), n=cos(gamma). l^2+m^2+n^2=1.
DIRECTION RATIOS: proportional to direction cosines. a,b,c are DRs if l/a=m/b=n/c.
l=a/sqrt(a^2+b^2+c^2), m=b/sqrt(a^2+b^2+c^2), n=c/sqrt(a^2+b^2+c^2).
EQUATION OF LINE:
Vector form: r=a+lambda*b (a=point on line, b=direction vector).
Cartesian: (x-x1)/a=(y-y1)/b=(z-z1)/c (symmetric form).
Through two points: (x-x1)/(x2-x1)=(y-y1)/(y2-y1)=(z-z1)/(z2-z1).
ANGLE BETWEEN LINES:
cos(theta)=|l1l2+m1m2+n1n2|=|a1a2+b1b2+c1c2|/sqrt(a1^2+b1^2+c1^2)*sqrt(a2^2+b2^2+c2^2).
Parallel: a1/a2=b1/b2=c1/c2. Perpendicular: a1a2+b1b2+c1c2=0.
EQUATION OF PLANE:
General: ax+by+cz+d=0. Normal vector=(a,b,c).
Intercept form: x/a+y/b+z/c=1.
Vector form: r.n_hat=d (n_hat=unit normal).
Through three points: use determinant form.
DISTANCE FROM POINT TO PLANE:
Distance of (x1,y1,z1) from ax+by+cz+d=0: |ax1+by1+cz1+d|/sqrt(a^2+b^2+c^2).
ANGLE BETWEEN LINE AND PLANE:
sin(phi)=|al+bm+cn|/sqrt(a^2+b^2+c^2)*sqrt(l^2+m^2+n^2).
SKEW LINES: lines that are not parallel and do not intersect.
Shortest distance=|(a2-a1).(b1×b2)|/|b1×b2|.
SOLVED EXAMPLES:
Example 1: Angle between lines (x-1)/2=(y+1)/3=(z-2)/6 and (x+2)/1=(y-3)/4=(z+1)/2.
DRs: (2,3,6) and (1,4,2). cos(theta)=(2+12+12)/(7×sqrt(21))=26/(7sqrt(21)).
Example 2: Distance from (1,2,3) to plane 2x-3y+z=5.
d=|2(1)-3(2)+1(3)-5|/sqrt(4+9+1)=|2-6+3-5|/sqrt(14)=|-6|/sqrt(14)=6/sqrt(14)=3sqrt(14)/7.
Example 3: Shortest distance between skew lines.
r1=i+j+t(2i-j+k) and r2=2i+j-k+s(3i-5j+2k).
a1=i+j, a2=2i+j-k. b1=2i-j+k, b2=3i-5j+2k.
b1×b2=det([[i,j,k],[2,-1,1],[3,-5,2]])=i(-2+5)-j(4-3)+k(-10+3)=3i-j-7k.
|b1×b2|=sqrt(9+1+49)=sqrt(59).
(a2-a1)=i-k. (a2-a1).(b1×b2)=3+0+7=10.
Distance=|10|/sqrt(59)=10/sqrt(59).
COMMON MISTAKES:
Direction ratios are proportional to direction cosines (not equal unless normalised).
Skew lines: neither parallel nor intersecting (common in 3D, impossible in 2D).
Distance formula: use |...|/sqrt(a^2+b^2+c^2), not just |...|.""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_12", "chapter": "ch11", "difficulty": "advanced"}),

    Document(page_content="""Class 12 | Ch12: Linear Programming
LINEAR PROGRAMMING PROBLEM (LPP):
Objective function: Z=ax+by (to maximise or minimise).
Constraints: inequalities (ax+by<=c, x>=0, y>=0 etc).
Feasible region: set of all points satisfying ALL constraints simultaneously.
Feasible solution: any point in feasible region.
Optimal solution: feasible solution that gives maximum/minimum value of Z.
CORNER POINT METHOD (THEOREM):
If optimal solution exists, it occurs at a CORNER POINT (vertex) of feasible region.
Steps:
1. Graph all constraints. Find feasible region.
2. Find all corner points (vertices) of feasible region.
3. Evaluate Z at each corner point.
4. Maximum/minimum value of Z is the optimal solution.
TYPES OF LPP:
Bounded feasible region: has maximum AND minimum.
Unbounded feasible region: may not have maximum (for maximise) or minimum (for minimise).
Infeasible: no feasible region (constraints contradictory). No solution.
FORMULATING LPP FROM WORD PROBLEMS:
Identify: variables (what to find), objective (what to optimise), constraints (conditions).
SOLVED EXAMPLES:
Example 1: Maximise Z=3x+4y subject to x+y<=450, 2x+y<=600, x>=0, y>=0.
Corner points: O(0,0), A(300,0), B(150,300), C(0,450).
Z at O=0. Z at A=900. Z at B=450+1200=1650. Z at C=1800.
Maximum Z=1800 at C(0,450).
Example 2: Minimise Z=5x+7y subject to 2x+y>=8, x+2y>=10, x>=0, y>=0.
Corner points: A(0,8), B(2,4), C(10,0).
Z at A=56. Z at B=10+28=38. Z at C=50.
Minimum Z=38 at B(2,4).
FINDING CORNER POINTS: solve pairs of boundary equations simultaneously.
Intersection of 2x+y=600 and x+y=450: subtract → x=150, y=300.
COMMON MISTAKES:
Evaluate Z at ALL corner points (not just one or two).
Feasible region must satisfy ALL constraints (including x>=0, y>=0).
For minimum in unbounded region: check if solution is truly minimum.""",
    metadata={"source": "ncert", "topic": "algebra", "class_level": "class_12", "chapter": "ch12", "difficulty": "advanced"}),

    Document(page_content="""Class 12 | Ch13: Probability
CONDITIONAL PROBABILITY:
P(A|B)=P(A∩B)/P(B) where P(B)≠0.
P(A∩B)=P(A|B)*P(B)=P(B|A)*P(A).
MULTIPLICATION THEOREM:
P(A∩B)=P(A)*P(B|A). P(A∩B∩C)=P(A)*P(B|A)*P(C|AB).
INDEPENDENT EVENTS:
A and B independent: P(A∩B)=P(A)*P(B). P(A|B)=P(A).
A,B,C independent: P(A∩B)=P(A)P(B), P(B∩C)=P(B)P(C), P(A∩C)=P(A)P(C), AND P(A∩B∩C)=P(A)P(B)P(C). (All four conditions needed.)
TOTAL PROBABILITY THEOREM:
If B1,B2,...,Bn are mutually exclusive and exhaustive events:
P(A)=P(A|B1)*P(B1)+P(A|B2)*P(B2)+...+P(A|Bn)*P(Bn).
BAYES' THEOREM:
P(Bi|A)=P(A|Bi)*P(Bi) / [P(A|B1)*P(B1)+...+P(A|Bn)*P(Bn)].
Prior probability: P(Bi). Posterior probability: P(Bi|A).
RANDOM VARIABLE AND PROBABILITY DISTRIBUTION:
Random variable X: function from sample space to real numbers.
Mean (Expected value): E(X)=mu=sum(xi*P(xi)).
Variance: Var(X)=E(X^2)-[E(X)]^2=sum(xi^2*P(xi))-mu^2.
SD=sqrt(Var(X)).
BERNOULLI TRIALS AND BINOMIAL DISTRIBUTION:
n independent trials, each with probability p of success.
P(X=r)=nCr*p^r*(1-p)^(n-r)=nCr*p^r*q^(n-r) where q=1-p.
Mean=np. Variance=npq. SD=sqrt(npq).
SOLVED EXAMPLES:
Example 1: Bag A: 3R,5B. Bag B: 4R,6B. One bag chosen randomly, red ball drawn. Find P(bag A).
P(A)=P(B)=1/2. P(R|A)=3/8. P(R|B)=4/10=2/5.
P(R)=P(R|A)P(A)+P(R|B)P(B)=(3/8)(1/2)+(2/5)(1/2)=3/16+1/5=31/80.
P(A|R)=P(R|A)P(A)/P(R)=(3/16)/(31/80)=(3/16)*(80/31)=15/31.
Example 2: Binomial X~B(10,0.4). Find P(X=3).
P(X=3)=10C3*(0.4)^3*(0.6)^7=120*0.064*0.0279936≈0.2150.
Mean=10*0.4=4. Variance=10*0.4*0.6=2.4.
COMMON MISTAKES:
Bayes theorem: denominator is TOTAL probability P(A) using all branches.
Binomial: trials must be INDEPENDENT with CONSTANT probability p.
E(X^2) ≠ [E(X)]^2. Variance=E(X^2)-[E(X)]^2.""",
    metadata={"source": "ncert", "topic": "probability", "class_level": "class_12", "chapter": "ch13", "difficulty": "advanced"}),


    # ── JEE ADVANCED — 8 Topic Groups ───────────────────────────────

    Document(page_content="""JEE Advanced | Topic 1: Advanced Calculus
LIMITS - SPECIAL TECHNIQUES:
L'Hopital's Rule: if lim f(x)/g(x) gives 0/0 or inf/inf, then lim f(x)/g(x)=lim f'(x)/g'(x).
Apply repeatedly if still indeterminate. Works for 0/0, inf/inf forms.
Other indeterminate: 0×inf, inf-inf, 0^0, 1^inf, inf^0. Convert to 0/0 or inf/inf first.
1^inf form: lim[f(x)]^g(x) where f→1, g→inf. Take log: g(x)*ln(f(x))→inf×0. Use L'Hopital.
TAYLOR AND MACLAURIN SERIES:
e^x=1+x+x^2/2!+x^3/3!+... (all x).
sin x=x-x^3/3!+x^5/5!-... (all x).
cos x=1-x^2/2!+x^4/4!-... (all x).
ln(1+x)=x-x^2/2+x^3/3-... (|x|<=1, x≠-1).
(1+x)^n=1+nx+n(n-1)x^2/2!+... (|x|<1 for non-integer n).
LEIBNIZ THEOREM (nth derivative of product):
(fg)^(n)=sum(r=0 to n) nCr * f^(r) * g^(n-r).
DEFINITE INTEGRAL PROPERTIES:
King's rule: integral[a to b] f(x)dx=integral[a to b] f(a+b-x)dx.
integral[0 to 2a] f(x)dx=2*integral[0 to a] f(x)dx if f(2a-x)=f(x), else 0 if f(2a-x)=-f(x).
integral[-a to a] f(x)dx=2*integral[0 to a] f(x)dx if f even, else 0 if f odd.
Walli's formula: integral[0 to pi/2] sin^n(x)dx=integral[0 to pi/2] cos^n(x)dx.
For even n: (n-1)(n-3)...1 / n(n-2)...2 * pi/2.
For odd n: (n-1)(n-3)...2 / n(n-2)...1.
REDUCTION FORMULAS:
integral sin^n x dx = -sin^(n-1)x cosx/n + (n-1)/n * integral sin^(n-2)x dx.
SOLVED EXAMPLES:
Example 1: lim(x→0) (e^x-1-x)/x^2.
0/0 form. L'Hopital: lim (e^x-1)/(2x). Still 0/0.
L'Hopital again: lim e^x/2=1/2.
Example 2: Evaluate integral[0 to pi] x*sinx/(1+cos^2 x)dx.
By King's rule: I=integral[0 to pi] (pi-x)*sin(pi-x)/(1+cos^2(pi-x))dx.
sin(pi-x)=sinx. cos(pi-x)=-cosx. So I=integral[0 to pi] (pi-x)*sinx/(1+cos^2 x)dx.
2I=pi*integral[0 to pi] sinx/(1+cos^2 x)dx.
Let u=cosx: 2I=pi*integral[-1 to 1] du/(1+u^2)=pi[tan^(-1)u] from -1 to 1=pi[pi/4+pi/4]=pi^2/2.
I=pi^2/4.
Example 3: Using Maclaurin: find lim(x→0) (sinx-x)/x^3.
sinx=x-x^3/6+... So sinx-x=-x^3/6+... Divide by x^3: limit=-1/6.
COMMON MISTAKES:
L'Hopital: must be 0/0 or inf/inf EXACTLY. Cannot apply to 0/inf or inf+inf.
King's rule: limits stay SAME (a to b), replace x with a+b-x inside.
Taylor series: valid only within radius of convergence.""",
    metadata={"source": "ncert", "topic": "calculus", "class_level": "jee_advanced", "chapter": "advanced_calculus", "difficulty": "advanced"}),

    Document(page_content="""JEE Advanced | Topic 2: Advanced Algebra
THEORY OF EQUATIONS:
For polynomial p(x)=a_n*x^n+...+a_0 with roots r1,r2,...,rn:
Sum of roots=r1+r2+...+rn=-a_(n-1)/a_n.
Sum of products of pairs=a_(n-2)/a_n.
Sum of products of triplets=-a_(n-3)/a_n.
Product of all roots=(-1)^n * a_0/a_n.
Newton's identities relate power sums to elementary symmetric polynomials.
LOCATION OF ROOTS:
Both roots of ax^2+bx+c=0 positive: D>=0, -b/a>0, c/a>0.
Both roots negative: D>=0, -b/a<0, c/a>0.
Roots of opposite sign: c/a<0 (D automatically >0).
Both roots in (p,q): D>=0, f(p)>0 (same sign as a), f(q)>0, p<-b/2a<q.
COMMON ROOTS:
If ax^2+bx+c=0 and dx^2+ex+f=0 have common root alpha:
(bf-ce)^2=(ae-bd)(cd-af) (condition for one common root).
For both roots common: a/d=b/e=c/f.
SUM OF SERIES:
Telescoping: express term as f(n)-f(n-1), sum collapses.
1/(n(n+1))=1/n-1/(n+1). Sum from 1 to n = 1-1/(n+1).
Method of differences: if T_n can be expressed as f(n)-f(n-2), sum accordingly.
COMPLEX NUMBERS ADVANCED:
nth roots of unity: 1, omega, omega^2,...,omega^(n-1) where omega=e^(2pi*i/n).
Sum of all nth roots of unity=0. Product=(-1)^(n+1).
Roots evenly spaced on unit circle at angles 2pi*k/n.
SOLVED EXAMPLES:
Example 1: Roots of x^3-6x^2+11x-6=0 in AP. Find them.
Let roots be a-d, a, a+d. Sum=3a=6 → a=2. Product=a(a^2-d^2)=6 → 2(4-d^2)=6 → d^2=1 → d=1.
Roots: 1, 2, 3. Verify: sum of pairs=1*2+2*3+1*3=11. Product=6. Correct.
Example 2: Find sum of series 1/(1*2)+1/(2*3)+...+1/(n(n+1)).
T_k=1/(k(k+1))=1/k-1/(k+1). Telescoping sum=1-1/(n+1)=n/(n+1).
Example 3: Show sum of cube roots of unity=0.
1+omega+omega^2=0. (Sum of all nth roots of unity=0 for n>1.)
Geometric series: (1-omega^3)/(1-omega)=0/(1-omega)=0 since omega^3=1.
COMMON MISTAKES:
For roots in AP: take a-d, a, a+d (NOT a, a+d, a+2d — product is messier).
Telescoping: must identify the correct f(n) that gives the telescoping pattern.
Common roots: substitute the common root into BOTH equations, eliminate.""",
    metadata={"source": "ncert", "topic": "algebra", "class_level": "jee_advanced", "chapter": "advanced_algebra", "difficulty": "advanced"}),

    Document(page_content="""JEE Advanced | Topic 3: Advanced Coordinate Geometry
PAIR OF STRAIGHT LINES:
ax^2+2hxy+by^2=0 represents pair of lines through origin.
Slopes m1,m2: m1+m2=-2h/b, m1*m2=a/b.
Angle between lines: tan(theta)=2sqrt(h^2-ab)/(a+b).
Lines coincident: h^2=ab. Lines perpendicular: a+b=0.
Combined equation of lines through origin with slopes m1,m2: b(y-m1*x)(y-m2*x)=0.
General second degree: ax^2+2hxy+by^2+2gx+2fy+c=0.
Represents pair of lines if det([[a,h,g],[h,b,f],[g,f,c]])=0.
CIRCLES:
Radical axis of two circles: locus of points with equal power w.r.t. both circles.
Power of point P w.r.t. circle: PT^2=S1 where S1=x1^2+y1^2+2gx1+2fy1+c.
Radical axis: S1-S2=0 (subtract equations).
Coaxial circles: family of circles with common radical axis.
CONICS - ADVANCED:
Chord of contact from point (x1,y1) to circle x^2+y^2=a^2: xx1+yy1=a^2.
Chord of contact to ellipse x^2/a^2+y^2/b^2=1: xx1/a^2+yy1/b^2=1.
Parametric forms: Ellipse (a*cos t, b*sin t). Parabola (at^2, 2at). Hyperbola (a*sec t, b*tan t).
Normal at parametric point t on parabola y^2=4ax: y=-tx+2at+at^3.
Condition for line y=mx+c to be tangent to y^2=4ax: c=a/m.
LOCUS PROBLEMS:
Set up coordinates, use given conditions, eliminate parameter, simplify to standard form.
SOLVED EXAMPLES:
Example 1: 3x^2+10xy+8y^2=0. Find angle between lines.
a=3, 2h=10 so h=5, b=8. tan(theta)=2*sqrt(25-24)/(3+8)=2/11. theta=tan^(-1)(2/11).
Example 2: Chord of contact from (1,2) to circle x^2+y^2=25.
x(1)+y(2)=25 → x+2y=25.
Example 3: If z=x+iy and |z-2|=2|z-1|, find locus.
|(x-2)+iy|=2|(x-1)+iy|. (x-2)^2+y^2=4[(x-1)^2+y^2].
x^2-4x+4+y^2=4x^2-8x+4+4y^2. 3x^2+3y^2-4x=0. x^2+y^2-4x/3=0. Circle.
COMMON MISTAKES:
Pair of lines: 2hxy (coefficient of xy is 2h, not h).
Radical axis: subtract S1 and S2 equations directly (coefficients of x^2,y^2 must be 1 first).
Tangent condition: c=a/m for parabola y^2=4ax (from OUTSIDE).""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "jee_advanced", "chapter": "advanced_coord_geometry", "difficulty": "advanced"}),

    Document(page_content="""JEE Advanced | Topic 4: Advanced Trigonometry
PRODUCT FORMULAS:
sin A + sin B = 2 sin((A+B)/2) cos((A-B)/2).
sin A - sin B = 2 cos((A+B)/2) sin((A-B)/2).
cos A + cos B = 2 cos((A+B)/2) cos((A-B)/2).
cos A - cos B = -2 sin((A+B)/2) sin((A-B)/2).
sin A * sin B = (1/2)[cos(A-B)-cos(A+B)].
cos A * cos B = (1/2)[cos(A-B)+cos(A+B)].
sin A * cos B = (1/2)[sin(A+B)+sin(A-B)].
TRIGONOMETRIC EQUATIONS:
General solutions: sin(theta)=sin(alpha) → theta=n*pi+(-1)^n*alpha.
cos(theta)=cos(alpha) → theta=2n*pi±alpha.
tan(theta)=tan(alpha) → theta=n*pi+alpha.
For sin^2(theta)=sin^2(alpha): theta=n*pi±alpha.
CONDITIONAL IDENTITIES (when A+B+C=pi, i.e., angles of triangle):
sin2A+sin2B+sin2C=4sinA sinB sinC.
sinA+sinB+sinC=4cos(A/2)cos(B/2)cos(C/2).
cos A+cosB+cosC=1+4sin(A/2)sin(B/2)sin(C/2).
tan A+tanB+tanC=tanA tanB tanC (since A+B+C=pi).
INVERSE TRIG ADVANCED:
sin^(-1)x+sin^(-1)y=sin^(-1)(x*sqrt(1-y^2)+y*sqrt(1-x^2)) if x^2+y^2<=1.
tan^(-1)x+tan^(-1)y=pi+tan^(-1)((x+y)/(1-xy)) if x>0, y>0, xy>1.
TRIGONOMETRIC INEQUALITIES:
sin x > sin a for x in (a, pi-a) when a in (0, pi/2).
Solve by graphical method: draw y=sinx and horizontal line y=sin(a).
SOLVED EXAMPLES:
Example 1: Prove cos(pi/7)*cos(2pi/7)*cos(3pi/7)=1/8.
Use sin(2^n*A)=2^n*sinA*cosA*cos(2A)*...
sin(8pi/7)=sin(pi+pi/7)=-sin(pi/7).
2^3*sin(pi/7)*cos(pi/7)*cos(2pi/7)*cos(4pi/7)=sin(8pi/7)=-sin(pi/7).
8*sin(pi/7)*cos(pi/7)*cos(2pi/7)*cos(4pi/7)=-sin(pi/7).
cos(pi/7)*cos(2pi/7)*cos(4pi/7)=-1/8. Note cos(4pi/7)=cos(pi-3pi/7)=-cos(3pi/7).
So cos(pi/7)*cos(2pi/7)*(-(-cos(3pi/7)))... gives final answer 1/8.
Example 2: Solve sin2x-sinx=cosx-cos2x for x in [0,2pi].
sin2x+cos2x=sinx+cosx. 2sinx cosx+2cos^2x-1=sinx+cosx.
Let s=sinx, c=cosx. 2sc+2c^2-s-c-1=0. Factor: (2c-1)(c+s)... 
Try: (sinx+cosx)(2cosx-1)-(sinx+cosx)=0... 
(sinx+cosx-1)(2cosx-1)=0.
Case 1: sinx+cosx=1 → sqrt(2)sin(x+pi/4)=1 → x+pi/4=pi/4 or 3pi/4 → x=0 or pi/2.
Case 2: cosx=1/2 → x=pi/3 or 5pi/3.
Solutions: {0, pi/3, pi/2, 5pi/3}.
COMMON MISTAKES:
Sum-to-product and product-to-sum: memorise both directions.
Conditional identities: only valid when A+B+C=pi (triangle angles).
General solution: write COMPLETE general solution then find specific values in given interval.""",
    metadata={"source": "ncert", "topic": "trigonometry", "class_level": "jee_advanced", "chapter": "advanced_trigonometry", "difficulty": "advanced"}),

    Document(page_content="""JEE Advanced | Topic 5: Advanced Vectors and 3D Geometry
VECTOR ADVANCED RESULTS:
Scalar triple product [a b c]=a.(b×c)=b.(c×a)=c.(a×b).
[a b c]=det([[a1,a2,a3],[b1,b2,b3],[c1,c2,c3]]).
[a b c]=0 iff vectors coplanar.
[a+b, b+c, c+a]=2[a b c].
Vector triple product: a×(b×c)=(a.c)b-(a.b)c.
LINES IN 3D:
Symmetric form: (x-x1)/l=(y-y1)/m=(z-z1)/n.
Vector form: r=a+lambda*b.
Foot of perpendicular from point P to line: find lambda from (P-foot).b=0.
Image of point P in line: foot F is midpoint of P and image P'.
PLANES:
Equation through three points: use determinant form.
Foot of perpendicular from (x1,y1,z1) to ax+by+cz=d:
(x-x1)/a=(y-y1)/b=(z-z1)/c=-(ax1+by1+cz1-d)/(a^2+b^2+c^2).
Image of point in plane: foot is midpoint of point and image.
Angle bisector planes: locus of points equidistant from two planes.
SKEW LINES - SHORTEST DISTANCE:
SD=|(a2-a1).(b1×b2)|/|b1×b2|.
If SD=0: lines intersect (or are parallel).
SPHERE:
Equation: (x-a)^2+(y-b)^2+(z-c)^2=r^2. Centre (a,b,c), radius r.
General: x^2+y^2+z^2+2ux+2vy+2wz+d=0. Centre (-u,-v,-w), r=sqrt(u^2+v^2+w^2-d).
SOLVED EXAMPLES:
Example 1: Find foot of perpendicular from P(1,2,3) to line r=2i+j+t(i+2j+3k).
Point on line: Q=(2+t, 1+2t, 3t). PQ=(1+t, -1+2t, 3t-3).
PQ perpendicular to direction (1,2,3): (1+t)+2(-1+2t)+3(3t-3)=0.
1+t-2+4t+9t-9=0 → 14t=10 → t=5/7.
Foot: (2+5/7, 1+10/7, 15/7)=(19/7, 17/7, 15/7).
Example 2: Shortest distance between lines r=(i+j)+t(2i-j+k) and r=(2i+j-k)+s(3i-5j+2k).
b1×b2=|i j k; 2 -1 1; 3 -5 2|=i(-2+5)-j(4-3)+k(-10+3)=3i-j-7k. |b1×b2|=sqrt(59).
(a2-a1)=(i-k). (a2-a1).(b1×b2)=3+0+7=10. SD=10/sqrt(59)=10sqrt(59)/59.
Example 3: Prove [a+b, b+c, c+a]=2[a b c].
[a+b, b+c, c+a]=(a+b).((b+c)×(c+a)).
(b+c)×(c+a)=b×c+b×a+c×c+c×a=b×c-a×b+0+c×a.
(a+b).(b×c-a×b+c×a)=a.(b×c)+b.(b×c)-a.(a×b)-b.(a×b)+a.(c×a)+b.(c×a).
=[abc]+0-0-0+0+[bca]=[abc]+[abc]=2[abc]. Proved.
COMMON MISTAKES:
Vector triple product a×(b×c)≠(a×b)×c (NOT associative).
Shortest distance formula: (a2-a1) is difference of POSITION VECTORS of points on each line.
Coplanar vectors: [a b c]=0, NOT just any two being parallel.""",
    metadata={"source": "ncert", "topic": "vectors", "class_level": "jee_advanced", "chapter": "advanced_vectors_3d", "difficulty": "advanced"}),

    Document(page_content="""JEE Advanced | Topic 6: Advanced Probability
GEOMETRIC PROBABILITY:
When outcomes are continuous (length, area, volume based).
P(event)=favourable measure/total measure.
Example: Point chosen randomly in [0,1]. P(x^2<x)=P(0<x<1)=1 (since x^2<x for x in (0,1)).
DISTRIBUTIONS:
Binomial X~B(n,p): P(X=r)=nCr*p^r*q^(n-r). Mean=np. Var=npq.
Poisson X~P(lambda): P(X=r)=e^(-lambda)*lambda^r/r!. Mean=Var=lambda.
Used when n large, p small, np=lambda moderate.
Normal X~N(mu,sigma^2): P(a<X<b)=integral from a to b of (1/(sigma*sqrt(2pi)))*e^(-(x-mu)^2/(2sigma^2)).
Standardise: Z=(X-mu)/sigma. P(X<x)=P(Z<(x-mu)/sigma).
CONDITIONAL PROBABILITY ADVANCED:
Bayes with multiple stages.
P(A_k|B)=P(B|A_k)*P(A_k)/sum_i P(B|A_i)*P(A_i).
EXPECTED VALUE AND VARIANCE:
E(aX+b)=aE(X)+b. Var(aX+b)=a^2*Var(X).
E(X+Y)=E(X)+E(Y) (always). E(XY)=E(X)*E(Y) only if X,Y independent.
Var(X+Y)=Var(X)+Var(Y)+2Cov(X,Y). If independent: Cov=0 so Var(X+Y)=Var(X)+Var(Y).
MARKOV INEQUALITY: P(X>=a)<=E(X)/a for non-negative X.
CHEBYSHEV INEQUALITY: P(|X-mu|>=k*sigma)<=1/k^2.
SOLVED EXAMPLES:
Example 1: 4 cards from deck without replacement. P(all 4 suits).
Total ways=52C4=270725. Favourable: choose 1 from each suit=13^4=28561.
P=28561/270725=2197/20825.
Example 2: X~B(10,1/3). Find P(X=3) and mean.
P(X=3)=10C3*(1/3)^3*(2/3)^7=120*(1/27)*(128/2187)=120*128/(27*2187)=15360/59049≈0.260.
Mean=np=10/3≈3.33. Variance=npq=10*(1/3)*(2/3)=20/9.
Example 3: Three machines A,B,C produce 50%,30%,20% of items. Defect rates 2%,3%,4%.
Item defective. P(from machine A)?
P(D)=0.5*0.02+0.3*0.03+0.2*0.04=0.01+0.009+0.008=0.027.
P(A|D)=0.5*0.02/0.027=0.01/0.027=10/27.
COMMON MISTAKES:
Geometric probability: verify sample space is correctly defined.
Binomial: trials must be independent with constant p.
Bayes: identify all mutually exclusive exhaustive events (the partition).""",
    metadata={"source": "ncert", "topic": "probability", "class_level": "jee_advanced", "chapter": "advanced_probability", "difficulty": "advanced"}),

    Document(page_content="""JEE Advanced | Topic 7: Number Theory
DIVISIBILITY AND PRIMES:
Prime factorisation theorem: unique factorisation into primes.
Number of divisors of n=p1^a1*p2^a2*...*pk^ak is (a1+1)(a2+1)...(ak+1).
Sum of divisors=(p1^(a1+1)-1)/(p1-1) * (p2^(a2+1)-1)/(p2-1) * ...
EULER'S TOTIENT FUNCTION phi(n):
phi(n)=number of integers from 1 to n that are coprime to n.
phi(p)=p-1 for prime p. phi(p^k)=p^k-p^(k-1)=p^(k-1)(p-1).
phi(mn)=phi(m)*phi(n) if gcd(m,n)=1 (multiplicative).
phi(n)=n*(1-1/p1)*(1-1/p2)*...*(1-1/pk) where p1,...pk are distinct prime factors.
FERMAT'S LITTLE THEOREM:
If p is prime and gcd(a,p)=1: a^(p-1)≡1(mod p).
Equivalently: a^p≡a(mod p) for all a.
Used for: computing large powers mod prime, finding inverses mod prime.
EULER'S THEOREM (generalisation):
If gcd(a,n)=1: a^phi(n)≡1(mod n).
WILSON'S THEOREM:
(p-1)!≡-1(mod p) iff p is prime.
Converse: if (n-1)!≡-1(mod n) then n is prime.
CHINESE REMAINDER THEOREM (CRT):
System x≡a1(mod n1), x≡a2(mod n2) has unique solution mod n1*n2 if gcd(n1,n2)=1.
Solution: x=a1*M1*y1+a2*M2*y2 where M=n1*n2, Mi=M/ni, yi=Mi^(-1)(mod ni).
MODULAR ARITHMETIC:
(a+b)mod n=((a mod n)+(b mod n))mod n.
(a*b)mod n=((a mod n)*(b mod n))mod n.
Modular inverse of a mod n: find x such that ax≡1(mod n). Exists iff gcd(a,n)=1.
SOLVED EXAMPLES:
Example 1: Find last two digits of 7^100 (i.e., 7^100 mod 100).
phi(100)=phi(4)*phi(25)=2*20=40. gcd(7,100)=1.
7^40≡1(mod 100). 7^100=7^(40*2+20)=(7^40)^2*7^20≡7^20(mod 100).
7^2=49. 7^4=2401≡1(mod 100). 7^20=(7^4)^5≡1(mod 100).
Last two digits of 7^100 are 01.
Example 2: Prove 2^(p-1)≡1(mod p) for prime p=7.
2^6=64=63+1=9*7+1≡1(mod 7). Fermat's little theorem confirmed.
Example 3: phi(36)=phi(4)*phi(9)=2*6=12.
Integers from 1-36 coprime to 36: 12 such integers.
COMMON MISTAKES:
Fermat's little theorem: requires gcd(a,p)=1 (a not divisible by p).
phi is MULTIPLICATIVE only for coprime factors.
CRT requires moduli to be pairwise coprime.""",
    metadata={"source": "ncert", "topic": "number_theory", "class_level": "jee_advanced", "chapter": "number_theory", "difficulty": "advanced"}),

    Document(page_content="""JEE Advanced | Topic 8: Inequalities and Functional Equations
CLASSICAL INEQUALITIES:
AM-GM: (a1+a2+...+an)/n >= (a1*a2*...*an)^(1/n). Equality iff all equal.
For two numbers: (a+b)/2 >= sqrt(ab). So a+b >= 2*sqrt(ab).
AM-GM-HM chain: AM >= GM >= HM. HM=n/(1/a1+...+1/an). For two: 2ab/(a+b).
Cauchy-Schwarz: (a1^2+a2^2+...+an^2)(b1^2+...+bn^2) >= (a1b1+...+anbn)^2.
Equality iff a1/b1=a2/b2=...=an/bn (proportional).
Alternate form: (sum ai*bi)^2 <= (sum ai^2)(sum bi^2).
Power Mean inequality: if p>q then M_p >= M_q where M_p=((a1^p+...+an^p)/n)^(1/p).
Triangle inequality: |a+b| <= |a|+|b|. ||a|-|b|| <= |a-b|.
APPLICATIONS OF AM-GM:
Minimum of f(x)=x+1/x for x>0: by AM-GM, x+1/x >= 2*sqrt(x*1/x)=2. Min=2 at x=1.
Minimum of ax+b/x: 2*sqrt(ab). Attained at x=sqrt(b/a).
For PRODUCT fixed, SUM is minimised when equal.
For SUM fixed, PRODUCT is maximised when equal.
FUNCTIONAL EQUATIONS:
Find all functions satisfying given condition.
Common types:
f(x+y)=f(x)+f(y): Cauchy equation. Solution: f(x)=cx for continuous functions.
f(x+y)=f(x)*f(y): Solution f(x)=a^x.
f(xy)=f(x)+f(y): Solution f(x)=c*log(x).
APPROACH: substitute special values (x=0, x=y, y=0) to find constraints, then prove.
SOLVED EXAMPLES:
Example 1: Prove AM >= GM for 3 numbers a,b,c.
By AM-GM for 2 numbers: a+b >= 2*sqrt(ab). So a+b+c >= 2*sqrt(ab)+c.
Need 2*sqrt(ab)+c >= 3*(abc)^(1/3). Let p=sqrt(ab), q=c/2 (not quite right approach).
Direct: WLOG a+b+c=3 (normalise). Need abc<=1.
By AM-GM on a,b: (a+b)/2>=sqrt(ab). On (a+b)/2 and c: ((a+b)/2+c)/2>=sqrt((a+b)c/2).
Better: use substitution x=a^(1/3), y=b^(1/3), z=c^(1/3). x^3+y^3+z^3>=3xyz (standard identity).
Since x^3+y^3+z^3-3xyz=(x+y+z)(x^2+y^2+z^2-xy-yz-zx)>=0 (since x+y+z>0 and second factor>=0).
Example 2: Find min of (x+1/x)^2+(y+1/y)^2 given x,y>0, xy=1.
Since xy=1: y=1/x. Minimize f(x)=(x+1/x)^2+(1/x+x)^2=2(x+1/x)^2.
By AM-GM: x+1/x>=2. So f(x)>=2*4=8. Min=8 at x=y=1.
Example 3: Cauchy-Schwarz: (a^2+b^2)(c^2+d^2)>=(ac+bd)^2.
Proof: expand LHS-RHS=(ad-bc)^2>=0. QED.
COMMON MISTAKES:
AM-GM equality: ALL quantities must be EQUAL for equality to hold.
Cauchy-Schwarz: direction of inequality. LHS (product of sums of squares) >= RHS (square of sum of products).
For functional equations: proving f satisfies equation is NOT enough; must show it is the ONLY solution.""",
    metadata={"source": "ncert", "topic": "algebra", "class_level": "jee_advanced", "chapter": "inequalities", "difficulty": "advanced"}),

]

